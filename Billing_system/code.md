
# 🧾 Refactored Billing System (Tkinter + SQLite)

## 📁 Final Folder Structure (IMPORTANT)

```
Billing_System/
│
├── main.py               # Tkinter UI
├── controller.py         # UI ↔ Logic bridge
├── billing_logic.py      # Price & tax calculations
├── database.py           # SQLite DB operations
├── config.py             # Configurations
├── schema.sql            # DB schema
└── billing.db            # Auto-created
```

---

## 1️⃣ `config.py`

```python
DB_NAME = "billing.db"
MEDICAL_TAX = 0.05
COLD_DRINK_TAX = 0.10
```

---

## 2️⃣ `schema.sql`

```sql
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS bills (
    bill_no INTEGER PRIMARY KEY,
    customer_id INTEGER,
    total REAL,
    medical_tax REAL,
    grocery_tax REAL,
    cold_drink_tax REAL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS bill_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bill_no INTEGER,
    category TEXT,
    product TEXT,
    quantity INTEGER,
    price REAL
);
```

---

## 3️⃣ `database.py`

```python
import sqlite3
from config import DB_NAME

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    with open("schema.sql") as f:
        conn.executescript(f.read())
    conn.close()

def save_customer(name, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO customers(name, phone) VALUES (?,?)", (name, phone))
    conn.commit()
    cid = cur.lastrowid
    conn.close()
    return cid

def save_bill(bill_no, customer_id, total, m_tax, g_tax, c_tax):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO bills VALUES (?,?,?,?,?,?,datetime('now'))",
        (bill_no, customer_id, total, m_tax, g_tax, c_tax)
    )
    conn.commit()
    conn.close()

def save_items(bill_no, items):
    conn = get_connection()
    cur = conn.cursor()
    for item in items:
        cur.execute(
            "INSERT INTO bill_items(bill_no, category, product, quantity, price) VALUES (?,?,?,?,?)",
            item
        )
    conn.commit()
    conn.close()

def get_bill(bill_no):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM bills WHERE bill_no=?", (bill_no,))
    bill = cur.fetchone()

    cur.execute("SELECT category, product, quantity, price FROM bill_items WHERE bill_no=?", (bill_no,))
    items = cur.fetchall()
    conn.close()
    return bill, items
```

---

## 4️⃣ `billing_logic.py`

```python
PRICES = {
    "medical": {
        "Sanitizer": 2, "Mask": 5, "Hand Gloves": 12,
        "Dettol": 30, "Newsprin": 5, "Thermal Gun": 15
    },
    "grocery": {
        "Rice": 10, "Food Oil": 10, "Wheat": 10,
        "Daal": 6, "Flour": 8, "Maggi": 5
    },
    "cold": {
        "Sprite": 10, "Limka": 10, "Mazza": 10,
        "Coke": 10, "Fanta": 10, "Mountain Duo": 10
    }
}

def calculate_items(data):
    items = []
    subtotal = {"medical": 0, "grocery": 0, "cold": 0}

    for category, products in data.items():
        for name, qty in products.items():
            if qty > 0:
                price = PRICES[category][name] * qty
                subtotal[category] += price
                items.append((None, category, name, qty, price))

    return items, subtotal
```

---

## 5️⃣ `controller.py`

```python
import random
from billing_logic import calculate_items
from database import save_customer, save_bill, save_items

def generate_bill(customer, phone, product_data):
    bill_no = random.randint(1000, 9999)

    items, subtotal = calculate_items(product_data)

    medical_tax = round(subtotal["medical"] * 0.05, 2)
    grocery_tax = round(subtotal["grocery"] * 0.05, 2)
    cold_tax = round(subtotal["cold"] * 0.10, 2)

    total = subtotal["medical"] + subtotal["grocery"] + subtotal["cold"] \
            + medical_tax + grocery_tax + cold_tax

    customer_id = save_customer(customer, phone)
    save_bill(bill_no, customer_id, total, medical_tax, grocery_tax, cold_tax)

    final_items = [(bill_no, *i[1:]) for i in items]
    save_items(bill_no, final_items)

    return bill_no, items, total
```

---

## 6️⃣ `main.py` (Tkinter UI – CLEAN & SHORT)

```python
from tkinter import *
from tkinter import messagebox
from controller import generate_bill
from database import init_db

init_db()

root = Tk()
root.title("Billing System")
root.geometry("600x400")

customer = StringVar()
phone = StringVar()
qty = {k: IntVar() for k in ["Sanitizer","Mask","Rice","Coke"]}

Label(root, text="Customer Name").grid(row=0, column=0)
Entry(root, textvariable=customer).grid(row=0, column=1)

Label(root, text="Phone").grid(row=1, column=0)
Entry(root, textvariable=phone).grid(row=1, column=1)

row = 2
for p in qty:
    Label(root, text=p).grid(row=row, column=0)
    Entry(root, textvariable=qty[p]).grid(row=row, column=1)
    row += 1

def bill():
    if not customer.get() or not phone.get():
        messagebox.showerror("Error", "Customer details required")
        return

    data = {
        "medical": {"Sanitizer": qty["Sanitizer"].get(), "Mask": qty["Mask"].get()},
        "grocery": {"Rice": qty["Rice"].get()},
        "cold": {"Coke": qty["Coke"].get()}
    }

    bill_no, _, total = generate_bill(customer.get(), phone.get(), data)
    messagebox.showinfo("Success", f"Bill {bill_no} Generated\nTotal: Rs.{total}")

Button(root, text="Generate Bill", command=bill).grid(row=row, column=0, columnspan=2)

root.mainloop()
```

---

## 🔥 What You Have Now (Compared to Before)

| Feature         | Old Code   | Refactored |
| --------------- | ---------- | ---------- |
| Architecture    | Monolithic | MVC-style  |
| Storage         | Text files | SQLite DB  |
| Maintainability | Hard       | Easy       |
| Scalability     | ❌          | ✅          |
| Professional    | ❌          | ✅          |

---

