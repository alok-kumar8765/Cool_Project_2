import os
import shutil
import tempfile
import platform
import subprocess
import gc

def clean_temp():
    temp_dir = tempfile.gettempdir()
    print(f"[+] Cleaning TEMP: {temp_dir}")

    for root, dirs, files in os.walk(temp_dir):
        for name in files:
            try:
                os.remove(os.path.join(root, name))
            except:
                pass
        for name in dirs:
            try:
                shutil.rmtree(os.path.join(root, name), ignore_errors=True)
            except:
                pass

def clean_windows_cache():
    paths = [
        os.environ.get("TEMP"),
        os.environ.get("TMP"),
        r"C:\Windows\Temp",
        r"C:\Windows\Prefetch"
    ]

    for path in paths:
        if path and os.path.exists(path):
            print(f"[+] Cleaning: {path}")
            try:
                shutil.rmtree(path, ignore_errors=True)
                os.makedirs(path, exist_ok=True)
            except:
                pass

def clean_linux_cache():
    print("[+] Dropping Linux caches")
    subprocess.run("sync; echo 3 | sudo tee /proc/sys/vm/drop_caches", shell=True)

def clean_mac_cache():
    print("[+] Cleaning macOS caches")
    subprocess.run("sudo purge", shell=True)

def free_ram():
    print("[+] Forcing garbage collection")
    gc.collect()

def flush_dns():
    system = platform.system()
    print("[+] Flushing DNS cache")

    try:
        if system == "Windows":
            subprocess.run("ipconfig /flushdns", shell=True)
        elif system == "Linux":
            subprocess.run("sudo systemctl restart systemd-resolved", shell=True)
        elif system == "Darwin":
            subprocess.run("sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder", shell=True)
    except:
        pass

def main():
    print("=== SYSTEM CLEANUP STARTED ===")

    clean_temp()
    free_ram()
    flush_dns()

    system = platform.system()
    if system == "Windows":
        clean_windows_cache()
    elif system == "Linux":
        clean_linux_cache()
    elif system == "Darwin":
        clean_mac_cache()

    print("=== CLEANUP COMPLETE ===")

if __name__ == "__main__":
    main()
