import platform
import subprocess
import shutil
import sys
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox


# ===================== CORE FUNCTIONS =====================
def command_exists(cmd):
    return shutil.which(cmd) is not None


def run_command(command, log):
    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        for line in process.stdout:
            log(line.strip())
        process.wait()
    except Exception as e:
        log(f"❌ Error: {e}")


# ===================== WINDOWS =====================
def update_windows(log):
    if not command_exists("winget"):
        log("❌ winget not found. Install App Installer from Microsoft Store.")
        return

    log("🔍 Checking outdated software (Windows)...")
    run_command(["winget", "upgrade"], log)

    log("⬆ Updating all outdated software (Windows)...")
    run_command(
        ["winget", "upgrade", "--all", "--silent",
         "--accept-source-agreements", "--accept-package-agreements"],
        log
    )


# ===================== LINUX =====================
def detect_linux_package_manager():
    if command_exists("apt"):
        return "apt"
    if command_exists("dnf"):
        return "dnf"
    if command_exists("pacman"):
        return "pacman"
    return None


def update_linux(log):
    manager = detect_linux_package_manager()

    if not manager:
        log("❌ No supported Linux package manager found.")
        return

    log(f"🔍 Detected Linux package manager: {manager}")

    if manager == "apt":
        run_command(["sudo", "apt", "update"], log)
        run_command(["sudo", "apt", "upgrade", "-y"], log)

    elif manager == "dnf":
        run_command(["sudo", "dnf", "upgrade", "--refresh", "-y"], log)

    elif manager == "pacman":
        run_command(["sudo", "pacman", "-Syu", "--noconfirm"], log)


# ===================== macOS =====================
def update_macos(log):
    if not command_exists("brew"):
        log("❌ Homebrew not found. Install from https://brew.sh/")
        return

    log("🔍 Checking outdated software (macOS)...")
    run_command(["brew", "outdated"], log)

    log("⬆ Updating all outdated software (macOS)...")
    run_command(["brew", "upgrade"], log)


# ===================== MAIN LOGIC =====================
def start_update(log):
    os_name = platform.system()
    log(f"🖥 Detected OS: {os_name}")

    if os_name == "Windows":
        update_windows(log)

    elif os_name == "Linux":
        update_linux(log)

    elif os_name == "Darwin":
        update_macos(log)

    else:
        log("❌ Unsupported operating system.")

    log("✅ Update process completed.")


# ===================== GUI =====================
class AutoUpdaterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Automatic Software Updater")
        self.root.geometry("750x450")

        tk.Label(root, text="System Auto Updater",
                 font=("Arial", 16, "bold")).pack(pady=10)

        self.log_area = scrolledtext.ScrolledText(
            root, width=90, height=20, state="disabled"
        )
        self.log_area.pack(padx=10, pady=10)

        self.update_btn = tk.Button(
            root, text="Start Update", font=("Arial", 12),
            command=self.run_thread
        )
        self.update_btn.pack(pady=10)

    def log(self, message):
        self.log_area.config(state="normal")
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.yview(tk.END)
        self.log_area.config(state="disabled")
        self.root.update_idletasks()

    def run_thread(self):
        if platform.system() != "Windows":
            if hasattr(os, "geteuid") and os.geteuid() != 0:
                messagebox.showerror(
                    "Permission Error",
                    "Please run this program with sudo/root privileges."
                )
                return

        self.update_btn.config(state="disabled")
        thread = threading.Thread(
            target=lambda: start_update(self.log),
            daemon=True
        )
        thread.start()


# ===================== START =====================
if __name__ == "__main__":
    root = tk.Tk()
    app = AutoUpdaterGUI(root)
    root.mainloop()
