# -*- coding: utf-8 -*-
import io
import os
import sys
import time
import json
import shutil
import socket
import winreg
import subprocess
import threading
import webbrowser
import urllib.request
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

LAST_HEARTBEAT_TS = time.time()
CLIENT_CONNECTED = False

# Guard stdout/stderr when compiled with PyInstaller --noconsole
if sys.stdout is None:
    sys.stdout = io.StringIO()
if sys.stderr is None:
    sys.stderr = io.StringIO()

if getattr(sys, "frozen", False):
    BASE_DIR = getattr(sys, "_MEIPASS", os.path.dirname(sys.executable))
    FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")
    BACKEND_DIR = os.path.join(BASE_DIR, "backend")
else:
    BACKEND_DIR = os.path.dirname(os.path.abspath(__file__))
    PROJECT_DIR = os.path.dirname(BACKEND_DIR)
    FRONTEND_DIR = os.path.join(PROJECT_DIR, "frontend")

if BACKEND_DIR not in sys.path:
    sys.path.insert(0, BACKEND_DIR)

from database import (
    init_db,
    login_or_create_user,
    list_all_users,
    delete_user_profile,
    update_user_settings,
    record_session_and_telemetry,
    get_user_dashboard_data,
)
from curriculum_en import (
    FINGER_LABELS,
    LANGUAGE_REGISTRY,
    get_units_for_language,
    get_speed_passages_for_language,
    get_finger_map_for_language,
    get_keymap_and_guide_for_language,
    get_all_lessons_flat,
    get_lesson_by_id,
)
from adaptive_engine import analyze_user_weaknesses, generate_remedial_drill


# ============================================================================
# MICROSOFT STORE WIN32 SILENT INSTALLER & UNINSTALLER SUPPORT (/S, --install, --uninstall)
# ============================================================================
UNINSTALL_REG_KEY = r"Software\Microsoft\Windows\CurrentVersion\Uninstall\AksharaFlowStudio"


def get_install_dir() -> str:
    local_app_data = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~")
    return os.path.join(local_app_data, "Programs", "AksharaFlowStudio")


def create_windows_shortcut(target_exe: str, shortcut_path: str, description: str):
    ps_script = (
        f'$ws = New-Object -ComObject WScript.Shell; '
        f'$s = $ws.CreateShortcut("{shortcut_path}"); '
        f'$s.TargetPath = "{target_exe}"; '
        f'$s.WorkingDirectory = "{os.path.dirname(target_exe)}"; '
        f'$s.Description = "{description}"; '
        f'$s.IconLocation = "{target_exe},0"; '
        f'$s.Save()'
    )
    try:
        subprocess.run(
            ["powershell", "-NoProfile", "-WindowStyle", "Hidden", "-Command", ps_script],
            check=False,
            creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, "CREATE_NO_WINDOW") else 0,
        )
    except Exception:
        pass


