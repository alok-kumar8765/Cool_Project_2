import platform
import subprocess
import shutil
import sys


def command_exists(cmd):
    return shutil.which(cmd) is not None


def run_command(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running command: {' '.join(command)}")
        print(e)


# ===================== WINDOWS =====================
def update_windows():
    if not command_exists("winget"):
        print("❌ winget not found. Please install App Installer from Microsoft Store.")
        return

    print("🔍 Checking outdated software (Windows)...")
    run_command(["winget", "upgrade"])

    print("⬆ Updating all outdated software (Windows)...")
    run_command(["winget", "upgrade", "--all", "--silent", "--accept-source-agreements", "--accept-package-agreements"])


# ===================== LINUX =====================
def detect_linux_package_manager():
    if command_exists("apt"):
        return "apt"
    if command_exists("dnf"):
        return "dnf"
    if command_exists("pacman"):
        return "pacman"
    return None


def update_linux():
    manager = detect_linux_package_manager()

    if not manager:
        print("❌ No supported Linux package manager found.")
        return

    print(f"🔍 Detected Linux package manager: {manager}")

    if manager == "apt":
        run_command(["sudo", "apt", "update"])
        run_command(["sudo", "apt", "upgrade", "-y"])

    elif manager == "dnf":
        run_command(["sudo", "dnf", "upgrade", "--refresh", "-y"])

    elif manager == "pacman":
        run_command(["sudo", "pacman", "-Syu", "--noconfirm"])


# ===================== macOS =====================
def update_macos():
    if not command_exists("brew"):
        print("❌ Homebrew not found. Install from https://brew.sh/")
        return

    print("🔍 Checking outdated software (macOS)...")
    run_command(["brew", "outdated"])

    print("⬆ Updating all outdated software (macOS)...")
    run_command(["brew", "upgrade"])


# ===================== MAIN =====================
def main():
    os_name = platform.system()

    print(f"🖥 Detected OS: {os_name}")

    if os_name == "Windows":
        update_windows()

    elif os_name == "Linux":
        update_linux()

    elif os_name == "Darwin":
        update_macos()

    else:
        print("❌ Unsupported operating system.")


if __name__ == "__main__":
    if sys.platform != "win32":
        if os.geteuid() != 0:
            print("⚠ Please run as root / sudo")
            sys.exit(1)

    main()
