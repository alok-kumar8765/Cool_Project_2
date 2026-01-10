
# 📝 Cool_Project_2 — Python GUI Text Editor

<p align="center">
  <b>A lightweight, beginner-friendly desktop text editor built using Python & Tkinter</b>
</p>

<p align="center">
  <a href="https://github.com/alok-kumar8765/Cool_Project_2">
    <img src="https://img.shields.io/badge/GitHub-alok--kumar8765-black?style=for-the-badge&logo=github">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Stable-success?style=for-the-badge">
</p>

---

<details>
<summary><h2>📌 Project Overview</h2></summary>

### 🔹 Title
**Cool_Project_2 – Python Tkinter Text Editor**

### 🔹 Description
A simple yet powerful **desktop text editor application** developed using **Python’s Tkinter GUI framework**.  
It allows users to **open**, **edit**, and **save text files** with an intuitive graphical interface.

### 🔹 Key Objective
To demonstrate:
- GUI application development in Python
- File handling operations
- Event-driven programming
- Clean and readable code structure

</details>

---

<details>
<summary><h2>📑 Table of Contents</h2></summary>

- 📌 Project Overview  
- ⚙️ Features  
- 🧩 Code Explanation  
- 🏗 Architecture  
- 🔄 Flow Diagram  
- 📊 Data Flow Diagram (DFD)  
- 🛠 Technology Stack  
- 🚀 Installation & Usage  
- 💡 Use Cases  
- 🌍 Real-World Applications  
- ✅ Pros & ❌ Cons  
- 📈 Future Enhancements  

</details>

---

<details>
<summary><h2>⚙️ Features</h2></summary>

- 📂 Open `.txt` and all file formats
- 💾 Save edited content to new files
- 🖥 Clean and responsive GUI layout
- 🧠 Beginner-friendly and readable code
- ⚡ Lightweight & fast execution
- 🪟 Cross-platform (Windows, Linux, macOS)

</details>

---

<details>
<summary><h2>🧩 Code Explanation</h2></summary>

### 🔹 `open_file()`
- Opens file dialog
- Reads selected file content
- Displays text inside Tkinter Text widget

### 🔹 `save_file()`
- Opens save dialog
- Writes current editor content to file
- Updates window title dynamically

### 🔹 GUI Layout
- **Text Widget** → Main editing area
- **Frame Widget** → Button container
- **Buttons** → Open & Save functionality
- **Grid Layout** → Responsive resizing

</details>

---

<details>
<summary><h2>🏗 Architecture Diagram</h2></summary>

```mermaid
graph TD
    User -->|Click Open/Save| GUI
    GUI --> FileDialog
    FileDialog --> FileSystem
    FileSystem --> GUI
```

</details>

---

<details>
<summary><h2>🔄 Application Flow Diagram</h2></summary>

```mermaid
flowchart LR
    Start --> LaunchApp
    LaunchApp --> UserAction
    UserAction -->|Open File| ReadFile
    UserAction -->|Save File| WriteFile
    ReadFile --> DisplayText
    WriteFile --> SaveConfirmation
```

</details>

---

<details>
<summary><h2>📊 Data Flow Diagram (DFD)</h2></summary>


```mermaid
flowchart TD
    User -->|Text Input| Editor
    Editor -->|Request| FileDialog
    FileDialog -->|Read/Write| FileSystem
    FileSystem --> Editor
```

</details>

---

<details>
<summary><h2>🛠 Technology Stack</h2></summary>

+ Language: Python 3.x

- GUI Library: Tkinter

h File Handling: Native Python I/O

- OS Support: Windows / Linux / macOS


</details>

---

<details>
<summary><h2>🚀 Installation & Usage</h2></summary>

## 🔹 Prerequisites

- Python 3.x installed


## 🔹 Run Application

- python text_editor.py

- No external dependencies required.

</details>

---

<details>
<summary><h2>💡 Use Cases</h2></summary>

- 🧑‍🎓 Learning GUI development in Python

- 📝 Quick text editing without heavy IDEs

- 🧪 Prototyping file-based applications

- 👨‍🏫 Teaching event-driven programming


</details>

---

<details>
<summary><h2>🌍 Real-World Applications</h2></summary>

- Students: Notes & assignment drafting

- Developers: Editing config / log files

h Offices: Lightweight internal tools

- Education: Tkinter demonstration projects


h 📌 Example:
A school computer lab uses this app for basic text editing without installing heavy software.

</details>


---

<details>
<summary><h2>✅ Pros & ❌ Cons</h2></summary>

## ✅ Pros

- Simple & clean codebase

- No external libraries needed

- Cross-platform

h Easy to extend


## ❌ Cons

- No syntax highlighting

- No autosave feature

- Limited formatting options

- Not suitable for large files


</details>

---

<details>
<summary><h2>📈 Future Enhancements</h2></summary>

- 🔍 Search & replace

- 🎨 Syntax highlighting

- 💾 Autosave functionality

- 📁 Multi-tab support

- 🌙 Dark mode UI


</details>

---

<p align="center">
  <b>⭐ If you like this project, give it a star on GitHub!</b><br>
  🔗 <a href="https://github.com/alok-kumar8765/Cool_Project_2">github.com/alok-kumar8765/Cool_Project_2</a>
</p>

---

