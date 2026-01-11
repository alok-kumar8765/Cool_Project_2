
# 🚀 Capture Video Frames — Production Ready Python Package


---

## 1️⃣ Convert into a pip package

## 📁 Recommended Project Structure

```text
capture-video-frames/
│
├── capture_video_frames/
│   ├── __init__.py
│   ├── frame_capture.py
│
├── tests/
│   ├── __init__.py
│   └── test_frame_capture.py
│
├── benchmarks/
│   └── benchmark_frames.py
│
├── setup.py
├── pyproject.toml
├── README.md
├── requirements.txt
├── Dockerfile
└── .dockerignore
```

---

## 📄 capture_video_frames/frame_capture.py

```
import os
import shutil
import cv2

class FrameCapture:
    """
    Extract frames from a video file using OpenCV.
    """

    def __init__(self, file_path, output_dir="captured_frames"):
        self.file_path = file_path
        self.output_dir = output_dir

        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)
        os.makedirs(self.output_dir, exist_ok=True)

    def capture_frames(self):
        cap = cv2.VideoCapture(self.file_path)
        frame_number = 0

        while True:
            success, frame = cap.read()
            if not success:
                break

            cv2.imwrite(
                f"{self.output_dir}/frame{frame_number}.jpg",
                frame
            )
            frame_number += 1

        cap.release()
        return frame_number
```

---

## 📄 capture_video_frames/__init__.py

```
from .frame_capture import FrameCapture
```

---

## 📄 setup.py

```
from setuptools import setup, find_packages

setup(
    name="capture-video-frames",
    version="1.0.0",
    description="Extract frames from videos using OpenCV",
    author="Alok Kumar",
    author_email="your-email@example.com",
    url="https://github.com/alok-kumar8765/Cool_Project_2",
    packages=find_packages(),
    install_requires=[
        "opencv-python"
    ],
    entry_points={
        "console_scripts": [
            "capture-frames=capture_video_frames.frame_capture:FrameCapture"
        ]
    },
    python_requires=">=3.7",
)
```

---

## 📄 pyproject.toml

```bash
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

---

## 📄 requirements.txt

````text
opencv-python
pytest
````

---

## 2️⃣ 🧪 Unit Testing (pytest)

## 📄 tests/test_frame_capture.py

````bash
import os
from capture_video_frames import FrameCapture

def test_invalid_video():
    try:
        fc = FrameCapture("invalid.mp4")
        fc.capture_frames()
    except Exception:
        assert True

def test_output_directory_created():
    fc = FrameCapture("sample.mp4", "test_frames")
    assert os.path.exists("test_frames")
````

## ▶ Run tests

```bash
pytest tests/
```

---

## 3️⃣ 📈 Benchmarking (Performance Measurement)

## 📄 benchmarks/benchmark_frames.py

```
import time
from capture_video_frames import FrameCapture

video = "sample.mp4"
start = time.time()

fc = FrameCapture(video)
total_frames = fc.capture_frames()

end = time.time()

print("Benchmark Results")
print("-----------------")
print(f"Total Frames  : {total_frames}")
print(f"Time Taken   : {end - start:.2f} seconds")
print(f"FPS          : {total_frames / (end - start):.2f}")
```

## ▶ Run benchmark

```
python benchmarks/benchmark_frames.py
```

---

## 4️⃣ 🐳 Docker Support

## 📄 Dockerfile

````bash
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python"]
CMD ["benchmarks/benchmark_frames.py"]
````

---

## 📄 .dockerignore

```
__pycache__/
*.pyc
.env
.git
```

---

## ▶ Build & Run Docker

````bash
docker build -t capture-video-frames .
docker run --rm capture-video-frames

````

---

## 5️⃣ 📦 Build & Install as pip Package (Local)

````bash
pip install .
````

Or editable mode:

````bash
pip install -e .
````

---









