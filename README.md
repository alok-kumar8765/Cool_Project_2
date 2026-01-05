
# 🚀 Cool Project 2 – Python Mini Projects Collection

![Stars](https://img.shields.io/github/stars/alok-kumar8765/Cool_Project_2?style=social)
![Forks](https://img.shields.io/github/forks/alok-kumar8765/Cool_Project_2?style=social)
![Issues](https://img.shields.io/github/issues/alok-kumar8765/Cool_Project_2)
![Pull Requests](https://img.shields.io/github/issues-pr/alok-kumar8765/Cool_Project_2)
![License](https://img.shields.io/github/license/alok-kumar8765/Cool_Project_2)
![Language](https://img.shields.io/github/languages/top/alok-kumar8765/Cool_Project_2)
![Contributors](https://img.shields.io/github/contributors/alok-kumar8765/Cool_Project_2)
![Last Commit](https://img.shields.io/github/last-commit/alok-kumar8765/Cool_Project_2)

---

## 📌 About This Repository

**Cool Project 2** is a **collection of beginner-to-intermediate Python mini projects** covering:

* 🤖 Chatbots
* 🖥 GUI applications
* 🎮 Simulations
* 🔐 Security & hashing
* ⛓ Blockchain basics
* 🌐 Web scraping
* 🖼 Image processing

Each project is **independent**, easy to run, and designed to help **students, beginners, and non-coders** understand real-world Python use cases.

---

## 📑 Table of Contents

* [Projects Overview](#-projects-overview)
* [Installation & Setup](#-installation--setup)
* [How to Run Projects](#-how-to-run-projects)
* [Project Details](#-project-details)
* [Use Cases](#-use-cases)
* [Pros & Cons](#-pros--cons)
* [Known Bugs & Fixes](#-known-bugs--fixes)
* [Contribution Guide](#-contribution-guide)
* [Support & Motivation](#-support--motivation)

---

## 📦 Installation & Setup

<details>
<summary><b>Click to expand</b></summary>

### 1️⃣ Install Python

* Download Python **3.8+** from
  👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)
* During installation, ✅ check **“Add Python to PATH”**

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/alok-kumar8765/Cool_Project_2.git
cd Cool_Project_2
```

### 3️⃣ Install Required Libraries

```bash
pip install pygame opencv-python numpy requests beautifulsoup4 captcha wechaty
```

> ⚠ Some projects use **Tkinter** (comes preinstalled with Python)
> ⚠ Alarm app uses **winsound (Windows only)**

</details>

---

## ▶ How to Run Projects

<details>
<summary><b>General Run Command</b></summary>

```bash
python filename.py
```

Example:

```bash
python alarm_clock.py
```

Each file runs **independently**.

</details>

---
## Project Structure Diagram (Visual)

```markdown

Cool_Project_2
│
├─ README.md
├─ requirements.txt
├─ assets
│   ├─ sample_image.png
│   └─ sound.wav
├─ bills
└─ projects
    ├─ ding_dong_wechat_bot
    │   └─ ding_dong_bot.py
    ├─ captcha_verification
    │   └─ captcha_app.py
    ├─ year_calendar
    │   └─ year_calendar.py
    ├─ age_calculator
    │   └─ age_calculator.py
    ├─ ball_bounce_simulation
    │   └─ ball_bounce.py
    ├─ blockchain_mining
    │   └─ blockchain.py
    ├─ billing_software
    │   └─ billing_app.py
    ├─ alarm_clock
    │   └─ alarm_clock.py
    ├─ website_link_scraper
    │   └─ link_scraper.py
    └─ image_to_ascii
        └─ ascii_converter.py
```

---

## 🧩 Project Details

<details>
<summary><b>1️⃣ Ding-Dong WeChat Bot (OOP)</b></summary>

* Built using **Wechaty**
* Responds to messages like `ding → dong`
* Handles images, files, groups, and friends

**Use Case:**
Chat automation, customer support bots

</details>

<details>
<summary><b>2️⃣ CAPTCHA Verification System</b></summary>

* Generates image CAPTCHA
* Verifies user input
* Tkinter-based GUI

**Use Case:**
Login security, form validation

</details>

<details>
<summary><b>3️⃣ Year Calendar GUI</b></summary>

* Displays full calendar of a year
* Simple Tkinter interface

**Use Case:**
Date utilities, desktop widgets

</details>

<details>
<summary><b>4️⃣ Age Calculator (Years / Months / Days)</b></summary>

* Calculates exact age
* Handles leap years

**Use Case:**
Education, personal utilities

</details>

<details>
<summary><b>5️⃣ Ball Bounce Physics Simulation</b></summary>

* Built with **Pygame**
* Gravity + wall collision

**Use Case:**
Physics learning, game development basics

</details>

<details>
<summary><b>6️⃣ Blockchain Mining Simulation</b></summary>

* SHA-256 hashing
* Proof-of-Work concept

**Use Case:**
Blockchain fundamentals, cryptography learning

</details>

<details>
<summary><b>7️⃣ Billing Software (Complete GUI App)</b></summary>

* Medical, Grocery & Cold Drinks billing
* Auto tax calculation
* Bill save & search

**Use Case:**
Retail shops, billing systems

</details>

<details>
<summary><b>8️⃣ Alarm Clock Application</b></summary>

* Multi-threaded alarm
* Sound notification

**Use Case:**
Desktop utilities, threading concepts

</details>

<details>
<summary><b>9️⃣ Website Link Scraper</b></summary>

* Extracts all `<a>` links
* Saves output to file

**Use Case:**
SEO analysis, web crawling basics

</details>

<details>
<summary><b>🔟 Image to ASCII Art Converter</b></summary>

* Uses OpenCV & NumPy
* Converts image → ASCII text

**Use Case:**
Creative coding, image processing

</details>

---

## 💡 Use Cases

* 🎓 Student learning projects
* 🧠 Python practice & revision
* 🏗 Mini-project portfolio
* 🖥 Desktop applications
* 🤖 Automation & bots

---

## ✅ Pros & ❌ Cons

### ✅ Pros

* Beginner friendly
* Real-world examples
* Independent projects
* Covers multiple domains

### ❌ Cons

* Minimal error handling in some scripts
* GUI designs are basic
* Some apps are OS-specific

---

## 🐞 Known Bugs & Fixes

<details>
<summary><b>Common Issues & Solutions</b></summary>

* ❌ **Tkinter not opening**

  * ✅ Ensure Python is installed correctly

* ❌ **Captcha font error**

  * ✅ Update font paths in code

* ❌ **Alarm sound not playing**

  * ✅ Use Windows OS or replace `winsound`

* ❌ **Billing app bill save error**

  * ✅ Create a `bills/` folder before running

```bash
mkdir bills
```

</details>

---

## 🤝 Contribution Guide

We ❤️ contributions!

* Fork the repo
* Create a new branch
* Add improvements / new mini projects
* Submit a Pull Request

**Ideas to contribute:**

* Improve UI
* Add comments
* Convert scripts to packages
* Add error handling

---

## ⭐ Support & Motivation

If you found this repository useful:

👉 **Please give it a ⭐ Star**
👉 **Fork it** and build your own projects
👉 **Share it** with friends & learners

Your support keeps this project growing 🚀

---

### 👨‍💻 Author

**Alok Kumar**
GitHub: [alok-kumar8765](https://github.com/alok-kumar8765)

---
