# -*- coding: utf-8 -*-
"""
AksharaFlow Studio — Zero-Dependency GitHub Repository & Release Publisher
Uses Python's built-in urllib.request + official GitHub REST API (no git.exe required!):
1. Creates a new public GitHub repository: 'AksharaFlow-Studio'
2. Uploads all source code, icons, store logos, and documentation
3. Creates GitHub Release v1.0.0 and uploads 'dist/AksharaFlow_Studio.exe'
4. Outputs the direct HTTPS download URL ready to paste into Microsoft Store Partner Center!
"""

import os
import sys
import json
import base64
import urllib.request
import urllib.error

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_NAME = "AksharaFlow-Studio-"
REPO_DESC = "AksharaFlow Studio — 100% Free Offline 14-Script Touch-Typing Coach & Arcade (English + 13 Indian InScript Languages)"

FILES_TO_UPLOAD = [
    "README.md",
    "LICENSE",
    ".gitignore",
    "MICROSOFT_STORE_SUBMISSION.md",
    "version_info.txt",
    "build_assets.py",
    "build_exe.bat",
    "publish_to_github.py",
    "Start_TypingMaster_Pro.bat",
    "backend/app.py",
    "backend/database.py",
    "backend/curriculum_en.py",
    "backend/curriculum_inscript.py",
    "backend/adaptive_engine.py",
    "frontend/index.html",
    "frontend/styles.css",
    "frontend/app.js",
    "frontend/games.js",
    "assets/aksharaflow.ico",
    "assets/store_logos/StoreLogo_300x300.png",
    "assets/store_logos/Square150x150Logo.png",
    "assets/store_logos/Square310x310Logo.png",
]


def github_api(method: str, url: str, token: str, data=None, content_type="application/json"):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "AksharaFlow-Studio-Publisher",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    body = None
    if data is not None:
        if isinstance(data, (bytes, bytearray)):
            body = data
            headers["Content-Type"] = content_type
        else:
            body = json.dumps(data).encode("utf-8")
            headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw = resp.read().decode("utf-8")
            return resp.status, (json.loads(raw) if raw else {})
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        try:
            err_json = json.loads(err_body)
        except Exception:
            err_json = {"message": err_body}
        return e.code, err_json


