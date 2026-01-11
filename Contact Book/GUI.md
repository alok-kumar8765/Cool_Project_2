# 🖥 Contact Book – GUI Desktop App (Python + Tkinter + SQLite)

---

## 📦 Requirements (Already Included with Python)

* Python 3.x
* Tkinter (comes pre-installed with Python on Windows)
* SQLite (built-in)

---

## ▶ How to Run

```bat
py run.py
```

---

## 🔐 Default Login Password

```
admin123
```

---

## 🧑‍💻 FULL GUI SOURCE CODE (`run.py`)

```python
import tkinter as tk
from tkinter import messagebox
import sqlite3
import sys

DB_NAME = "contact_book.db"
PASSWORD = "admin123"

# ================= DATABASE =================
class ContactDB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            name TEXT PRIMARY KEY,
            phone TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def add(self, name, phone):
        try:
            self.cursor.execute(
                "INSERT INTO contacts VALUES (?, ?)", (name, phone)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def update(self, name, phone):
        self.cursor.execute(
            "UPDATE contacts SET phone=? WHERE name=?", (phone, name)
        )
        self.conn.commit()
        return self.cursor.rowcount

    def delete(self, name):
        self.cursor.execute("DELETE FROM contacts WHERE name=?", (name,))
        self.conn.commit()
        return self.cursor.rowcount

    def search(self, name):
        self.cursor.execute(
            "SELECT phone FROM contacts WHERE name=?", (name,)
        )
        return self.cursor.fetchone()

    def all(self):
        self.cursor.execute("SELECT * FROM contacts")
        return self.cursor.fetchall()


db = ContactDB()

# ================= GUI =================
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x420")
root.resizable(False, False)

# ---------------- LOGIN ----------------
def login():
    if password_entry.get() != PASSWORD:
        messagebox.showerror("Error", "Incorrect Password")
        sys.exit()
    login_frame.destroy()
    main_ui()

login_frame = tk.Frame(root)
login_frame.pack(pady=100)

tk.Label(login_frame, text="🔐 Login", font=("Arial", 16)).pack(pady=10)
password_entry = tk.Entry(login_frame, show="*", width=25)
password_entry.pack()
tk.Button(login_frame, text="Login", command=login).pack(pady=10)

# ---------------- MAIN UI ----------------
def main_ui():
    frame = tk.Frame(root)
    frame.pack(pady=10)

    tk.Label(frame, text="📇 Contact Book", font=("Arial", 18)).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(frame, text="Name").grid(row=1, column=0)
    tk.Label(frame, text="Phone").grid(row=2, column=0)

    name_entry = tk.Entry(frame, width=25)
    phone_entry = tk.Entry(frame, width=25)
    name_entry.grid(row=1, column=1)
    phone_entry.grid(row=2, column=1)

    result_box = tk.Text(frame, height=8, width=45)
    result_box.grid(row=7, column=0, columnspan=2, pady=10)

    def refresh():
        result_box.delete("1.0", tk.END)
        for n, p in db.all():
            result_box.insert(tk.END, f"{n} : {p}\n")

    def add_contact():
        if not db.add(name_entry.get(), phone_entry.get()):
            messagebox.showwarning("Warning", "Contact already exists")
        refresh()

    def update_contact():
        if db.update(name_entry.get(), phone_entry.get()) == 0:
            messagebox.showerror("Error", "Contact not found")
        refresh()

    def delete_contact():
        if db.delete(name_entry.get()) == 0:
            messagebox.showerror("Error", "Contact not found")
        refresh()

    def search_contact():
        result = db.search(name_entry.get())
        result_box.delete("1.0", tk.END)
        if result:
            result_box.insert(tk.END, f"{name_entry.get()} : {result[0]}")
        else:
            result_box.insert(tk.END, "Not Found")

    tk.Button(frame, text="Add", width=10, command=add_contact).grid(row=3, column=0, pady=5)
    tk.Button(frame, text="Update", width=10, command=update_contact).grid(row=3, column=1)
    tk.Button(frame, text="Delete", width=10, command=delete_contact).grid(row=4, column=0)
    tk.Button(frame, text="Search", width=10, command=search_contact).grid(row=4, column=1)
    tk.Button(frame, text="Show All", width=22, command=refresh).grid(row=5, column=0, columnspan=2, pady=5)

# ---------------- RUN ----------------
root.mainloop()
```

---

## 🎯 Features Included

* 🖥 Desktop GUI (Tkinter)
* 🔐 Password-protected login
* 🧠 SQLite database (persistent)
* ➕ Add contact
* 🔄 Update contact
* ❌ Delete contact
* 🔍 Search contact
* 📋 Show all contacts
* ⚡ Fast & lightweight

---

## 📦 Convert GUI App to EXE (Optional)

```bat
py -m PyInstaller --onefile --windowed run.py
```

Output:

```
dist/ContactBook.exe
```

Double-click → GUI opens 🎉

---

