

# 📩 WhatsApp Message Automation using Python

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![Repo Size](https://img.shields.io/github/repo-size/alok-kumar8765/Cool_Project_2)
![Stars](https://img.shields.io/github/stars/alok-kumar8765/Cool_Project_2?style=social)
![Forks](https://img.shields.io/github/forks/alok-kumar8765/Cool_Project_2?style=social)
![Issues](https://img.shields.io/github/issues/alok-kumar8765/Cool_Project_2)
![License](https://img.shields.io/github/license/alok-kumar8765/Cool_Project_2)

---

## 📌 Project Overview

<details>
<summary><b>Click to expand</b></summary>

This project demonstrates **automated WhatsApp message scheduling** using **Python** and the `pywhatkit` library.  
It allows users to send WhatsApp messages **at a specified time** without manual intervention.

✔ Beginner-friendly  
✔ Practical automation use case  
✔ Minimal dependencies  

</details>

---

## 📚 Table of Contents

<details>
<summary><b>Click to expand</b></summary>

- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [How It Works](#-how-it-works)
- [Code Explanation](#-code-explanation)
- [Architecture Diagram](#-architecture-diagram)
- [DFD (Data Flow Diagram)](#-dfd-data-flow-diagram)
- [Flow Diagram](#-flow-diagram)
- [Use Cases](#-use-cases)
- [Real World Applications](#-real-world-applications)
- [Pros & Cons](#-pros--cons)
- [Example Execution](#-example-execution)
- [Installation & Setup](#-installation--setup)
- [Future Improvements](#-future-improvements)
- [License](#-license)

</details>

---

## ✨ Features

<details>
<summary><b>Click to expand</b></summary>

- 📅 Schedule WhatsApp messages
- 📱 Works with any valid WhatsApp number
- ⏱ Sends message at exact hour & minute
- 🔒 Uses WhatsApp Web (no API key required)
- 🧩 Simple and readable Python code

</details>

---

## 🛠 Technology Stack

<details>
<summary><b>Click to expand</b></summary>

- **Language:** Python 3.8+
- **Library:** pywhatkit
- **Platform:** WhatsApp Web
- **OS Support:** Windows / Linux / macOS

</details>

---

## ⚙ How It Works

<details>
<summary><b>Click to expand</b></summary>

1. User enters:
   - Receiver's mobile number
   - Message text
   - Hour & minute
2. Script launches WhatsApp Web
3. Message is sent automatically at scheduled time

</details>

---

## 🧠 Code Explanation

<details>
<summary><b>Click to expand</b></summary>

### 🔹 Python Script

```python
import pywhatkit
from datetime import datetime

now = datetime.now()

chour = now.strftime("%H")
mobile = input('Enter Mobile No of Receiver : ')
message = input('Enter Message you wanna send : ')
hour = int(input('Enter hour : '))
minute = int(input('Enter minute : '))

pywhatkit.sendwhatmsg(mobile, message, hour, minute)
```

## 🔍 Explanation

Line	Description

import pywhatkit	Imports WhatsApp automation library
datetime.now()	Fetches current system time
input()	Takes user inputs
sendwhatmsg()	Schedules WhatsApp message


</details>
---

## 🏗 Architecture Diagram

<details>
<summary><b>Click to expand</b></summary>
   graph TD
    User -->|Input Details| PythonScript
    PythonScript -->|Schedule| WhatsAppWeb
    WhatsAppWeb -->|Send Message| Receiver

</details>
---

## 🔄 DFD (Data Flow Diagram)

<details>
<summary><b>Click to expand</b></summary>
   graph LR
    U[User] --> D[Python Program]
    D --> W[WhatsApp Web]
    W --> R[Receiver]

</details>
---

## 🔁 Flow Diagram

<details>
<summary><b>Click to expand</b></summary>

   flowchart TD
    Start --> Input
    Input --> ValidateTime
    ValidateTime --> OpenWhatsApp
    OpenWhatsApp --> SendMessage
    SendMessage --> End

</details>
---

## 🎯 Use Cases

<details>
<summary><b>Click to expand</b></summary>Automated reminders

Birthday / Anniversary wishes

Business follow-ups

Scheduled notifications

Personal productivity automation


</details>
---

## 🌍 Real World Applications

<details>
<summary><b>Click to expand</b></summary>🏢 Small businesses sending reminders

🧑‍🏫 Teachers sending class notifications

🏥 Appointment reminders

📢 Marketing follow-up automation

🤖 Learning automation scripting


</details>
---

## ⚖ Pros & Cons

<details>
<summary><b>Click to expand</b></summary>✅ Pros

- Easy to use

- No paid API required

- Beginner friendly

- Works on WhatsApp Web


## ❌ Cons

- Requires internet

- Browser must remain open

- Not suitable for bulk spam (policy violation)


</details>
---

## ▶ Example Execution

<details>
<summary><b>Click to expand</b></summary>Enter Mobile No of Receiver : +919876543210
Enter Message you wanna send : Hello from Python!
Enter hour : 14
Enter minute : 30

➡ Message sent automatically at 14:30

</details>
---

## 🚀 Installation & Setup

<details>
<summary><b>Click to expand</b></summary>Step 1: Install Python Library

pip install pywhatkit

Step 2: Run Script

python main.py

Step 3:

Ensure WhatsApp Web is logged in

Keep browser open until message is sent


</details>
---

## 🔮 Future Improvements

<details>
<summary><b>Click to expand</b></summary>Bulk message scheduling

- GUI using Tkinter

- Message templates

- Database logging

- Retry & error handling

- WhatsApp Business integration


</details>
---

## 📜 License

<details>
<summary><b>Click to expand</b></summary>This project is licensed under the MIT License.
Feel free to use, modify, and distribute responsibly.

</details>
---