def perform_silent_install():
    """
    Installs AksharaFlow_Studio.exe into %LOCALAPPDATA%\\Programs\\AksharaFlowStudio,
    creates Start Menu & Desktop shortcuts, and registers in Windows Add/Remove Programs
    for Microsoft Store Win32 package compliance.
    """
    install_dir = get_install_dir()
    os.makedirs(install_dir, exist_ok=True)
    current_exe = sys.executable if getattr(sys, "frozen", False) else os.path.abspath(__file__)
    target_exe = os.path.join(install_dir, "AksharaFlow_Studio.exe")

    if os.path.abspath(current_exe).lower() != os.path.abspath(target_exe).lower():
        try:
            shutil.copy2(current_exe, target_exe)
        except Exception:
            target_exe = current_exe

    # Create Start Menu & Desktop shortcuts
    appdata = os.environ.get("APPDATA") or os.path.expanduser("~")
    start_menu_dir = os.path.join(appdata, r"Microsoft\Windows\Start Menu\Programs")
    desktop_dir = os.path.join(os.path.expanduser("~"), "Desktop")

    create_windows_shortcut(
        target_exe,
        os.path.join(start_menu_dir, "AksharaFlow Studio.lnk"),
        "AksharaFlow Studio — Free 14-Script Touch-Typing Coach",
    )
    create_windows_shortcut(
        target_exe,
        os.path.join(desktop_dir, "AksharaFlow Studio.lnk"),
        "AksharaFlow Studio — Free 14-Script Touch-Typing Coach",
    )

    # Register in Windows Uninstall Registry (HKCU)
    try:
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, UNINSTALL_REG_KEY) as key:
            winreg.SetValueEx(key, "DisplayName", 0, winreg.REG_SZ, "AksharaFlow Studio")
            winreg.SetValueEx(key, "DisplayVersion", 0, winreg.REG_SZ, "1.0.0.0")
            winreg.SetValueEx(key, "Publisher", 0, winreg.REG_SZ, "AksharaFlow Open Education")
            winreg.SetValueEx(key, "DisplayIcon", 0, winreg.REG_SZ, target_exe)
            winreg.SetValueEx(key, "InstallLocation", 0, winreg.REG_SZ, install_dir)
            winreg.SetValueEx(key, "UninstallString", 0, winreg.REG_SZ, f'"{target_exe}" --uninstall')
            winreg.SetValueEx(key, "QuietUninstallString", 0, winreg.REG_SZ, f'"{target_exe}" --uninstall --silent')
            winreg.SetValueEx(key, "NoModify", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key, "NoRepair", 0, winreg.REG_DWORD, 1)
            winreg.SetValueEx(key, "EstimatedSize", 0, winreg.REG_DWORD, 9600)
    except Exception:
        pass

    return 0


def perform_silent_uninstall():
    """Removes shortcuts and Windows Uninstall Registry entry."""
    appdata = os.environ.get("APPDATA") or os.path.expanduser("~")
    start_menu_lnk = os.path.join(appdata, r"Microsoft\Windows\Start Menu\Programs", "AksharaFlow Studio.lnk")
    desktop_lnk = os.path.join(os.path.expanduser("~"), "Desktop", "AksharaFlow Studio.lnk")

    for lnk in (start_menu_lnk, desktop_lnk):
        if os.path.exists(lnk):
            try:
                os.remove(lnk)
            except Exception:
                pass

    try:
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, UNINSTALL_REG_KEY)
    except Exception:
        pass

    return 0


def build_full_user_payload(user_id: int, language: str = None):
    dash_initial = get_user_dashboard_data(user_id, "en")
    if not dash_initial:
        return None
    lang = language or dash_initial["user"].get("current_language") or "en"
    dash = get_user_dashboard_data(user_id, lang)

    weakness = analyze_user_weaknesses(dash["telemetry"], lang)
    remedial = generate_remedial_drill(dash["telemetry"], None, lang)
    km_info = get_keymap_and_guide_for_language(lang)

    return {
        "user": dash["user"],
        "active_language": lang,
        "progress_map": dash["progress_map"],
        "recent_sessions": dash["recent_sessions"],
        "telemetry": dash["telemetry"],
        "weakness_analysis": weakness,
        "recommended_remedial": remedial,
        "units": get_units_for_language(lang),
        "all_lessons": get_all_lessons_flat(lang),
        "speed_passages": get_speed_passages_for_language(lang),
        "finger_map": get_finger_map_for_language(lang),
        "finger_labels": FINGER_LABELS,
        "languages": LANGUAGE_REGISTRY,
        "inscript_keymap": km_info["keymap"],
        "inscript_setup_guide": km_info["setup_guide"],
        "native_vocab": km_info["vocab"],
    }


class TypingMasterRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=FRONTEND_DIR, **kwargs)

    def log_message(self, format, *args):
        pass

    def _send_json(self, data: dict, status: int = 200):
        payload = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)

    def _read_body(self) -> dict:
        length = int(self.headers.get("Content-Length", 0))
        if length <= 0:
            return {}
        raw = self.rfile.read(length).decode("utf-8")
        return json.loads(raw) if raw else {}

    def do_GET(self):
        global LAST_HEARTBEAT_TS, CLIENT_CONNECTED
        LAST_HEARTBEAT_TS = time.time()
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/api/health":
            return self._send_json({"ok": True, "app": "AksharaFlow Studio"})

        if path == "/api/heartbeat":
            CLIENT_CONNECTED = True
            return self._send_json({"ok": True})

        if path == "/api/users":
            CLIENT_CONNECTED = True
            users = list_all_users()
            return self._send_json({
                "ok": True,
                "users": users,
                "languages": LANGUAGE_REGISTRY
            })

        return super().do_GET()

    def do_POST(self):
        global LAST_HEARTBEAT_TS, CLIENT_CONNECTED
        LAST_HEARTBEAT_TS = time.time()
        CLIENT_CONNECTED = True
        parsed = urlparse(self.path)
        path = parsed.path
        try:
            body = self._read_body()
        except Exception as e:
            return self._send_json({"ok": False, "error": str(e)}, 400)

        try:
            if path == "/api/login":
                name = (body.get("name") or "").strip()
                preferred_language = (body.get("language") or "").strip() or None
                if not name:
                    return self._send_json({"ok": False, "error": "Please enter your name."}, 400)
                user = login_or_create_user(name, preferred_language)
                payload = build_full_user_payload(user["id"], user.get("current_language", "en"))
                return self._send_json({"ok": True, "data": payload})

            elif path == "/api/delete_user":
                user_id = int(body.get("user_id", 0))
                if user_id:
                    delete_user_profile(user_id)
                return self._send_json({"ok": True, "users": list_all_users()})

            elif path == "/api/settings":
                user_id = int(body.get("user_id", 0))
                updated = update_user_settings(
                    user_id=user_id,
                    settings=body.get("settings"),
                    target_wpm=body.get("target_wpm"),
                    current_language=body.get("current_language"),
                    current_lesson_id=body.get("current_lesson_id"),
                )
                lang = updated.get("current_language", "en") if updated else "en"
                payload = build_full_user_payload(user_id, lang)
                return self._send_json({"ok": True, "data": payload})

            elif path == "/api/remedial_drill":
                user_id = int(body.get("user_id", 0))
                language = body.get("language", "en")
                custom_keys = body.get("focus_keys")
                dash = get_user_dashboard_data(user_id, language)
                telemetry = dash["telemetry"] if dash else []
                drill = generate_remedial_drill(telemetry, custom_keys, language)
                return self._send_json({"ok": True, "drill": drill})

            elif path == "/api/record_session":
                user_id = int(body.get("user_id", 0))
                language = body.get("language", "en")
                lesson_id = body.get("lesson_id", f"{language}_u1_l1")
                lesson_title = body.get("lesson_title", "Practice Session")
                mode = body.get("mode", "lesson")
                gross_wpm = float(body.get("gross_wpm", 0))
                net_wpm = float(body.get("net_wpm", 0))
                accuracy = float(body.get("accuracy", 0))
                duration_sec = float(body.get("duration_sec", 1))
                total_chars = int(body.get("total_chars", 0))
                error_chars = int(body.get("error_chars", 0))
                score = int(body.get("score", 0))
                key_stats = body.get("key_stats", {})

                lesson_obj = get_lesson_by_id(lesson_id, language) if mode == "lesson" else None
                next_lesson_id = lesson_obj.get("next_lesson_id") if lesson_obj else None

                result = record_session_and_telemetry(
                    user_id=user_id,
                    language=language,
                    lesson_id=lesson_id,
                    lesson_title=lesson_title,
                    mode=mode,
                    gross_wpm=gross_wpm,
                    net_wpm=net_wpm,
                    accuracy=accuracy,
                    duration_sec=duration_sec,
                    total_chars=total_chars,
                    error_chars=error_chars,
                    score=score,
                    key_stats=key_stats,
                    next_lesson_id=next_lesson_id,
                )

                payload = build_full_user_payload(user_id, language)
                return self._send_json({
                    "ok": True,
                    "session_result": result,
                    "data": payload
                })

            else:
                return self._send_json({"ok": False, "error": "Unknown API endpoint"}, 404)

        except Exception as e:
            return self._send_json({"ok": False, "error": str(e)}, 500)


