 
#  🎮 TIC TAC TOE – GUI + AI (Python Tkinter)

## 📦 Requirements

```
pip install playsound==1.2.2
```

> (Tkinter comes pre-installed with Python)




---

## 🧠 AI Difficulty Levels

### Level	Logic

- Easy	Random moves
- Hard	Win / Block / Strategy
- Minimax	Perfect AI (Unbeatable)



---

## 🧩 Full GUI Code :

```python
import tkinter as tk
from tkinter import messagebox
import random
import copy
from playsound import playsound
import threading

# ---------------- SOUND HANDLER ---------------- #
def play_sound(file):
    threading.Thread(target=lambda: playsound(file), daemon=True).start()

# ---------------- MAIN CLASS ---------------- #
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - GUI AI")
        self.root.resizable(False, False)

        self.theme = "dark"
        self.mode = "AI"
        self.difficulty = "Easy"

        self.scores = {"X": 0, "O": 0}
        self.current_player = "X"
        self.board = [""] * 9

        self.create_ui()
        self.apply_theme()

    # ---------------- UI ---------------- #
    def create_ui(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.info = tk.Label(self.frame, text="TIC TAC TOE", font=("Arial", 20, "bold"))
        self.info.grid(row=0, column=0, columnspan=3)

        self.score_label = tk.Label(self.frame, text="X: 0  |  O: 0", font=("Arial", 12))
        self.score_label.grid(row=1, column=0, columnspan=3)

        self.buttons = []
        for i in range(9):
            btn = tk.Button(
                self.frame,
                text="",
                font=("Arial", 20),
                width=5,
                height=2,
                command=lambda i=i: self.on_click(i)
            )
            btn.grid(row=2 + i // 3, column=i % 3)
            self.buttons.append(btn)

        self.controls()

    def controls(self):
        self.control = tk.Frame(self.root)
        self.control.pack(pady=5)

        tk.Button(self.control, text="Restart", command=self.reset).grid(row=0, column=0)
        tk.Button(self.control, text="Theme", command=self.toggle_theme).grid(row=0, column=1)

        tk.OptionMenu(self.control, tk.StringVar(value="AI"),
                      "AI", "PVP", command=self.set_mode).grid(row=0, column=2)

        tk.OptionMenu(self.control, tk.StringVar(value="Easy"),
                      "Easy", "Hard", "Minimax",
                      command=self.set_difficulty).grid(row=0, column=3)

    # ---------------- GAME LOGIC ---------------- #
    def on_click(self, i):
        if self.board[i] or self.check_winner():
            return

        self.make_move(i, self.current_player)
        play_sound("click.mp3")

        if self.check_end():
            return

        if self.mode == "AI":
            self.root.after(300, self.ai_move)

    def make_move(self, i, player):
        self.board[i] = player
        self.buttons[i].config(text=player)
        self.current_player = "O" if player == "X" else "X"

    def ai_move(self):
        if self.difficulty == "Easy":
            move = random.choice([i for i in range(9) if not self.board[i]])
        elif self.difficulty == "Hard":
            move = self.hard_ai()
        else:
            move = self.minimax_ai(self.board, "O")[1]

        self.make_move(move, "O")
        play_sound("click.mp3")
        self.check_end()

    def hard_ai(self):
        for p in ["O", "X"]:
            for i in range(9):
                temp = self.board[:]
                if not temp[i]:
                    temp[i] = p
                    if self.winner(temp) == p:
                        return i
        return random.choice([i for i in range(9) if not self.board[i]])

    def minimax_ai(self, board, player):
        winner = self.winner(board)
        if winner == "X": return (-1, None)
        if winner == "O": return (1, None)
        if "" not in board: return (0, None)

        moves = []
        for i in range(9):
            if board[i] == "":
                new = board[:]
                new[i] = player
                score = self.minimax_ai(new, "X" if player == "O" else "O")[0]
                moves.append((score, i))

        return max(moves) if player == "O" else min(moves)

    # ---------------- CHECKS ---------------- #
    def winner(self, b):
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a,b1,c in wins:
            if b[a] and b[a]==b[b1]==b[c]:
                return b[a]
        return None

    def check_winner(self):
        return self.winner(self.board)

    def check_end(self):
        w = self.check_winner()
        if w:
            play_sound("win.mp3")
            self.scores[w] += 1
            self.update_score()
            messagebox.showinfo("Winner", f"{w} Wins!")
            self.reset()
            return True
        if "" not in self.board:
            play_sound("draw.mp3")
            messagebox.showinfo("Draw", "It's a Draw!")
            self.reset()
            return True
        return False

    # ---------------- UTIL ---------------- #
    def reset(self):
        self.board = [""] * 9
        self.current_player = "X"
        for b in self.buttons:
            b.config(text="")

    def update_score(self):
        self.score_label.config(text=f"X: {self.scores['X']}  |  O: {self.scores['O']}")

    def toggle_theme(self):
        self.theme = "light" if self.theme == "dark" else "dark"
        self.apply_theme()

    def apply_theme(self):
        bg = "#1e1e1e" if self.theme == "dark" else "#ffffff"
        fg = "#ffffff" if self.theme == "dark" else "#000000"

        self.root.config(bg=bg)
        self.frame.config(bg=bg)
        self.control.config(bg=bg)
        self.info.config(bg=bg, fg=fg)
        self.score_label.config(bg=bg, fg=fg)

        for b in self.buttons:
            b.config(bg=bg, fg=fg, activebackground="#555")

    def set_mode(self, val):
        self.mode = val
        self.reset()

    def set_difficulty(self, val):
        self.difficulty = val
        self.reset()

# ---------------- RUN ---------------- #
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()

```

