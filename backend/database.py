import os
import sys
import json
import shutil
import sqlite3
from datetime import datetime


def _resolve_db_path() -> str:
    """
    Uses %LOCALAPPDATA%\\AksharaFlowStudio for Microsoft Store / standalone .exe compatibility
    (since Program Files / WindowsApps install directories are read-only).
    """
    local_app_data = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~")
    appdata_dir = os.path.join(local_app_data, "AksharaFlowStudio")
    os.makedirs(appdata_dir, exist_ok=True)
    target_db = os.path.join(appdata_dir, "aksharaflow_studio.db")

    # Migrate existing dev database if present and target_db doesn't exist yet
    if not os.path.exists(target_db) and not getattr(sys, "frozen", False):
        legacy_db = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "data",
            "typing_master_pro.db"
        )
        if os.path.exists(legacy_db):
            try:
                shutil.copy2(legacy_db, target_db)
            except Exception:
                pass

    return target_db


DB_PATH = _resolve_db_path()


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL COLLATE NOCASE,
        avatar_color TEXT DEFAULT '#e11d48',
        current_language TEXT DEFAULT 'en',
        current_lesson_id TEXT DEFAULT 'en_u1_l1',
        target_wpm INTEGER DEFAULT 40,
        total_practice_sec INTEGER DEFAULT 0,
        total_keystrokes INTEGER DEFAULT 0,
        streak_days INTEGER DEFAULT 1,
        last_active_date TEXT,
        settings_json TEXT DEFAULT '{"sound": true, "auto_inscript": true, "show_keyboard": true, "show_hands": true}',
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS lesson_progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        language TEXT NOT NULL,
        lesson_id TEXT NOT NULL,
        best_wpm REAL DEFAULT 0,
        best_net_wpm REAL DEFAULT 0,
        best_accuracy REAL DEFAULT 0,
        stars INTEGER DEFAULT 0,
        attempts INTEGER DEFAULT 0,
        completed INTEGER DEFAULT 0,
        last_practiced_at TEXT NOT NULL,
        UNIQUE(user_id, language, lesson_id),
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS session_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        language TEXT NOT NULL,
        lesson_id TEXT NOT NULL,
        lesson_title TEXT NOT NULL,
        mode TEXT NOT NULL,
        gross_wpm REAL NOT NULL,
        net_wpm REAL NOT NULL,
        accuracy REAL NOT NULL,
        duration_sec REAL NOT NULL,
        total_chars INTEGER NOT NULL,
        error_chars INTEGER NOT NULL,
        score INTEGER DEFAULT 0,
        weak_keys_json TEXT DEFAULT '{}',
        created_at TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS key_telemetry (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        language TEXT NOT NULL,
        expected_key TEXT NOT NULL,
        hits INTEGER DEFAULT 0,
        misses INTEGER DEFAULT 0,
        avg_latency_ms REAL DEFAULT 250.0,
        confused_with_json TEXT DEFAULT '{}',
        updated_at TEXT NOT NULL,
        UNIQUE(user_id, language, expected_key),
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """)

    conn.commit()
    conn.close()


AVATAR_COLORS = [
    "#e11d48", "#d97706", "#0d9488", "#7c3aed",
    "#059669", "#db2777", "#ea580c", "#2563eb"
]


def _resolve_lesson_for_language(cur, user_id: int, lang: str, existing_lesson_id: str = None):
    if existing_lesson_id and existing_lesson_id.startswith(f"{lang}_"):
        return existing_lesson_id
    cur.execute("""
        SELECT lesson_id FROM lesson_progress
        WHERE user_id = ? AND language = ?
        ORDER BY last_practiced_at DESC LIMIT 1
    """, (user_id, lang))
    row = cur.fetchone()
    if row:
        return row["lesson_id"]
    return f"{lang}_u1_l1"


def login_or_create_user(name: str, preferred_language: str = None):
    clean_name = name.strip()
    if not clean_name:
        raise ValueError("Name cannot be empty")

    now = datetime.now().isoformat(timespec="seconds")
    today = datetime.now().strftime("%Y-%m-%d")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = ? COLLATE NOCASE", (clean_name,))
    row = cur.fetchone()

    if row:
        user = dict(row)
        lang = preferred_language or user.get("current_language") or "en"
        lesson_id = _resolve_lesson_for_language(cur, user["id"], lang, user.get("current_lesson_id"))
        last_date = user.get("last_active_date")
        streak = user.get("streak_days") or 1
        if last_date and last_date != today:
            try:
                d1 = datetime.strptime(last_date, "%Y-%m-%d").date()
                d2 = datetime.strptime(today, "%Y-%m-%d").date()
                diff = (d2 - d1).days
                if diff == 1:
                    streak += 1
                elif diff > 1:
                    streak = 1
            except Exception:
                pass
        cur.execute("""
            UPDATE users
            SET last_active_date = ?, streak_days = ?, current_language = ?, current_lesson_id = ?, updated_at = ?
            WHERE id = ?
        """, (today, streak, lang, lesson_id, now, user["id"]))
        conn.commit()
        cur.execute("SELECT * FROM users WHERE id = ?", (user["id"],))
        user = dict(cur.fetchone())
    else:
        lang = preferred_language or "en"
        lesson_id = f"{lang}_u1_l1"
        color = AVATAR_COLORS[sum(ord(c) for c in clean_name) % len(AVATAR_COLORS)]
        cur.execute("""
            INSERT INTO users (name, avatar_color, current_language, current_lesson_id,
                               target_wpm, total_practice_sec, total_keystrokes,
                               streak_days, last_active_date, created_at, updated_at)
            VALUES (?, ?, ?, ?, 40, 0, 0, 1, ?, ?, ?)
        """, (clean_name, color, lang, lesson_id, today, now, now))
        conn.commit()
        user_id = cur.lastrowid
        cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user = dict(cur.fetchone())

    conn.close()
    user["settings"] = json.loads(user.get("settings_json") or "{}")
    return user


def list_all_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT u.*,
               COUNT(CASE WHEN lp.completed = 1 THEN 1 END) AS completed_lessons,
               COALESCE(MAX(lp.best_net_wpm), 0) AS peak_wpm,
               COALESCE(AVG(CASE WHEN lp.best_accuracy > 0 THEN lp.best_accuracy END), 0) AS avg_accuracy
        FROM users u
        LEFT JOIN lesson_progress lp ON u.id = lp.user_id AND lp.language = u.current_language
        GROUP BY u.id
        ORDER BY u.updated_at DESC
    """)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    for r in rows:
        r["settings"] = json.loads(r.get("settings_json") or "{}")
    return rows


