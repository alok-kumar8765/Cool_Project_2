

# 📦 1. Making it pip-installable (Professional Level)

This is an excellent move — very few beginners do this.

What “pip-installable” means

After this, anyone can do:

```
pip install bouncing-ball-simulator
bouncing-ball
```

…and this game runs 🎉


---

## 🏗️ Step-by-Step: Convert This Project into a pip Package

### ✅ 1. Restructure the project

```text
bouncing_ball_simulator/
│
├── bouncing_ball/
│   ├── __init__.py
│   ├── game.py          # main pygame logic (your code)
│   └── assets/
│       ├── ball.png
│       └── background-img.jpg
│
├── README.md
├── pyproject.toml
└── setup.cfg

```

---

## ✅ 2. Move this code into game.py

```
def run():
    import pygame, time, random
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Ball Bounce Simulation")

    background = pygame.image.load(
        pygame.resource_path("assets/background-img.jpg")
    )

    class Ball:
        ball_image = pygame.image.load(
            pygame.resource_path("assets/ball.png")
        )
        g = 1
        ...
    
    # main loop here
```

(Assets inside package = professional standard)


---

## ✅ 3. Add __init__.py

```
from .game import run
```

---

## ✅ 4. Create pyproject.toml

```
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

---

## ✅ 5. Create setup.cfg

```
[metadata]
name = bouncing-ball-simulator
version = 1.0.0
author = Alok Kumar
description = A physics-based bouncing ball simulation using Pygame
long_description = file: README.md
long_description_content_type = text/markdown
license = MIT
url = https://github.com/alok-kumar8765/Cool_Project_2
classifiers =
    Programming Language :: Python :: 3
    Topic :: Games/Entertainment
    Topic :: Scientific/Engineering :: Physics

[options]
packages = find:
install_requires =
    pygame>=2.0
python_requires = >=3.8
include_package_data = True

[options.entry_points]
console_scripts =
    bouncing-ball = bouncing_ball.game:run
```

---

## ✅ 6. Include assets (VERY IMPORTANT)

Create MANIFEST.in

```
recursive-include bouncing_ball/assets *.png *.jpg
```

---

## ▶️ Install & Run (Locally)

```
pip install .
bouncing-ball
```

🎉 This simulation now runs like a real app


---

# 🎮 Bouncing Ball Mini-Game (Playable + Scoring)

## **🕹️ Game Rules**

- Balls fall with gravity

- They bounce elastically off walls

- Click on a ball to destroy it

- Each hit increases score

- Missed balls reduce lives

- Game ends when lives reach 0

- Restart with R



---

## 📂 Final Project Structure (Required)

```text
bouncing_ball_game/
│
├── game.py
├── assets/
│   ├── ball.png
│   └── background-img.jpg
└── requirements.txt
```

---

## 🧠 Complete Playable Game Code (game.py)

```
import pygame
import random
import sys

# ---------------- CONFIG ----------------
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 1
BALL_RADIUS = 16
MAX_BALLS = 5
LIVES = 5

# ---------------- INIT ----------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Mini Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 24)

# ---------------- ASSETS ----------------
ball_img = pygame.image.load("assets/ball.png").convert_alpha()
bg_img = pygame.image.load("assets/background-img.jpg").convert()

# ---------------- BALL CLASS ----------------
class Ball:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(0, 200)
        self.vx = random.choice([-4, 4])
        self.vy = random.randint(2, 5)
        self.rect = ball_img.get_rect(center=(self.x, self.y))

    def update(self):
        self.vy += GRAVITY
        self.x += self.vx
        self.y += self.vy

        if self.x <= 0 or self.x >= WIDTH - BALL_RADIUS * 2:
            self.vx *= -1

        if self.y >= HEIGHT - BALL_RADIUS * 2:
            self.vy *= -0.9
            self.y = HEIGHT - BALL_RADIUS * 2

        self.rect.topleft = (self.x, self.y)

    def draw(self):
        screen.blit(ball_img, self.rect)

# ---------------- GAME STATE ----------------
def reset_game():
    return [Ball() for _ in range(MAX_BALLS)], 0, LIVES, False

balls, score, lives, game_over = reset_game()

# ---------------- MAIN LOOP ----------------
running = True
while running:
    clock.tick(FPS)
    screen.blit(bg_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_pos = pygame.mouse.get_pos()
            for ball in balls[:]:
                if ball.rect.collidepoint(mouse_pos):
                    balls.remove(ball)
                    balls.append(Ball())
                    score += 10

        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                balls, score, lives, game_over = reset_game()

    if not game_over:
        for ball in balls:
            ball.update()
            if ball.y > HEIGHT:
                balls.remove(ball)
                balls.append(Ball())
                lives -= 1

        if lives <= 0:
            game_over = True

    for ball in balls:
        ball.draw()

    # ---------------- UI ----------------
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))

    if game_over:
        over_text = font.render("GAME OVER - Press R to Restart", True, (255, 50, 50))
        screen.blit(over_text, (WIDTH // 2 - 180, HEIGHT // 2))

    pygame.display.flip()

pygame.quit()
sys.exit()
```

---

## 📦 requirements.txt

```
pygame>=2.0
```

---

# 🪟 Build Windows .EXE (Single Click Game)

## ✅ Step 1: Install PyInstaller

```
pip install pyinstaller
```

---

## ✅ Step 2: Build Executable

Run this inside project folder:

```
pyinstaller --onefile --windowed --add-data "assets;assets" game.py
```

✔ --windowed → no terminal
✔ --onefile → single .exe
✔ --add-data → include images


---

## 📁 Output Location

```
dist/
└── game.exe

```
🎉 Double-click to play!


---

🧠 What You’ve Now Built (Seriously Impressive)

✔ Real playable game
✔ Scoring system
✔ Game over & restart
✔ Asset handling
✔ Windows executable
✔ Resume-worthy project
✔ Game-dev fundamentals


---






