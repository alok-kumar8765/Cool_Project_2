# 🚀 Python System Optimizer & Cleaner

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)
![Maintenance](https://img.shields.io/badge/Maintained-Yes-brightgreen)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-orange)
![Stars](https://img.shields.io/github/stars/alok-kumar8765/Cool_Project_2?style=social)

A **lightweight, cross-platform Python utility** to:

* 🧹 Clean temporary & cache files
* 🧠 Free unused memory
* 🌐 Flush DNS cache
* ❌ Kill unnecessary background Python processes

Designed for **developers, power users, and automation enthusiasts** who want a **simple yet effective system cleanup tool** without bloated software.

---

## 📑 Table of Contents

* [Overview](#-overview)
* [Project Structure](#-project-structure)
* [How It Works](#-how-it-works)

  * [Code 1: Background Process Killer](#code-1-background-killpy)
  * [Code 2: System Cleaner](#code-2-mainpy)
* [Features](#-features)
* [Use Cases](#-use-cases)
* [Real-World Applications](#-real-world-applications)
* [Examples](#-examples)
* [Pros & Cons](#-pros--cons)
* [Limitations](#-limitations)
* [Future Enhancements](#-future-enhancements)
* [Security Warning](#-security-warning)
* [How to Run](#-how-to-run)
* [Contributing](#-contributing)
* [Support the Project](#-support-the-project)
* [License](#-license)

---

## 🔍 Overview

This project provides **two focused Python scripts**:

1. **`background-kill.py`**
   Terminates unnecessary background Python processes that consume RAM & CPU.

2. **`main.py`**
   Performs system cleanup operations like temp deletion, cache clearing, DNS flush, and memory cleanup.

Together, they help **reduce system load and improve responsiveness**—especially on development machines.

---

## 📂 Project Structure

```text
├── background-kill.py   # Kills background Python processes
├── main.py              # Core system cleaner
└── README.md
```

---

## ⚙️ How It Works

### Code 1: `background-kill.py`

```python
import psutil

for proc in psutil.process_iter(['pid', 'name']):
    if 'python' in proc.info['name'].lower():
        try:
            proc.kill()
        except:
            pass
```

#### 🔹 Explanation

* Iterates through all running system processes
* Identifies processes containing `"python"` in their name
* Forcefully terminates them
* Ignores protected or inaccessible processes safely

#### ⚠️ Purpose

Useful when:

* Python scripts crash and remain running
* RAM usage increases due to zombie processes
* Multiple background Python services pile up

---

### Code 2: `main.py`

This is the **core system cleaner**.

#### 🔹 Key Operations

| Function                | Description                        |
| ----------------------- | ---------------------------------- |
| `clean_temp()`          | Deletes OS temporary files         |
| `clean_windows_cache()` | Clears Windows cache & prefetch    |
| `clean_linux_cache()`   | Drops filesystem cache             |
| `clean_mac_cache()`     | Clears macOS system cache          |
| `free_ram()`            | Triggers Python garbage collection |
| `flush_dns()`           | Clears DNS resolver cache          |
| `main()`                | OS detection & orchestrator        |

#### 🔹 Cross-Platform Intelligence

The script automatically detects:

* **Windows**
* **Linux**
* **macOS**

…and runs **OS-specific cleanup commands**.

---

## ✨ Features

✅ Cross-platform support
✅ No third-party bloatware
✅ Lightweight & fast
✅ Developer-friendly
✅ Safe exception handling
✅ CLI-ready automation
✅ Can be scheduled (Task Scheduler / Cron)

---

## 🧠 Use Cases

* Developers running multiple Python apps
* Low-RAM systems
* CI/CD machines
* Cloud VMs
* Student laptops
* AI/ML training cleanup
* Post-build system cleanup

---

## 🌍 Real-World Applications

* **DevOps**: Run after CI jobs to free system resources
* **AI Engineers**: Clear memory before heavy training
* **IT Admins**: Automate daily system maintenance
* **Power Users**: One-click system hygiene tool
* **Embedded Systems**: Minimal cleanup utility

---

## 📌 Examples

### Run System Cleaner

```bash
python main.py
```

### Kill Background Python Processes

```bash
python background-kill.py
```

### Linux / macOS (Admin Required)

```bash
sudo python3 main.py
```

---

## ✅ Pros & ❌ Cons

### ✅ Pros

* Simple & readable code
* No spyware, no ads
* Fully open-source
* Easy to extend
* Works without GUI

### ❌ Cons

* Cannot increase physical RAM
* Process killing is aggressive
* Requires admin access for some features
* Not a replacement for OS-level optimizers

---

## 🚫 Limitations

* Cannot overclock CPU
* Cannot modify kernel memory management
* `background-kill.py` may kill **important Python apps**
* Linux/macOS cache clearing needs `sudo`

---

## 🔮 Future Enhancements

🚀 Planned & Suggested Features:

* GUI (Tkinter / PyQT)
* One-click EXE build
* Scheduler integration
* RAM/CPU monitor
* Safe-mode process whitelist
* Logging & dry-run mode
* AI-based process analysis
* Tray-based background service

---

## 🔐 Security Warning

⚠️ **Use responsibly**

* Do NOT run `background-kill.py` on production servers
* Whitelist critical services before extending
* Always review running processes

---

## ▶️ How to Run

### Requirements

```bash
pip install psutil
```

### Python Version

```text
Python 3.8+
```

---

## 🤝 Contributing

Contributions are **highly welcome** 🎉

You can help by:

* Adding features
* Improving safety
* Writing tests
* Creating a GUI
* Improving documentation

### Steps

1. Fork the repo
2. Create a feature branch
3. Commit changes
4. Open a Pull Request 🚀

---

## ⭐ Support the Project

If this project helped you:

👉 **Give it a ⭐ on GitHub**
👉 **Share it with other developers**
👉 **Contribute new ideas**

Your support motivates continuous improvement ❤️

---

## 📜 License

This project is licensed under the **MIT License**
Free to use, modify, and distribute.

---

