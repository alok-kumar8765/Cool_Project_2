# 🖼️ Image to PDF Converter (Python CLI Tool)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" />
  <img src="https://img.shields.io/badge/CLI-Utility-green.svg" />
  <img src="https://img.shields.io/badge/PDF-Automation-red.svg" />
  <img src="https://img.shields.io/badge/Open%20Source-Yes-orange.svg" />
  <img src="https://img.shields.io/github/stars/alok-kumar8765/Cool_Project_2?style=social" />
</p>

---

## 📌 Project Title
**Convert JPG Images to PDF using Python (Single File or Folder)**

---

<details>
<summary><h2>📖 Description</h2></summary>

This project is a **lightweight Python Command Line Interface (CLI) utility** that converts:

- ✅ A **single JPG image** into a PDF  
- ✅ **Multiple JPG images from a directory** into a single PDF  

It uses the powerful **`img2pdf`** library to ensure **lossless image-to-PDF conversion**, making it ideal for automation, scripting, and backend processing.

</details>

---

<details>
<summary><h2>📚 Table of Contents</h2></summary>

1. 📖 Description  
2. ⚙️ How It Works  
3. 🧠 Architecture Overview  
4. 🔁 Application Flow  
5. 📊 Data Flow Diagram (DFD)  
6. 🚀 Installation  
7. ▶️ Usage  
8. 📌 Use Cases  
9. 🌍 Real-World Examples  
10. ✅ Pros & ❌ Cons  
11. 🔐 Limitations  
12. 📦 Dependencies  
13. 🧩 Future Enhancements  

</details>

---

<details>
<summary><h2>⚙️ How It Works (Explanation)</h2></summary>

- Accepts a **file or directory path** via command-line arguments.
- Detects whether the input is:
  - 📁 A directory → converts all `.jpg` files inside.
  - 🖼️ A single `.jpg` file → converts it directly.
- Generates a single output file named **`output.pdf`**.
- Skips non-JPG files and subdirectories.
- Uses **binary-safe PDF writing**.

</details>

---

<details>
<summary><h2>🧠 System Architecture</h2></summary>

```mermaid
graph TD
    User[User CLI Input] --> PythonScript[Python Script]
    PythonScript -->|Validates Path| FileCheck{File or Folder?}
    FileCheck -->|Folder| ImageCollector[Collect JPG Images]
    FileCheck -->|File| SingleImage[Single JPG File]
    ImageCollector --> PDFGenerator[img2pdf Engine]
    SingleImage --> PDFGenerator
    PDFGenerator --> Output[output.pdf]
````

</details>

---

<details>
<summary><h2>🔁 Application Flow Diagram</h2></summary>

```mermaid
flowchart LR
    A[Start] --> B[Read CLI Argument]
    B --> C{Is Directory?}
    C -->|Yes| D[Scan JPG Files]
    C -->|No| E{Is JPG File?}
    E -->|Yes| F[Convert to PDF]
    E -->|No| G[Show Error]
    D --> F
    F --> H[Save output.pdf]
    H --> I[End]
```

</details>

---

<details>
<summary><h2>📊 Data Flow Diagram (DFD)</h2></summary>

```mermaid
graph LR
    User -->|File/Folder Path| Script
    Script -->|JPG Files| img2pdf
    img2pdf -->|Binary PDF Data| PDF_File
```

</details>

---

<details>
<summary><h2>🚀 Installation</h2></summary>

```bash
pip install img2pdf
```

✔ Python 3.x required
✔ Works on Windows, Linux, macOS

</details>

---

<details>
<summary><h2>▶️ Usage</h2></summary>

### Convert a Single Image

```bash
python convert.py image.jpg
```

### Convert a Folder of Images

```bash
python convert.py ./images/
```

📄 Output:

```text
output.pdf
```

</details>

---

<details>
<summary><h2>📌 Use Cases</h2></summary>

* 📄 Scanning documents and converting to PDF
* 🧾 Invoice and receipt digitization
* 📚 Creating study notes from images
* 🏢 Office automation scripts
* 📸 Bulk image archival

</details>

---

<details>
<summary><h2>🌍 Real-World Example</h2></summary>

### Example: Government Form Submission

A user scans multiple pages of a form as JPG images:

```
page1.jpg
page2.jpg
page3.jpg
```

Running:

```bash
python convert.py ./scans/
```

Result:

```
output.pdf
```

✔ Ready for upload to official portals
✔ Maintains original image quality

</details>

---

<details>
<summary><h2>✅ Pros & ❌ Cons</h2></summary>

### ✅ Pros

* Lightweight & fast
* Lossless image conversion
* Simple CLI interface
* No GUI overhead
* Scriptable & automation-friendly

### ❌ Cons

* Supports only `.jpg`
* Output filename is fixed
* No sorting control
* No GUI interface

</details>

---

<details>
<summary><h2>🔐 Limitations</h2></summary>

* Images are processed in OS directory order
* Does not support PNG, JPEG, or WebP yet
* Overwrites `output.pdf` if already present

</details>

---

<details>
<summary><h2>📦 Dependencies</h2></summary>

* **Python 3.x**
* **img2pdf**
* **os, sys (Standard Library)**

</details>

---

<details>
<summary><h2>🧩 Future Enhancements</h2></summary>

* 🔄 Support PNG/JPEG formats
* 🧾 Custom output filename
* 📂 Recursive directory scanning
* 🖥️ GUI version (Tkinter / PyQt)
* ☁️ Cloud-based PDF generation API

</details>

---

## ⭐ Repository

🔗 **GitHub:** [https://github.com/alok-kumar8765/Cool_Project_2](https://github.com/alok-kumar8765/Cool_Project_2)

---

### 🔥 If you like this project, don’t forget to ⭐ star the repository!



---

