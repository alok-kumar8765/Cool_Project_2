# 🌐 Internet Connection Checker  

[![GitHub stars](https://img.shields.io/github/stars/alok-kumar8765/Cool_Project_2?style=social)](https://github.com/alok-kumar8765/Cool_Project_2) 
[![GitHub forks](https://img.shields.io/github/forks/alok-kumar8765/Cool_Project_2?style=social)](https://github.com/alok-kumar8765/Cool_Project_2) 
[![GitHub issues](https://img.shields.io/github/issues/alok-kumar8765/Cool_Project_2)](https://github.com/alok-kumar8765/Cool_Project_2/issues) 
[![Python Version](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/downloads/)  

A lightweight Python script to **check internet connectivity** by attempting to connect to a reliable endpoint (Google). Ideal for **automation scripts, network diagnostics, and IoT applications**.  

---

## 📌 Table of Contents
<details>
<summary>Click to expand</summary>

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Code Explanation](#code-explanation)  
6. [Architecture & Flow](#architecture--flow)  
7. [Diagrams](#diagrams)  
8. [Pros & Cons](#pros--cons)  
9. [Use Cases & Real-World Examples](#use-cases--real-world-examples)  
10. [License](#license)  

</details>

---

## 📝 Project Overview
This project is a **simple yet robust Python utility** to check for internet connectivity. It attempts to connect to `https://www.google.com/` and returns the connection status.  

It is ideal for:
- **Automated scripts** requiring internet verification.  
- **IoT devices** or **embedded systems** that need network checks.  
- **Debugging network issues** in Python programs.  

---

## ⚡ Features
<details>
<summary>Click to expand</summary>

- Lightweight and **dependency-free** (uses only `requests`).  
- **Reliable** check by connecting to Google.  
- **Timeout control** to prevent hanging scripts.  
- Returns **Boolean status**: `True` if internet is available, `False` if not.  
- Simple **CLI and programmatic integration**.  

</details>

---

## 🛠 Installation
<details>
<summary>Click to expand</summary>

```bash
# Clone repo
git clone https://github.com/alok-kumar8765/Cool_Project_2.git
cd Cool_Project_2/Internet_connection_check

# Install dependencies
pip install requests
````

</details>

---

## 🚀 Usage

<details>
<summary>Click to expand</summary>

**Run directly as a script:**

```bash
python internet_connection_check.py
```

**Function usage in other scripts:**

```python
from internet_connection_check import internet_connection_test

if internet_connection_test():
    print("Internet is available.")
else:
    print("Internet is not available.")
```

**Sample Output:**

```
Attempting to connect to https://www.google.com/ to determine internet connection status.
https://www.google.com/
Connection to https://www.google.com/ was successful.
```

</details>

---

## 💡 Code Explanation

<details>
<summary>Click to expand</summary>

**Key Function:** `internet_connection_test()`

* Attempts a **GET request** to `https://www.google.com/` with a **timeout of 10 seconds**.
* **Handles exceptions**:

  * `ConnectionError` → network unreachable.
  * Generic exception → unparsed failures.
* Returns `True` if connection succeeds, `False` otherwise.
* Prints status messages for **user-friendly logging**.

**Python Libraries Used:**

* `requests` → perform HTTP requests.
* `requests.exceptions.ConnectionError` → detect failed connections.

</details>

---

## 🏗 Architecture & Flow

<details>
<summary>Click to expand</summary>

**Flow of Internet Connection Check:**

```mermaid
flowchart TD
A[Start] --> B[Call internet_connection_test()]
B --> C{Try connecting to Google?}
C -->|Success| D[Print success message]
D --> E[Return True]
C -->|ConnectionError| F[Print failed message]
F --> G[Return False]
C -->|Other Exception| H[Print unparsed failure]
H --> G
E --> I[End]
G --> I
```

**High-Level Architecture:**

```mermaid
graph LR
User[User or Script] --> Function[internet_connection_test()]
Function --> HTTP[Send GET Request to Google]
HTTP -->|200 OK| Success[Return True]
HTTP -->|ConnectionError| Failure[Return False]
HTTP -->|Other Exception| Failure
Success --> Output[Display & Return Status]
Failure --> Output
```

---

## ✅ Pros & Cons

<details>
<summary>Click to expand</summary>

**Pros:**

* Minimalistic and **lightweight**.
* Easy to integrate into **automation scripts** or **network tools**.
* **Reliable** endpoint (`Google`) ensures true connectivity check.
* Provides **clear logging** for troubleshooting.

**Cons:**

* Only checks **one endpoint** (Google) → may fail if blocked by firewall.
* Cannot diagnose **detailed network issues** (latency, bandwidth).
* Limited to **HTTP connectivity**; does not check full DNS/network stack.

</details>

---

## 🌍 Use Cases & Real-World Examples

<details>
<summary>Click to expand</summary>

**Use Cases:**

* **Automation Pipelines:** Ensure scripts run only when internet is available.
* **IoT Devices:** Devices can validate network before uploading sensor data.
* **Network Monitoring:** Periodically check connectivity in Python applications.

**Example Integration:**

```python
from internet_connection_check import internet_connection_test
import time

while True:
    if internet_connection_test():
        print("Network online. Uploading data...")
    else:
        print("Network offline. Retrying in 30 seconds...")
    time.sleep(30)
```

**SEO Keywords:** Python internet check, internet connectivity test Python, network diagnostic Python, requests connection check, Python automation tool.

</details>

---

## 🖇 License

<details>
<summary>Click to expand</summary>

MIT License – Free to use, modify, and distribute.

</details>

---

*Repo:* [https://github.com/alok-kumar8765/Cool_Project_2/tree/main/Internet_connection_check](https://github.com/alok-kumar8765/Cool_Project_2/tree/main/Internet_connection_check)


---