def is_aksharaflow_running(port: int) -> bool:
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/api/health", timeout=0.6) as resp:
            if resp.status == 200:
                data = json.loads(resp.read().decode("utf-8"))
                return data.get("app") == "AksharaFlow Studio"
    except Exception:
        return False
    return False


def find_free_port(preferred: int = 8765) -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        if s.connect_ex(("127.0.0.1", preferred)) != 0:
            return preferred
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def launch_desktop_window(url: str):
    """Launches a standalone native desktop window."""
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    ]
    local_app_data = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~")
    profile_dir = os.path.join(local_app_data, "AksharaFlowStudio", "WindowRuntime")
    os.makedirs(profile_dir, exist_ok=True)

    for ep in edge_paths:
        if os.path.exists(ep):
            return subprocess.Popen([
                ep,
                f"--app={url}",
                f"--user-data-dir={profile_dir}",
                "--window-size=1400,880",
                "--disable-extensions",
                "--no-first-run",
            ])
    webbrowser.open(url)
    return None


def main():
    global LAST_HEARTBEAT_TS, CLIENT_CONNECTED
    args_lower = [a.lower() for a in sys.argv[1:]]
    if any(flag in args_lower for flag in ("/s", "/silent", "/verysilent", "--install")):
        sys.exit(perform_silent_install())
    if any(flag in args_lower for flag in ("/u", "/uninstall", "--uninstall")):
        sys.exit(perform_silent_uninstall())

    init_db()
    preferred_port = 8765

    # If AksharaFlow Studio is already running, just open a window to it and exit
    if is_aksharaflow_running(preferred_port):
        if "--no-window" not in sys.argv:
            launch_desktop_window(f"http://127.0.0.1:{preferred_port}")
        return

    port = find_free_port(preferred_port)
    url = f"http://127.0.0.1:{port}"
    server = ThreadingHTTPServer(("127.0.0.1", port), TypingMasterRequestHandler)
    LAST_HEARTBEAT_TS = time.time()
    CLIENT_CONNECTED = False

    if getattr(sys, "frozen", False):
        server_thread = threading.Thread(target=server.serve_forever, daemon=True)
        server_thread.start()
        time.sleep(0.25)

        if "--no-window" not in sys.argv:
            launch_desktop_window(url)

        # Keep server alive while the desktop window sends heartbeats (survives Edge broker handoff!)
        start_ts = time.time()
        try:
            while True:
                time.sleep(2.0)
                now = time.time()
                if CLIENT_CONNECTED:
                    # Shut down cleanly 18 seconds after the user closes the window
                    if now - LAST_HEARTBEAT_TS > 18.0:
                        break
                else:
                    # Startup grace period of 60 seconds waiting for browser window to load
                    if now - start_ts > 60.0:
                        break
        finally:
            server.shutdown()
            server.server_close()
    else:
        print("=" * 64)
        print("  AKSHARAFLOW STUDIO — FREE PUBLIC MULTI-SCRIPT TYPING COACH")
        print(f"  Local Engine Running at: {url}")
        print("  14 Scripts Active: English + 13 Indian InScript Languages")
        print("=" * 64)

        if "--no-window" not in sys.argv:
            threading.Timer(0.4, lambda: launch_desktop_window(url)).start()

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            server.server_close()


if __name__ == "__main__":
    main()
