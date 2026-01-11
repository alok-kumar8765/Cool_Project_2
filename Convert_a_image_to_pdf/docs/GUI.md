# **Folder Structure with GUI**

```
Convert_a_image_to_pdf/
│
├── src/
│   └── image_to_pdf/
│       ├── __init__.py
│       ├── converter.py            # CLI script
│       ├── api.py                  # FastAPI REST API
│       ├── tasks.py                # Celery async task
│       ├── auth.py                 # JWT + Rate limiting
│       └── gui.py                  # GUI using PyQt6
│
├── Dockerfile
├── docker-compose.yml
├── k8s-deploy.yaml
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

## **1️⃣ src/image_to_pdf/gui.py** (PyQt6 GUI)

```python
import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QVBoxLayout, QMessageBox
from converter import convert

class ImageToPDFGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image to PDF Converter")
        self.setGeometry(300, 300, 400, 200)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Select a JPG file or folder:")
        layout.addWidget(self.label)

        self.btn_select = QPushButton("Select File/Folder")
        self.btn_select.clicked.connect(self.select_file)
        layout.addWidget(self.btn_select)

        self.btn_convert = QPushButton("Convert to PDF")
        self.btn_convert.clicked.connect(self.convert_pdf)
        layout.addWidget(self.btn_convert)

        self.setLayout(layout)
        self.path = None

    def select_file(self):
        options = QFileDialog.Options()
        file_path = QFileDialog.getExistingDirectory(self, "Select Folder")  # folder selection
        if not file_path:
            file_path, _ = QFileDialog.getOpenFileName(self, "Select JPG file", "", "Images (*.jpg)", options=options)
        if file_path:
            self.path = file_path
            self.label.setText(f"Selected: {file_path}")

    def convert_pdf(self):
        if not self.path:
            QMessageBox.warning(self, "Warning", "Please select a file or folder first!")
            return
        try:
            convert(self.path, "output_gui.pdf")
            QMessageBox.information(self, "Success", "PDF created successfully as output_gui.pdf")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Conversion failed: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageToPDFGUI()
    window.show()
    sys.exit(app.exec())
```

---

## **2️⃣ Update requirements.txt**

```txt
fastapi
uvicorn
img2pdf
celery[redis]
redis
python-multipart
slowapi
PyQt6
```

---

## **3️⃣ Docker Update (Optional GUI support)**

GUI apps cannot directly run in container with display without X server, but we can still keep CLI and API in Docker. For local GUI, you can run `gui.py` directly:

```bash
python src/image_to_pdf/gui.py
```

---

## **4️⃣ Features Added by GUI**

* 🖱️ Select single JPG file or folder via file picker
* 📄 Shows selected file/folder path
* ✅ Converts images to `output_gui.pdf`
* ⚠️ Error handling with dialog boxes
* GUI is lightweight, no backend server required

---

## **5️⃣ Integration with Existing Stack**

* CLI (`converter.py`) → unchanged
* REST API (`api.py`) → unchanged
* Async tasks (`tasks.py`) → unchanged
* Celery + Redis → unchanged
* Docker/K8s → unchanged (GUI runs locally)
* PyQt GUI → optional local desktop tool

---

## **6️⃣ Running GUI**

```bash
pip install -r requirements.txt
python src/image_to_pdf/gui.py
```

* Select file or folder
* Click **Convert to PDF**
* `output_gui.pdf` will be saved in project root

---
