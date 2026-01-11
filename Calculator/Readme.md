# 🧮 Python GUI Calculator (Tkinter)

<p align="center">
  <img src="https://img.shields.io/github/repo-size/alok-kumar8765/Cool_Project_2?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/alok-kumar8765/Cool_Project_2?style=for-the-badge" />
  <img src="https://img.shields.io/github/forks/alok-kumar8765/Cool_Project_2?style=for-the-badge" />
  <img src="https://img.shields.io/github/last-commit/alok-kumar8765/Cool_Project_2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-Tkinter-blue?style=for-the-badge" />
</p>

---

## 📌 Project Title
**Python GUI Calculator using Tkinter**

---

<details>
<summary><h2>📖 Table of Contents</h2></summary>

- 📌 Project Overview  
- 🎯 Features  
- 🧠 Working Explanation  
- 🏗 Architecture Diagram  
- 🔁 Flow Diagram  
- 📊 Data Flow Diagram (DFD)  
- 🧩 Code Structure  
- ⚙️ Installation & Usage  
- 🌍 Real World Use Cases  
- ✅ Pros & ❌ Cons  
- 🔐 Security Considerations  
- 🚀 Future Enhancements  
- 🏷 SEO Keywords  

</details>

---

<details>
<summary><h2>📘 Project Overview</h2></summary>

This project is a **desktop-based calculator application** developed using **Python Tkinter GUI framework**.  
It supports **basic arithmetic operations** with a clean UI, button-based input, and real-time expression evaluation.

📍 **Location in Repo:**  
`Cool_Project_2/Calculator`

</details>

---

<details>
<summary><h2>🎯 Features</h2></summary>

- 🖥 GUI-based Calculator (Tkinter)
- ➕ Addition, ➖ Subtraction, ✖ Multiplication, ➗ Division
- ⌫ Clear Screen Functionality
- 🧮 Real-time Expression Evaluation
- 🎨 Custom UI Styling
- 🔢 Unicode Symbols Support
- 🧠 Object-Oriented Design

</details>

---

<details>
<summary><h2>🧠 Working Explanation</h2></summary>

- The application initializes a **Tkinter window**
- Buttons are dynamically created using a reusable method
- User input is stored as a mathematical expression
- Expression is evaluated using Python’s `eval()` function
- Output is displayed in a disabled text widget
- Clear (`⌫`) resets the calculator state

</details>

---

<details>
<summary><h2>🏗 Architecture Diagram</h2></summary>

```mermaid
graph TD
    User -->|Clicks Button| Tkinter_UI
    Tkinter_UI --> Calculator_Class
    Calculator_Class --> Expression_Handler
    Expression_Handler --> Eval_Engine
    Eval_Engine --> Display_Screen
````

</details>

---

<details>
<summary><h2>🔁 Application Flow Diagram</h2></summary>

```mermaid
flowchart TD
    Start --> Launch_GUI
    Launch_GUI --> Button_Click
    Button_Click -->|Number| Update_Expression
    Button_Click -->|Operator| Update_Expression
    Button_Click -->|Equals| Evaluate
    Evaluate --> Display_Result
    Display_Result --> Wait_For_Input
```

</details>

---

<details>
<summary><h2>📊 Data Flow Diagram (DFD)</h2></summary>

```mermaid
graph LR
    User_Input --> Expression_String
    Expression_String --> Calculator_Logic
    Calculator_Logic --> Evaluated_Result
    Evaluated_Result --> GUI_Display
```

</details>

---

<details>
<summary><h2>🧩 Code Structure</h2></summary>

```text
Calculator/
│
├── calculator.py
│   ├── love()
│   ├── Calculator Class
│   │   ├── __init__()
│   │   ├── createButton()
│   │   ├── click()
│   │   ├── clear_screen()
│   │   ├── insert_screen()
│
└── README.md
```

</details>

---

<details>
<summary><h2>⚙️ Installation & Usage</h2></summary>

### Prerequisites

* Python 3.x
* Tkinter (comes pre-installed with Python)

### Run the App

```bash
python calculator.py
```

</details>

---

<details>
<summary><h2>🌍 Real World Use Cases</h2></summary>

### 📌 Examples

* 🧑‍🎓 Students performing quick calculations
* 🧮 Desktop utility calculator
* 🧑‍💻 Learning GUI development with Tkinter
* 📚 Teaching OOP concepts in Python

### 🏢 Practical Scenarios

* Embedded calculator in desktop tools
* Prototype for advanced scientific calculators
* Internal tools for offices

</details>

---

<details>
<summary><h2>✅ Pros & ❌ Cons</h2></summary>

### ✅ Pros

* Simple and clean UI
* Easy to understand code
* Beginner-friendly
* Uses OOP principles
* Lightweight and fast

### ❌ Cons

* Uses `eval()` (security risk if extended)
* No scientific functions
* Desktop-only (no web/mobile)
* No input validation

</details>

---

<details>
<summary><h2>🔐 Security Considerations</h2></summary>

⚠️ `eval()` can execute arbitrary code
✔ Safe here because:

* Input is restricted to button clicks
* No direct user text input

🔒 For production:

* Replace `eval()` with a safe expression parser

</details>

---

<details>
<summary><h2>🚀 Future Enhancements</h2></summary>

* 🔢 Scientific calculator functions
* 📱 Mobile version using Kivy
* 🧠 Expression validation
* 🖱 Keyboard input support
* 🌙 Dark/Light mode
* 📦 Convert to `.exe` file

</details>

---

<details>
<summary><h2>🏷 SEO Keywords</h2></summary>

`Python Calculator`
`Tkinter GUI Calculator`
`Python Desktop Application`
`Beginner Python Project`
`GUI Calculator Python`
`Object Oriented Python Project`

</details>

---

<details>
<summary><h2> Screen Shot</h2></summary>

![Image](https://github.com/alok-kumar8765/Cool_Project_2/blob/main/Calculator/Output.png)

</details>

---


## ⭐ Author

**Alok Kumar**
🔗 GitHub: [https://github.com/alok-kumar8765](https://github.com/alok-kumar8765)

---

### ⭐ If you like this project, give it a star!



---
