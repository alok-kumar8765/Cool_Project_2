import os
import sys
import platform
import subprocess
import json
import datetime
from notifier import notify


# ================= BASE PATH (EXE SAFE) =================
def base_path():
    if getattr(sys, "frozen", False):
        # Running as compiled EXE
        return os.path.dirname(sys.executable)
    # Running as normal Python script
    return os.path.dirname(os.path.abspath(__file__))


BASE_DIR = base_path()
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

REPORT_FILE = os.path.join(DATA_DIR, "report.json")
ROLLBACK_FILE = os.path.join(DATA_DIR, "rollback.json")


# ================= COMMAND EXECUTION =================
def run(cmd):
    try:
        return subprocess.check_output(
            cmd, shell=True, text=True, stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as e:
        return e.output


# ================= JSON SAVE =================
def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# ================= OS DETECTION =================
def detect_os():
    return platform.system()


# ================= VERSION DETECTION =================
def get_outdated():
    os_name = detect_os()
    packages = []

    if os_name == "Windows":
        out = run("winget upgrade")
        for line in out.splitlines():
            if ">" in line:
                parts = line.split()
                if len(parts) >= 4:
                    packages.append({
                        "name": parts[0],
                        "current": parts[-3],
                        "latest": parts[-1]
                    })

    elif os_name == "Linux":
        out = run("apt list --upgradable")
        for line in out.splitlines()[1:]:
            try:
                name = line.split("/")[0]
                parts = line.split()
                packages.append({
                    "name": name,
                    "current": parts[1],
                    "latest": parts[2]
                })
            except IndexError:
                continue

    elif os_name == "Darwin":
        out = run("brew outdated --verbose")
        for line in out.splitlines():
            parts = line.split()
            if len(parts) >= 4:
                packages.append({
                    "name": parts[0],
                    "current": parts[1],
                    "latest": parts[3]
                })

    return packages


# ================= BACKUP FOR ROLLBACK =================
def backup_versions(packages):
    rollback_data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "packages": packages
    }
    save_json(ROLLBACK_FILE, rollback_data)


# ================= UPDATE =================
def update_all():
    os_name = detect_os()

    if os_name == "Windows":
        run(
            "winget upgrade --all --silent "
            "--accept-source-agreements --accept-package-agreements"
        )

    elif os_name == "Linux":
        run("apt update && apt upgrade -y")

    elif os_name == "Darwin":
        run("brew upgrade")


# ================= ROLLBACK =================
def rollback():
    if not os.path.exists(ROLLBACK_FILE):
        print("❌ No rollback data found")
        return

    with open(ROLLBACK_FILE, encoding="utf-8") as f:
        data = json.load(f)

    os_name = detect_os()

    for pkg in data.get("packages", []):
        name = pkg["name"]
        version = pkg["current"]

        if os_name == "Linux":
            run(f"apt install {name}={version} -y")

        elif os_name == "Darwin":
            run(f"brew install {name}@{version}")

        else:
            print(f"⚠ Rollback not supported for {name}")


# ================= MAIN =================
def main():
    outdated = get_outdated()

    if not outdated:
        notify("System Update", "All software is up to date ✅")
        return

    backup_versions(outdated)
    update_all()

    report = {
        "updated_at": datetime.datetime.now().isoformat(),
        "updated_packages": outdated
    }

    save_json(REPORT_FILE, report)
    notify("System Updated", json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
