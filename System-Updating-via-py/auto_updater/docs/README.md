# **Create Exe File** 

# 1️⃣ REALITY CHECK (IMPORTANT)

| OS                        | Output               |
| ------------------------- | -------------------- |
| Windows                   | ✅ `auto_updater.exe` |
| Linux                     | ✅ single ELF binary  |
| macOS                     | ✅ Mach-O binary      |
| Cross-compile from one OS | ❌ NOT supported      |

➡ **You must build on the same OS** you target.

---

# 2️⃣ FINAL PROJECT STRUCTURE (REQUIRED)

```
auto_updater/
│
├── updater.py
├── notifier.py
├── config.py
│
├── data/                # auto-created at runtime
│
└── build_tools/
    └── build.spec       # PyInstaller spec (optional)
```

---

# 3️⃣ INSTALL BUILD TOOL

## All OSes

```bash
pip install pyinstaller
```

Verify:

```bash
pyinstaller --version
```

---

# 4️⃣ MODIFY CODE (VERY IMPORTANT)

## 🔧 Make paths binary-safe

In **updater.py**, ensure this exists (you already almost had it):

```python
import sys

def base_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

BASE_DIR = base_path()
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
```

This ensures:

* Works as `.exe`
* Works as service
* Works in `/opt`, `C:\`, `/usr/local/bin`

---

# 5️⃣ WINDOWS → SINGLE `.EXE`

## 📦 Build command (run INSIDE auto_updater folder)

```powershell
pyinstaller ^
  --onefile ^
  --noconsole ^
  --name auto_updater ^
  updater.py
```

### ✅ Output

```
dist/
└── auto_updater.exe
```

### 🔥 Run test

```powershell
dist\auto_updater.exe
```

---

# 6️⃣ LINUX → SINGLE BINARY

```bash
pyinstaller \
  --onefile \
  --name auto_updater \
  updater.py
```

### Output

```
dist/auto_updater
```

Make executable:

```bash
chmod +x dist/auto_updater
```

Test:

```bash
sudo ./dist/auto_updater
```

---

# 7️⃣ macOS → SINGLE BINARY

```bash
pyinstaller \
  --onefile \
  --name auto_updater \
  updater.py
```

### Fix macOS permission

```bash
chmod +x dist/auto_updater
```

If Gatekeeper blocks it:

```bash
xattr -d com.apple.quarantine dist/auto_updater
```

---

# 8️⃣ CONFIG & SECRETS (BEST PRACTICE)

### ❌ DO NOT embed secrets in EXE (bad)

### ✅ Use external `config.py`

Place it **next to the binary**:

```
/opt/auto_updater/
├── auto_updater        ← binary
├── config.py           ← editable
└── data/
```

Binary will auto-load it.

---

# 9️⃣ RUN AS SERVICE (BINARY VERSION)

## 🐧 Linux systemd (UPDATED)

```ini
[Service]
ExecStart=/opt/auto_updater/auto_updater
WorkingDirectory=/opt/auto_updater
User=root
```

(No Python needed anymore)

---

## 🪟 Windows Task Scheduler

```powershell
schtasks /create /sc daily /tn AutoUpdater ^
  /tr "C:\auto_updater\auto_updater.exe" ^
  /ru SYSTEM
```

---

## 🍎 macOS launchd

```xml
<array>
  <string>/opt/auto_updater/auto_updater</string>
</array>
```

---

# 🔐 SECURITY NOTES (IMPORTANT)

✔ EXE is harder to tamper
✔ Source code not exposed
✔ Still editable config
✔ JSON logs remain readable
✔ Rollback preserved

---

