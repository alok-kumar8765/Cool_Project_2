# 📄 Article to PDF Downloader using Selenium (Python)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green)
![Chrome](https://img.shields.io/badge/Chrome-PDF%20Print-yellow)
![Status](https://img.shields.io/badge/Status-Stable-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Repo](https://img.shields.io/badge/GitHub-alok--kumar8765%2FCool__Project__2-black)

---

## 🧾 Project Overview

<details>
<summary><strong>📌 Description</strong></summary>

This project is a **Python automation utility** that converts **online articles/web pages into PDF files** using **Selenium WebDriver** and **Google Chrome's built-in "Print to PDF" feature**.

It automates the browser printing process, allowing users to download articles **without manually opening print dialogs**.

</details>

---

## 📑 Table of Contents

<details>
<summary><strong>🔖 Expand Table of Contents</strong></summary>

1. Project Overview  
2. Key Features  
3. Technology Stack  
4. How It Works  
5. Architecture Diagram  
6. Data Flow Diagram (DFD)  
7. Application Flow Diagram  
8. Installation & Setup  
9. Usage  
10. Real-World Use Cases  
11. Pros & Cons  
12. Future Enhancements  
13. Author  

</details>

---

## ✨ Key Features

<details>
<summary><strong>🚀 Expand Features</strong></summary>

- ✅ Converts **any valid article URL** to PDF  
- ✅ Fully **automated Chrome printing**
- ✅ No manual clicks required
- ✅ Uses **webdriver-manager** (no driver setup headache)
- ✅ Lightweight & fast
- ✅ CLI-based interaction

</details>

---

## 🧰 Technology Stack

<details>
<summary><strong>🛠 Expand Tech Stack</strong></summary>

- **Language:** Python 3.8+
- **Automation:** Selenium WebDriver
- **Browser:** Google Chrome
- **Driver Manager:** webdriver-manager
- **Networking:** requests

</details>

---

## ⚙️ How It Works

<details>
<summary><strong>🔍 Detailed Explanation</strong></summary>

1. User provides an **article URL**
2. URL is validated using `requests`
3. Chrome is launched with **preconfigured PDF print settings**
4. Selenium opens the page
5. JavaScript triggers `window.print()`
6. Chrome saves the page as **PDF automatically**
7. Browser closes

</details>

---

## 🏗 Architecture Diagram

<details>
<summary><strong>📐 Expand Architecture</strong></summary>


```

+-------------+
|   User CLI  |
+------+------+
|
v
+------+------+
| URL Validator|
| (requests)  |
+------+------+
|
v
+------+------+
| Selenium    |
| WebDriver   |
+------+------+
|
v
+------+------+
| Chrome      |
| Print Engine|
+------+------+
|
v
+-------------+
| PDF Output  |
+-------------+

```

</details>

---

## 🔄 Data Flow Diagram (DFD)

<details>
<summary><strong>📊 Expand DFD</strong></summary>

```

User
|
v
[Enter URL]
|
v
[Validate URL]
|
v
[Load Page]
|
v
[Print to PDF]
|
v
[Save PDF]

```

</details>

---

## 🔁 Application Flow Diagram

<details>
<summary><strong>🧭 Expand Flow Diagram</strong></summary>

```

START
|
v
Input URL
|
v
Is URL Valid?
|       |
| NO    | YES
|       v
|   Launch Chrome
|       |
|   Load Web Page
|       |
|   Execute Print
|       |
|   Save as PDF
|       |
|      END
|
Display Error

````

</details>

---

## 🧩 Installation & Setup

<details>
<summary><strong>📦 Expand Setup Instructions</strong></summary>

### 1️⃣ Clone Repository
```bash
git clone https://github.com/alok-kumar8765/Cool_Project_2.git
cd Cool_Project_2
````

### 2️⃣ Install Dependencies

```bash
pip install selenium webdriver-manager requests
```

### 3️⃣ Ensure Installed

* Google Chrome (Latest)

</details>

---

## ▶️ Usage

<details>
<summary><strong>💻 Expand Usage</strong></summary>

```bash
python article_to_pdf.py
```

Enter:

```text
provide article URL: https://www.geeksforgeeks.org/what-can-i-do-with-python/
```

📄 **PDF will be saved automatically**

</details>

---

## 🌍 Real-World Use Cases

<details>
<summary><strong>🌐 Expand Use Cases</strong></summary>

* 📚 **Students** saving tutorials/articles
* 📰 **Journalists** archiving web content
* 🧠 **Researchers** collecting references
* 🏢 **Companies** storing documentation
* 🔐 **Offline reading & backups**

**Example:**
A student downloads all Python tutorials from GeeksforGeeks as PDFs for offline study.

</details>

---

## ⚖️ Pros & Cons

<details>
<summary><strong>✅ Pros</strong></summary>

* Fully automated
* No manual browser interaction
* Clean and simple
* Chrome-native PDF rendering

</details>

<details>
<summary><strong>❌ Cons</strong></summary>

* Requires Chrome browser
* Not headless by default
* Limited customization of PDF layout
* Depends on website print support

</details>

---

## 🔮 Future Enhancements

<details>
<summary><strong>🚧 Expand Roadmap</strong></summary>

* 🔹 Headless Chrome support
* 🔹 Batch URL downloads
* 🔹 Custom file naming
* 🔹 GUI/Web interface
* 🔹 Docker support

</details>

---

## 👨‍💻 Author

<details>
<summary><strong>🙋 About Me</strong></summary>

**Alok Kumar**
🔗 GitHub: [alok-kumar8765](https://github.com/alok-kumar8765)
📂 Repository: **Cool_Project_2**

Passionate about **Python, Automation, Scalable Systems & Clean Architecture**

</details>

---

⭐ **If you find this project useful, don't forget to star the repository!**

```

---