---

## 🔊 Sound Files Needed

Place these in the same folder:

> click.mp3
> win.mp3
> draw.mp3

(You can replace with any short sound clips)


---

# 🖥️ PART 1 — Convert GUI App to .EXE (Windows)

- ✅ Tool Used: PyInstaller

## 📦 Install PyInstaller

```
pip install pyinstaller
```

---

## 📁 Recommended Project Structure

```text
tic_tac_toe_gui/
│
├── tic_tac_toe/
│   ├── __init__.py
│   ├── main.py          # GUI code (rename your file)
│   ├── sounds/
│   │   ├── click.mp3
│   │   ├── win.mp3
│   │   └── draw.mp3
│
├── icon.ico             # optional
```

- 👉 Move your GUI code into main.py
- 👉 Update sound paths:

play_sound("sounds/click.mp3")


---

## ⚙️ Build EXE Command

**Run from project root:**

```
pyinstaller --onefile --windowed --add-data "tic_tac_toe/sounds;sounds" --icon=icon.ico tic_tac_toe/main.py
```

## 🔍 Flags Explained

Flag	Meaning

```
--onefile	Single .exe
--windowed	No console window
--add-data	Include sound files
--icon	App icon

```

---


## 📦 Output Location

> dist/main.exe

🎉 Your EXE is ready to share!


---

## ❗ Common Fixes

If sounds don’t play, use this helper:

```python
import sys, os

def resource_path(relative):
    try:
        base = sys._MEIPASS
    except:
        base = os.path.abspath(".")
    return os.path.join(base, relative)
```

Then:

> play_sound(resource_path("sounds/click.mp3"))


---

## 📦 PART 2 — Package as a pip Module

### 📁 Final Package Structure

```text
tic-tac-toe-ai/
│
├── tic_tac_toe/
│   ├── __init__.py
│   ├── main.py
│   ├── sounds/
│
├── README.md
├── setup.py
├── pyproject.toml
├── MANIFEST.in
├── LICENSE

```

---

## 🧾 setup.py

```python
from setuptools import setup, find_packages

setup(
    name="tic-tac-toe-ai",
    version="1.0.0",
    author="Alok Kumar",
    author_email="your@email.com",
    description="GUI Tic Tac Toe with AI (Easy, Hard, Minimax)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["playsound==1.2.2"],
    entry_points={
        "console_scripts": [
            "tic-tac-toe=tic_tac_toe.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
```

---

## 🧾 MANIFEST.in

```
recursive-include tic_tac_toe/sounds *.mp3
```

---

## 🧾 pyproject.toml

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

---

## ▶ Update main.py

Add at bottom:

```python
def main():
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

```

---

## 🛠 Build the Package

```
pip install build
python -m build
```
Output:

```
dist/
 ├── tic_tac_toe_ai-1.0.0-py3-none-any.whl
 └── tic_tac_toe_ai-1.0.0.tar.gz
```

---

## 📥 Install Locally


```
pip install dist/tic_tac_toe_ai-1.0.0-py3-none-any.whl
```

Run:

> tic-tac-toe


---

## 🌍 Publish to PyPI (Optional)

```
pip install twine
twine upload dist/*
```

(Requires PyPI account)


---


