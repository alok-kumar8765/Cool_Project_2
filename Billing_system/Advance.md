# 🧾 Advanced Billing System (Python Tkinter + Database)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-blueviolet)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange)
![Status](https://img.shields.io/badge/Project-Production--Ready-success)
![Author](https://img.shields.io/badge/Author-Alok%20Kumar-informational)

> **SEO Description (GitHub Optimized):**  
> A professional **Python Tkinter Billing System** with **medical, grocery, and cold drink billing**, featuring **real-time tax calculation**, **bill storage**, **search functionality**, and a **fully refactored architecture** supporting **SQLite & MySQL databases**. Ideal for **retail shops, medical stores, learning projects, and desktop POS systems**.

---

<details>
<summary><h2>📑 Table of Contents</h2></summary>

1. 🔍 SEO-Boosted Project Overview  
2. 🎯 Features  
3. 🏗️ System Architecture  
4. 🔁 Application Flow  
5. 📊 Data Flow Diagram (DFD)  
6. 🧠 Refactoring Strategy (Step-by-Step)  
7. 📁 Refactored Folder Structure  
8. 🧾 Database Design (SQLite + MySQL)  
9. 💾 Database Code (Complete)  
10. 🔌 Tkinter ↔ Database Integration  
11. ⚙️ Installation & Setup  
12. 🌍 Real-World Use Cases  
13. ✅ Pros & ❌ Cons  
14. 🚀 Future Enhancements  
15. 🛠️ Tech Stack  
16. 📜 License  

</details>

---

<details>
<summary><h2>🔍 SEO-Boosted Project Overview</h2></summary>

This **Advanced Billing System** is a **desktop-based POS (Point of Sale) application** developed using **Python Tkinter** with **database-backed persistence**.

### 🔑 SEO Keywords Integrated
- Python Billing System  
- Tkinter POS Application  
- Retail Billing Software  
- Medical Store Billing App  
- Grocery Billing System  
- SQLite Billing Software  
- MySQL Desktop Application  

Designed for:
- 🏥 Medical Shops  
- 🛒 Grocery Stores  
- 🧾 Retail Counters  
- 🧑‍💻 Python Learning Projects  

</details>

---

<details>
<summary><h2>🎯 Features</h2></summary>

- 🧾 Category-wise Billing (Medical, Grocery, Cold Drinks)
- 🧮 Automatic Tax Calculation
- 💾 Database-Driven Bill Storage
- 🔍 Search Bills by Bill Number
- 🧑 Customer Management
- 📊 Persistent Sales Records
- 🧠 Clean, Refactored Architecture
- 🔌 SQLite (default) & MySQL (optional)

</details>

---

<details>
<summary><h2>🏗️ System Architecture</h2></summary>

```mermaid
graph TD
    UI[Tkinter GUI] --> Controller
    Controller --> BillingLogic
    BillingLogic --> Database
    Database --> Reports
````

**Architecture Pattern:**
🧱 MVC-Inspired Desktop Architecture

</details>

---

<details>
<summary><h2>🔁 Application Flow</h2></summary>

```mermaid
flowchart TD
    Start --> CustomerDetails
    CustomerDetails --> ItemSelection
    ItemSelection --> PriceTaxCalc
    PriceTaxCalc --> BillGeneration
    BillGeneration --> DatabaseSave
    DatabaseSave --> End
```

</details>

---

<details>
<summary><h2>📊 Data Flow Diagram (DFD)</h2></summary>

```mermaid
graph LR
    User --> BillingApp
    BillingApp --> Database
    Database --> BillingApp
    BillingApp --> BillOutput
```

</details>

---

<details>
<summary><h2>🧠 Code Refactoring Strategy (IMPORTANT)</h2></summary>

### ❌ Problems in Original Code

* UI + Logic tightly coupled
* No database (text files only)
* Difficult to scale
* No separation of concerns

### ✅ Refactoring Goals

* Modular design
* Database persistence
* Cleaner logic
* Easy future upgrades

---

### 🔧 Refactoring Steps

**Step 1: Separate Logic**

```python
# billing_logic.py
def calculate_medical(items):
    return sum(items.values())
```

**Step 2: Separate Database Layer**

```python
# database.py
def save_bill(data):
    pass
```

**Step 3: UI Calls Controller Only**

```python
# main.py
from controller import generate_bill
```

</details>

---

<details>
<summary><h2>📁 Refactored Folder Structure</h2></summary>

```
Billing_System/
│
├── main.py                # Tkinter UI
├── controller.py          # UI ↔ Logic bridge
├── billing_logic.py       # Price & tax calculations
├── database.py            # SQLite/MySQL handling
├── models.py              # Data models
├── config.py              # DB configuration
├── schema.sql             # Database schema
└── README.md
```

</details>

---

<details>
<summary><h2>🧾 Database Design (SQLite + MySQL)</h2></summary>

### 📌 Tables

```sql
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT
);

CREATE TABLE bills (
    bill_no INTEGER PRIMARY KEY,
    customer_id INTEGER,
    total REAL,
    tax REAL,
    date TEXT
);

CREATE TABLE bill_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_no INTEGER,
    product TEXT,
    quantity INTEGER,
    price REAL
);
```

✔ Works in **SQLite**
✔ Works in **MySQL** (minor syntax change)

</details>

---

<details>
<summary><h2>💾 Database Code (Complete)</h2></summary>

### SQLite Connection

```python
import sqlite3

conn = sqlite3.connect("billing.db")
cursor = conn.cursor()
```

### Save Bill

```python
def save_bill(bill_no, customer, items, total, tax):
    cursor.execute("INSERT INTO bills VALUES (?,?,?,?,date('now'))",
                   (bill_no, customer, total, tax))
    conn.commit()
```

### Search Bill

```python
def get_bill(bill_no):
    cursor.execute("SELECT * FROM bills WHERE bill_no=?", (bill_no,))
    return cursor.fetchone()
```

### MySQL (Optional)

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="billing"
)
```

</details>

---

<details>
<summary><h2>🔌 Tkinter ↔ Database Integration</h2></summary>

```python
def generate_bill():
    total, tax = calculate_total()
    save_bill(bill_no, customer, items, total, tax)
```

✔ UI never talks directly to DB
✔ Clean separation achieved

</details>

---

<details>
<summary><h2>⚙️ Installation & Setup</h2></summary>

```bash
git clone https://github.com/alok-kumar8765/Cool_Project_2.git
cd Billing_system
python main.py
```

For MySQL:

```bash
pip install mysql-connector-python
```

</details>

---

<details>
<summary><h2>🌍 Real-World Use Cases</h2></summary>

* 🏥 Medical Billing Counter
* 🛒 Grocery POS System
* 🧾 Retail Invoice Generator
* 🧑‍🎓 Python GUI + DB Learning Project

</details>

---

<details>
<summary><h2>✅ Pros & ❌ Cons</h2></summary>

### ✅ Pros

* Clean architecture
* Database persistence
* Scalable
* Easy to maintain

### ❌ Cons

* Desktop only
* Single-user system

</details>

---

<details>
<summary><h2>🚀 Future Enhancements</h2></summary>

* 🔐 Login System
* 📊 Sales Analytics
* 🖨️ Print Bills
* 🌐 Web Version (Django)

</details>

---

<details>
<summary><h2>🛠️ Tech Stack</h2></summary>

* Python
* Tkinter
* SQLite / MySQL
* MVC-Inspired Design

</details>

---

<details>
<summary><h2>📜 License</h2></summary>

MIT License © Alok Kumar

</details>

---