def main():
    print("=" * 72)
    print("  AKSHARAFLOW STUDIO — GITHUB REPO & RELEASE v1.0.0 PUBLISHER")
    print("=" * 72)

    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if len(sys.argv) > 1 and sys.argv[1].strip():
        token = sys.argv[1].strip()

    if not token:
        print("\nTo push this repository and upload AksharaFlow_Studio.exe to GitHub,")
        print("please paste your GitHub Personal Access Token (with 'repo' scope):")
        print("  (Create one at: https://github.com/settings/tokens/new?scopes=repo )\n")
        token = input("GitHub Token (ghp_...): ").strip()

    if not token:
        print("Error: No GitHub token provided.")
        sys.exit(1)

    # 1. Verify authenticated user
    status, user_info = github_api("GET", "https://api.github.com/user", token)
    if status != 200:
        print(f"Authentication failed ({status}): {user_info.get('message')}")
        sys.exit(1)

    username = user_info["login"]
    print(f"\n[1/4] Authenticated as GitHub user: {username}")

    # 2. Create or verify repository
    status, repo_info = github_api(
        "POST",
        "https://api.github.com/user/repos",
        token,
        {
            "name": REPO_NAME,
            "description": REPO_DESC,
            "private": False,
            "auto_init": True,
        },
    )
    if status in (200, 201):
        print(f"[2/4] Created new public repository: https://github.com/{username}/{REPO_NAME}")
    elif status == 422:
        print(f"[2/4] Repository already exists: https://github.com/{username}/{REPO_NAME}")
    else:
        print(f"Failed to create repository ({status}): {repo_info}")
        sys.exit(1)

    # 3. Upload all source files
    print(f"[3/4] Uploading {len(FILES_TO_UPLOAD)} project files to GitHub...")
    for rel_path in FILES_TO_UPLOAD:
        abs_path = os.path.join(PROJECT_DIR, rel_path.replace("/", os.sep))
        if not os.path.exists(abs_path):
            continue
        with open(abs_path, "rb") as f:
            b64_content = base64.b64encode(f.read()).decode("ascii")

        api_url = f"https://api.github.com/repos/{username}/{REPO_NAME}/contents/{rel_path}"
        # Check if file exists to get sha
        st_get, existing = github_api("GET", api_url, token)
        payload = {
            "message": f"Add/update {rel_path}",
            "content": b64_content,
        }
        if st_get == 200 and isinstance(existing, dict) and existing.get("sha"):
            payload["sha"] = existing["sha"]

        st_put, res_put = github_api("PUT", api_url, token, payload)
        if st_put in (200, 201):
            print(f"  ✓ Uploaded {rel_path}")
        else:
            print(f"  ! Warning on {rel_path} ({st_put}): {res_put.get('message')}")

    # 4. Create Release v1.0.0 and attach AksharaFlow_Studio.exe
    exe_path = os.path.join(PROJECT_DIR, "dist", "AksharaFlow_Studio.exe")
    if os.path.exists(exe_path):
        print("\n[4/4] Creating GitHub Release v1.0.0 & uploading AksharaFlow_Studio.exe...")
        rel_url = f"https://api.github.com/repos/{username}/{REPO_NAME}/releases"
        st_rel, rel_data = github_api(
            "POST",
            rel_url,
            token,
            {
                "tag_name": "v1.0.0",
                "name": "AksharaFlow Studio v1.0.0 (Windows Standalone & Store Installer)",
                "body": (
                    "### 🦉 AksharaFlow Studio v1.0.0\n"
                    "- **14 Scripts Supported:** English (QWERTY) + 13 Indian Languages (InScript)\n"
                    "- **310 Progressive Lessons** (including Gunintalu / Barakhadi / Kagunita / Uyirmei & `d+d` ZWNJ loanword breaks)\n"
                    "- **Proper Indic Akshara Cluster Shaping** (zero dotted circles) + **Auto-Collapse Focus Mode**\n"
                    "- **Adaptive Mistake Coach** + **3 Multi-Script Canvas Arcade Games**\n"
                    "- **Microsoft Store Win32 Compliant:** Supports silent installation via `/S`"
                ),
                "draft": False,
                "prerelease": False,
            },
        )
        if st_rel == 422:
            # Release already exists, fetch it
            _, rel_data = github_api(
                "GET",
                f"https://api.github.com/repos/{username}/{REPO_NAME}/releases/tags/v1.0.0",
                token,
            )

        # If AksharaFlow_Studio.exe already exists on this release, delete the old asset first so it updates cleanly
        for asset in rel_data.get("assets", []):
            if asset.get("name") == "AksharaFlow_Studio.exe" and asset.get("id"):
                github_api(
                    "DELETE",
                    f"https://api.github.com/repos/{username}/{REPO_NAME}/releases/assets/{asset['id']}",
                    token,
                )

        upload_url_template = rel_data.get("upload_url", "")
        if upload_url_template:
            upload_base = upload_url_template.split("{")[0]
            asset_url = f"{upload_base}?name=AksharaFlow_Studio.exe"
            with open(exe_path, "rb") as ef:
                exe_bytes = ef.read()
            st_up, up_data = github_api(
                "POST",
                asset_url,
                token,
                exe_bytes,
                content_type="application/vnd.microsoft.portable-executable",
            )
            if st_up in (200, 201):
                dl_url = up_data.get("browser_download_url")
                print("\n" + "=" * 72)
                print("  🎉 SUCCESS! REPOSITORY & RELEASE PUBLISHED TO GITHUB!")
                print(f"  GitHub Repo URL : https://github.com/{username}/{REPO_NAME}")
                print(f"  Direct .EXE URL : {dl_url}")
                print("  (Paste the Direct .EXE URL above into Microsoft Store Partner Center!)")
                print("=" * 72)
            else:
                print(f"  Release created! Upload status ({st_up}): {up_data.get('message')}")
                print(f"  Direct .EXE URL : https://github.com/{username}/{REPO_NAME}/releases/download/v1.0.0/AksharaFlow_Studio.exe")

    print("\nDone!")


if __name__ == "__main__":
    main()