def delete_user_profile(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM lesson_progress WHERE user_id = ?", (user_id,))
    cur.execute("DELETE FROM session_logs WHERE user_id = ?", (user_id,))
    cur.execute("DELETE FROM key_telemetry WHERE user_id = ?", (user_id,))
    cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()


def update_user_settings(user_id: int, settings: dict = None, target_wpm: int = None, current_language: str = None, current_lesson_id: str = None):
    now = datetime.now().isoformat(timespec="seconds")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = cur.fetchone()
    if not row:
        conn.close()
        return None
    user = dict(row)
    existing_settings = json.loads(user.get("settings_json") or "{}")
    if settings:
        existing_settings.update(settings)

    new_target = target_wpm if target_wpm is not None else user["target_wpm"]
    new_lang = current_language if current_language is not None else user["current_language"]
    if current_lesson_id is not None:
        new_lesson = current_lesson_id
    elif current_language is not None and current_language != user["current_language"]:
        new_lesson = _resolve_lesson_for_language(cur, user_id, new_lang)
    else:
        new_lesson = user["current_lesson_id"]

    cur.execute("""
        UPDATE users
        SET settings_json = ?, target_wpm = ?, current_language = ?, current_lesson_id = ?, updated_at = ?
        WHERE id = ?
    """, (json.dumps(existing_settings), new_target, new_lang, new_lesson, now, user_id))
    conn.commit()
    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    updated = dict(cur.fetchone())
    conn.close()
    updated["settings"] = json.loads(updated.get("settings_json") or "{}")
    return updated


def record_session_and_telemetry(
    user_id: int,
    language: str,
    lesson_id: str,
    lesson_title: str,
    mode: str,
    gross_wpm: float,
    net_wpm: float,
    accuracy: float,
    duration_sec: float,
    total_chars: int,
    error_chars: int,
    score: int,
    key_stats: dict,
    next_lesson_id: str = None
):
    now = datetime.now().isoformat(timespec="seconds")
    conn = get_connection()
    cur = conn.cursor()

    stars = 0
    completed = 0
    if accuracy >= 86.0 and net_wpm >= 8.0:
        completed = 1
        stars = 1
        if accuracy >= 93.0 and net_wpm >= 18.0:
            stars = 2
        if accuracy >= 97.0 and net_wpm >= 30.0:
            stars = 3

    session_weak = {}
    for k, st in (key_stats or {}).items():
        if st.get("misses", 0) > 0:
            session_weak[k] = st.get("misses", 0)

    cur.execute("""
        INSERT INTO session_logs (
            user_id, language, lesson_id, lesson_title, mode,
            gross_wpm, net_wpm, accuracy, duration_sec,
            total_chars, error_chars, score, weak_keys_json, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id, language, lesson_id, lesson_title, mode,
        round(gross_wpm, 1), round(net_wpm, 1), round(accuracy, 1),
        round(duration_sec, 1), total_chars, error_chars, score,
        json.dumps(session_weak, ensure_ascii=False), now
    ))

    if mode == "lesson":
        cur.execute("""
            SELECT * FROM lesson_progress
            WHERE user_id = ? AND language = ? AND lesson_id = ?
        """, (user_id, language, lesson_id))
        lp = cur.fetchone()
        if lp:
            lp = dict(lp)
            best_wpm = max(lp["best_wpm"], round(gross_wpm, 1))
            best_net = max(lp["best_net_wpm"], round(net_wpm, 1))
            best_acc = max(lp["best_accuracy"], round(accuracy, 1))
            best_stars = max(lp["stars"], stars)
            is_comp = max(lp["completed"], completed)
            cur.execute("""
                UPDATE lesson_progress
                SET best_wpm = ?, best_net_wpm = ?, best_accuracy = ?,
                    stars = ?, attempts = attempts + 1, completed = ?, last_practiced_at = ?
                WHERE id = ?
            """, (best_wpm, best_net, best_acc, best_stars, is_comp, now, lp["id"]))
        else:
            cur.execute("""
                INSERT INTO lesson_progress (
                    user_id, language, lesson_id, best_wpm, best_net_wpm,
                    best_accuracy, stars, attempts, completed, last_practiced_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, 1, ?, ?)
            """, (
                user_id, language, lesson_id, round(gross_wpm, 1),
                round(net_wpm, 1), round(accuracy, 1), stars, completed, now
            ))

    for expected_key, st in (key_stats or {}).items():
        if not expected_key:
            continue
        hits = int(st.get("hits", 0))
        misses = int(st.get("misses", 0))
        latencies = st.get("latencies", [])
        confused_new = st.get("confused_with", {})

        session_avg_lat = (sum(latencies) / len(latencies)) if latencies else None

        cur.execute("""
            SELECT * FROM key_telemetry
            WHERE user_id = ? AND language = ? AND expected_key = ?
        """, (user_id, language, expected_key))
        kt = cur.fetchone()
        if kt:
            kt = dict(kt)
            total_hits = kt["hits"] + hits
            total_misses = kt["misses"] + misses
            old_lat = kt["avg_latency_ms"] or 250.0
            if session_avg_lat is not None:
                new_lat = round(0.7 * old_lat + 0.3 * min(session_avg_lat, 1500.0), 1)
            else:
                new_lat = old_lat

            old_conf = json.loads(kt.get("confused_with_json") or "{}")
            for typed_char, cnt in confused_new.items():
                old_conf[typed_char] = old_conf.get(typed_char, 0) + int(cnt)

            cur.execute("""
                UPDATE key_telemetry
                SET hits = ?, misses = ?, avg_latency_ms = ?, confused_with_json = ?, updated_at = ?
                WHERE id = ?
            """, (total_hits, total_misses, new_lat, json.dumps(old_conf, ensure_ascii=False), now, kt["id"]))
        else:
            init_lat = round(min(session_avg_lat, 1500.0), 1) if session_avg_lat is not None else 250.0
            cur.execute("""
                INSERT INTO key_telemetry (
                    user_id, language, expected_key, hits, misses,
                    avg_latency_ms, confused_with_json, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                user_id, language, expected_key, hits, misses,
                init_lat, json.dumps(confused_new, ensure_ascii=False), now
            ))

    advance_lesson = next_lesson_id if (completed and next_lesson_id) else None
    if advance_lesson:
        cur.execute("""
            UPDATE users
            SET total_practice_sec = total_practice_sec + ?,
                total_keystrokes = total_keystrokes + ?,
                current_lesson_id = ?,
                updated_at = ?
            WHERE id = ?
        """, (int(round(duration_sec)), int(total_chars), advance_lesson, now, user_id))
    else:
        cur.execute("""
            UPDATE users
            SET total_practice_sec = total_practice_sec + ?,
                total_keystrokes = total_keystrokes + ?,
                updated_at = ?
            WHERE id = ?
        """, (int(round(duration_sec)), int(total_chars), now, user_id))

    conn.commit()
    conn.close()
    return {
        "stars": stars,
        "completed": bool(completed),
        "advanced_to": advance_lesson
    }


def get_user_dashboard_data(user_id: int, language: str = "en"):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    user_row = cur.fetchone()
    if not user_row:
        conn.close()
        return None
    user = dict(user_row)
    user["settings"] = json.loads(user.get("settings_json") or "{}")

    cur.execute("""
        SELECT * FROM lesson_progress
        WHERE user_id = ? AND language = ?
    """, (user_id, language))
    progress_rows = [dict(r) for r in cur.fetchall()]
    progress_map = {r["lesson_id"]: r for r in progress_rows}

    cur.execute("""
        SELECT * FROM session_logs
        WHERE user_id = ? AND language = ?
        ORDER BY id DESC LIMIT 40
    """, (user_id, language))
    sessions = [dict(r) for r in cur.fetchall()]
    for s in sessions:
        s["weak_keys"] = json.loads(s.get("weak_keys_json") or "{}")

    cur.execute("""
        SELECT * FROM key_telemetry
        WHERE user_id = ? AND language = ?
    """, (user_id, language))
    telemetry = [dict(r) for r in cur.fetchall()]
    for t in telemetry:
        t["confused_with"] = json.loads(t.get("confused_with_json") or "{}")
        total = t["hits"] + t["misses"]
        t["total_attempts"] = total
        t["error_rate"] = round((t["misses"] / total) * 100, 1) if total > 0 else 0.0
        t["accuracy"] = round((t["hits"] / total) * 100, 1) if total > 0 else 100.0

    conn.close()
    return {
        "user": user,
        "progress_map": progress_map,
        "recent_sessions": sessions,
        "telemetry": telemetry
    }
