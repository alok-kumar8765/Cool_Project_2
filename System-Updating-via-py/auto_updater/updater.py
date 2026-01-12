import os, platform, subprocess, json, datetime
from notifier import notify

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

REPORT_FILE = os.path.join(DATA_DIR, "report.json")
ROLLBACK_FILE = os.path.join(DATA_DIR, "rollback.json")


def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True)


def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)


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
                packages.append({
                    "name": parts[0],
                    "current": parts[-3],
                    "latest": parts[-1]
                })

    elif os_name == "Linux":
        out = run("apt list --upgradable")
        for line in out.splitlines()[1:]:
            name = line.split("/")[0]
            versions = line.split()
            packages.append({
                "name": name,
                "current": versions[1],
                "latest": versions[2]
            })

    elif os_name == "Darwin":
        out = run("brew outdated --verbose")
        for line in out.splitlines():
            parts = line.split()
            packages.append({
                "name": parts[0],
                "current": parts[1],
                "latest": parts[3]
            })

    return packages


# ================= BACKUP FOR ROLLBACK =================
def backup_versions(packages):
    rollback = {
        "timestamp": str(datetime.datetime.now()),
        "packages": packages
    }
    save_json(ROLLBACK_FILE, rollback)


# ================= UPDATE =================
def update_all():
    os_name = detect_os()

    if os_name == "Windows":
        run("winget upgrade --all --silent --accept-source-agreements --accept-package-agreements")

    elif os_name == "Linux":
        run("apt update && apt upgrade -y")

    elif os_name == "Darwin":
        run("brew upgrade")


# ================= ROLLBACK =================
def rollback():
    if not os.path.exists(ROLLBACK_FILE):
        print("❌ No rollback data")
        return

    data = json.load(open(ROLLBACK_FILE))
    os_name = detect_os()

    for pkg in data["packages"]:
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
        "updated_at": str(datetime.datetime.now()),
        "updated_packages": outdated
    }

    save_json(REPORT_FILE, report)
    notify("System Updated", json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
