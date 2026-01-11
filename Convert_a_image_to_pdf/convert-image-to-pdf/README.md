# 📦 PyPI Packaging Guide

## Image to PDF Converter (Python CLI Tool)

> Turn your Python script into a **pip-installable CLI package** like a real-world professional library.

---

<details>
<summary><h2>📌 Why PyPI Packaging?</h2></summary>

Publishing your project to **PyPI** allows users to:

* Install via `pip install image-to-pdf-converter`
* Use it as a **global CLI command**
* Integrate into automation & CI/CD
* Showcase production-level Python skills

✔ Essential for **resume, GitHub credibility, and open-source adoption**

</details>

---

<details>
<summary><h2>📂 Recommended Project Structure</h2></summary>

```
convert-image-to-pdf/
│
├── src/
│   └── image_to_pdf/
│       ├── __init__.py
│       └── converter.py
│
├── README.md
├── LICENSE
├── pyproject.toml
└── .gitignore
```

📌 **Why `src/` layout?**

* Prevents import bugs
* PyPI best practice
* Used by major libraries

</details>

---

<details>
<summary><h2>🧠 Refactored Python Code (converter.py)</h2></summary>

```python
import sys
import os
import img2pdf

def convert(path):
    if os.path.isdir(path):
        images = [
            os.path.join(path, f)
            for f in os.listdir(path)
            if f.lower().endswith(".jpg")
        ]
        if not images:
            print("No JPG images found.")
            return

        with open("output.pdf", "wb") as f:
            f.write(img2pdf.convert(images))

    elif os.path.isfile(path) and path.lower().endswith(".jpg"):
        with open("output.pdf", "wb") as f:
            f.write(img2pdf.convert(path))
    else:
        print("Invalid file or directory.")

def main():
    if len(sys.argv) != 2:
        print("Usage: img2pdf-convert <file_or_folder>")
        return
    convert(sys.argv[1])
```

✔ Modular
✔ Import-safe
✔ CLI-ready

</details>

---

<details>
<summary><h2>⚙️ pyproject.toml (Core of PyPI Packaging)</h2></summary>

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "image-to-pdf-converter"
version = "1.0.0"
description = "Convert JPG images or folders into a single PDF using Python CLI"
readme = "README.md"
license = { text = "MIT" }
authors = [
  { name="Alok Kumar", email="your-email@example.com" }
]
keywords = ["image", "pdf", "converter", "cli", "automation"]
classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
]

dependencies = [
  "img2pdf"
]

[project.scripts]
img2pdf-convert = "image_to_pdf.converter:main"

[project.urls]
Homepage = "https://github.com/alok-kumar8765/Cool_Project_2"
Source = "https://github.com/alok-kumar8765/Cool_Project_2"
```

📌 This enables:

```bash
img2pdf-convert images/
```

</details>

---

<details>
<summary><h2>📜 README.md (Minimum Required)</h2></summary>

Your existing README (already created earlier) is **PyPI compatible**.

Ensure it includes:

* Project description
* Installation
* Usage
* GitHub link

PyPI renders **Markdown automatically**.

</details>

---

<details>
<summary><h2>📦 Build the Package</h2></summary>

### 1️⃣ Install build tools

```bash
pip install --upgrade build twine
```

### 2️⃣ Build package

```bash
python -m build
```

Output:

```
dist/
 ├── image_to_pdf_converter-1.0.0.tar.gz
 └── image_to_pdf_converter-1.0.0-py3-none-any.whl
```

</details>

---

<details>
<summary><h2>🚀 Publish to PyPI</h2></summary>

### 1️⃣ Create account

👉 [https://pypi.org/account/register/](https://pypi.org/account/register/)

### 2️⃣ Upload

```bash
twine upload dist/*
```

🔐 Enter PyPI username & API token

</details>

---

<details>
<summary><h2>▶️ Install from PyPI (After Publishing)</h2></summary>

```bash
pip install image-to-pdf-converter
```

Use anywhere:

```bash
img2pdf-convert ./images
```

✔ Global CLI
✔ Cross-platform

</details>

---

<details>
<summary><h2>🌍 Real-World Use Case</h2></summary>

### Example: Office Automation Script

```bash
img2pdf-convert scanned_documents/
```

Used in:

* Govt offices
* Banks
* Schools
* Legal firms
* Backend batch jobs

</details>

---

<details>
<summary><h2>✅ Pros & ❌ Cons (PyPI Version)</h2></summary>

### ✅ Pros

* Professional distribution
* Easy installation
* CLI ready
* Automation friendly

### ❌ Cons

* Requires version management
* Initial setup complexity

</details>

---

<details>
<summary><h2>🧩 Future PyPI Enhancements</h2></summary>

* 🔢 Versioned output filenames
* 🧾 PNG/JPEG support
* 📄 Sort images by name/date
* 🧪 Unit tests
* 🛠️ GitHub Actions auto-publish

</details>

---

## ⭐ Final Tip

Publishing this to PyPI makes your project look **industry-grade** and **resume-ready**.
