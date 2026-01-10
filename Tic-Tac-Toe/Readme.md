
# 🎮 Tic Tac Toe – Python Tkinter GUI Application

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/GitHub-alok--kumar8765-black?style=for-the-badge&logo=github">
</p>

---

<details>
<summary><strong>📌 Project Overview</strong></summary>

### 📖 Title
**Tic Tac Toe Game using Python & Tkinter**

### 📝 Description
A **GUI-based two-player Tic Tac Toe game** built using **Python's Tkinter library**.  
The application allows players to enter their names, take turns, detects wins/ties automatically, and displays results via dialog boxes.

### 🎯 Key Objectives
- Practice **event-driven programming**
- Understand **Tkinter GUI layouts**
- Implement **game logic & state management**
- Build a **desktop-based interactive application**

</details>

---

<details>
<summary><strong>📚 Table of Contents</strong></summary>

1. Project Overview  
2. Features  
3. Tech Stack  
4. Application Flow  
5. Architecture Diagram  
6. Data Flow Diagram (DFD)  
7. Game Logic Explanation  
8. Mermaid Diagrams  
9. Pros & Cons  
10. Real World Use Cases  
11. Example Scenarios  
12. Future Enhancements  

</details>

---

<details>
<summary><strong>✨ Features</strong></summary>

- 👥 Two-player gameplay
- 🧑 Player name input support
- 🔁 Turn-based logic (X / O)
- 🏆 Automatic win detection
- 🤝 Tie detection
- 🚫 Button disabling after game end
- 🎨 Simple & clean UI with colors
- 🖥️ Desktop GUI (No CLI interaction)

</details>

---

<details>
<summary><strong>🛠️ Tech Stack</strong></summary>

- **Language:** Python 3.x  
- **GUI Framework:** Tkinter  
- **Paradigm:** Event-driven programming  
- **Platform:** Cross-platform (Windows / Linux / macOS)

</details>

---

<details>
<summary><strong>🔄 Application Flow</strong></summary>

```mermaid
flowchart TD
    A[Start Application] --> B[Enter Player Names]
    B --> C[Initialize Game Board]
    C --> D[Player Clicks Button]
    D --> E{Valid Move?}
    E -->|Yes| F[Mark X or O]
    F --> G[Check Win / Tie]
    G -->|Win| H[Show Winner]
    G -->|Tie| I[Show Tie Message]
    G -->|Continue| D
    E -->|No| J[Show Error Message]
```

</details>

---

<details>
<summary><strong>🏗️ Architecture Diagram</strong></summary>

```mermaid
graph LR
    UI[GUI Interface] --> Controller[Event Handler]
    Controller --> Logic[Game Logic]
    Logic --> UI
    Logic --> Popup[MessageBox Alerts]
```

</details>


---

<details>
<summary><strong>📊 Data Flow Diagram (DFD)</strong></summary>

```mermaid
graph TD
    Player1 -->|Click| GameSystem
    Player2 -->|Click| GameSystem
    GameSystem -->|Update Board| UI
    GameSystem -->|Result| MessageBox
```

</details>


---

<details>
<summary><strong>🧠 Game Logic Explanation</strong></summary>

- btnClick()

- Handles button clicks

- Alternates between X and O

- Prevents overwriting moves


- checkForWin()

- Checks all win combinations

- Detects tie condition

- Triggers message popup


- disableButton()

- Locks the board after game ends


Global flags:

- bclick → manages turn

- flag → counts moves



</details>

---

<details>
<summary><strong>✅ Pros & ❌ Cons</strong></summary>

## ✅ Pros

- Beginner-friendly code

- Easy to understand logic

- Lightweight and fast

- No external dependencies

- Great for learning GUI programming


## ❌ Cons

- No AI / single-player mode

- Hardcoded win conditions

- No restart/reset button

- Uses global variables

- Not scalable for larger boards


</details>

---

<details>
<summary><strong>🌍 Real World Use Cases</strong></summary>

- 🎓 Education:
  - Used in schools/colleges to teach Python GUI basics

- 🧪 Practice Project:
  - Ideal for beginners learning event handling

- 🖥️ Desktop App Demo:
  - Showcases how Python can build GUI apps

- 🧠 Logic Building:
  - Helps understand condition checking & state flow


</details>

---

<details>
<summary><strong>📌 Example Scenarios</strong></summary>

- Player 1 enters name Alice

- Player 2 enters name Bob

- Alice plays first with X

- Bob plays with O

- Alice completes a row

- Popup shows: Alice Wins!


</details>

---

<details>
<summary><strong>🚀 Future Enhancements</strong></summary>

- 🔁 Restart / Reset button

- 🤖 Single-player mode with AI

- 📊 Scoreboard tracking

- 🌐 Online multiplayer

- 📱 Mobile-friendly version

- 🧩 MVC-based refactoring


</details>

---

<p align="center">
  <strong>⭐ If you like this project, give it a star on GitHub!</strong><br>
  🔗 <a href="https://github.com/alok-kumar8765/Cool_Project_2">alok-kumar8765/Cool_Project_2</a>
</p>

---

