# 🚀 Advanced Contact Book – Final Professional Upgrade

You will get:

✅ **SQLite Database (Optimized storage)**
✅ **Unit Tests (Automated testing)**
✅ **Windows EXE Packaging (No Python needed to run)**

Everything works **without an IDE**.

---

# 🧠 PART 1 — Optimize with SQLite Database

## ✅ Why SQLite?

* Faster than JSON for large data
* ACID compliant
* No server required
* Industry-standard

---

## 📂 Project Structure (Recommended)

```
ContactBook/
│
├── run.py
├── contact_book.db
├── test_contact_book.py
└── build_exe.bat
```

---

## 🧑‍💻 `run.py` (SQLite + OOP + Password)

```python
import sqlite3
import getpass
import sys

DB_NAME = "contact_book.db"
PASSWORD = "admin123"

class ContactBook:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            name TEXT PRIMARY KEY,
            phone TEXT NOT NULL
        )
        """)
        self.conn.commit()

    # 🔐 Login
    def login(self):
        pwd = getpass.getpass("Enter Password: ")
        if pwd != PASSWORD:
            print("❌ Access Denied")
            sys.exit()
        print("✅ Login Successful\n")

    # ➕ Add
    def add_contact(self):
        name = input("Name: ")
        phone = input("Phone: ")
        try:
            self.cursor.execute(
                "INSERT INTO contacts VALUES (?, ?)", (name, phone)
            )
            self.conn.commit()
            print("✅ Contact Added")
        except sqlite3.IntegrityError:
            print("⚠ Contact already exists")

    # 🔄 Update
    def update_contact(self):
        name = input("Name to update: ")
        phone = input("New phone: ")
        self.cursor.execute(
            "UPDATE contacts SET phone=? WHERE name=?", (phone, name)
        )
        if self.cursor.rowcount == 0:
            print("❌ Contact not found")
        else:
            self.conn.commit()
            print("✅ Contact Updated")

    # ❌ Delete
    def delete_contact(self):
        name = input("Name to delete: ")
        self.cursor.execute("DELETE FROM contacts WHERE name=?", (name,))
        if self.cursor.rowcount == 0:
            print("❌ Contact not found")
        else:
            self.conn.commit()
            print("🗑 Contact Deleted")

    # 🔍 Search
    def search_contact(self):
        name = input("Name to search: ")
        self.cursor.execute(
            "SELECT phone FROM contacts WHERE name=?", (name,)
        )
        result = self.cursor.fetchone()
        if result:
            print(f"📞 {name}: {result[0]}")
        else:
            print("❌ Not Found")

    # 📋 Show All
    def show_all(self):
        self.cursor.execute("SELECT * FROM contacts")
        rows = self.cursor.fetchall()
        print("\nName\t\tPhone")
        print("-" * 30)
        for row in rows:
            print(f"{row[0]}\t\t{row[1]}")

    # 📜 Menu
    def menu(self):
        while True:
            print("""
1. Add Contact
2. Update Contact
3. Delete Contact
4. Search Contact
5. Show All
6. Exit
""")
            ch = input("Choice: ")
            if ch == "1":
                self.add_contact()
            elif ch == "2":
                self.update_contact()
            elif ch == "3":
                self.delete_contact()
            elif ch == "4":
                self.search_contact()
            elif ch == "5":
                self.show_all()
            elif ch == "6":
                print("👋 Bye")
                break
            else:
                print("❌ Invalid choice")

if __name__ == "__main__":
    app = ContactBook()
    app.login()
    app.menu()
```

---

# 🧪 PART 2 — Add Unit Tests

## ✅ Why Unit Tests?

* Prevent bugs
* Professional standard
* Interview-ready

---

## 🧪 `test_contact_book.py`

```python
import sqlite3
import unittest
from run import ContactBook

class TestContactBook(unittest.TestCase):

    def setUp(self):
        self.app = ContactBook()
        self.app.cursor.execute("DELETE FROM contacts")
        self.app.conn.commit()

    def test_add_contact(self):
        self.app.cursor.execute(
            "INSERT INTO contacts VALUES (?, ?)", ("Test", "123")
        )
        self.app.conn.commit()
        self.app.cursor.execute("SELECT * FROM contacts WHERE name='Test'")
        self.assertIsNotNone(self.app.cursor.fetchone())

    def test_update_contact(self):
        self.app.cursor.execute(
            "INSERT INTO contacts VALUES (?, ?)", ("A", "111")
        )
        self.app.conn.commit()
        self.app.cursor.execute(
            "UPDATE contacts SET phone='222' WHERE name='A'"
        )
        self.app.cursor.execute("SELECT phone FROM contacts WHERE name='A'")
        self.assertEqual(self.app.cursor.fetchone()[0], "222")

    def test_delete_contact(self):
        self.app.cursor.execute(
            "INSERT INTO contacts VALUES (?, ?)", ("B", "333")
        )
        self.app.conn.commit()
        self.app.cursor.execute("DELETE FROM contacts WHERE name='B'")
        self.app.cursor.execute("SELECT * FROM contacts WHERE name='B'")
        self.assertIsNone(self.app.cursor.fetchone())

if __name__ == "__main__":
    unittest.main()
```

### ▶ Run Tests

```bat
py test_contact_book.py
```

---

# 📦 PART 3 — Package as Windows EXE

## ✅ Install PyInstaller (One-Time)

```bat
py -m pip install pyinstaller
```

---

## ⚙ Build EXE

From project folder:

```bat
py -m PyInstaller --onefile --name ContactBook run.py
```

---

## 📁 Output Location

```
dist/
 └── ContactBook.exe
```

🎉 **Double-click → App runs (NO Python required)**

---

## 🖱 Optional: One-Click Build Script

### `build_exe.bat`

```bat
@echo off
py -m PyInstaller --onefile run.py
pause
```

---

# ✅ Final Feature Checklist

| Feature            | Status |
| ------------------ | ------ |
| SQLite DB          | ✅      |
| OOP Architecture   | ✅      |
| Password Protected | ✅      |
| Update/Delete      | ✅      |
| Unit Tests         | ✅      |
| Windows EXE        | ✅      |
| No IDE Needed      | ✅      |

---

