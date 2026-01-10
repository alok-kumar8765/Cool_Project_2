# 🔧 1️⃣ Fixing the Protocol-Check Bug (Professionally)

❌ Bug in the original code

- if ("https" or "http") in url:

- 👉 This always evaluates to "https" in url due to Python truthiness.


---

## ✅ Correct & Robust Fix

```python
from urllib.parse import urlparse
from urllib.request import urlopen
import time


def normalize_url(url: str) -> str:
    """Ensure URL has a valid scheme."""
    parsed = urlparse(url)
    if not parsed.scheme:
        return f"https://{url}"
    return url


def get_load_time(url: str) -> float:
    """
    Measure website load time in seconds.

    Args:
        url (str): Website URL

    Returns:
        float: Load time in seconds
    """
    url = normalize_url(url)

    start_time = time.time()
    with urlopen(url) as response:
        response.read()
    end_time = time.time()

    return end_time - start_time
```

- ✔ RFC-compliant
  
- ✔ Handles missing scheme
  
- ✔ Cleaner & safer


---

## 📦 2️⃣ Convert Into a Proper Python Package

### 📁 Project Structure

```text
cool_project_2/
│
├── cool_project_2/
│   ├── __init__.py
│   ├── core.py
│   ├── utils.py
│
├── tests/
│   ├── __init__.py
│   └── test_core.py
│
├── web/
│   └── app.py
│
├── setup.py
├── README.md
├── requirements.txt
└── pyproject.toml
```

---

## 📄 core.py

```python
from urllib.request import urlopen
import time
from .utils import normalize_url


def get_load_time(url: str) -> float:
    url = normalize_url(url)
    start = time.time()
    with urlopen(url) as r:
        r.read()
    return time.time() - start
```

---

## 📄 utils.py

```python
from urllib.parse import urlparse


def normalize_url(url: str) -> str:
    parsed = urlparse(url)
    if not parsed.scheme:
        return f"https://{url}"
    return url
```

---

## 📄 setup.py

```python
from setuptools import setup, find_packages

setup(
    name="cool_project_2",
    version="1.0.0",
    description="Website Load Time Analyzer",
    author="Alok Kumar",
    packages=find_packages(),
    python_requires=">=3.8",
)
```

---

## 🧪 3️⃣ Unit Tests (PyTest)

### 📄 tests/test_core.py

```python
from cool_project_2.core import get_load_time


def test_valid_url():
    time_taken = get_load_time("https://www.google.com")
    assert time_taken > 0


def test_url_without_scheme():
    time_taken = get_load_time("google.com")
    assert time_taken > 0
```

## ▶ Run Tests

```python
pip install pytest
pytest
```

- ✔ CI-ready
- ✔ Regression safe
- ✔ Professional testing standard


---

## 🌐 4️⃣ Web Version (Flask – Lightweight & Clean)

### 📄 web/app.py

```python
from flask import Flask, request, jsonify
from cool_project_2.core import get_load_time

app = Flask(__name__)


@app.route("/load-time", methods=["GET"])
def load_time():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        time_taken = get_load_time(url)
        return jsonify({
            "url": url,
            "load_time_seconds": round(time_taken, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
```

---

## ▶ Run Web App

```
pip install flask
python web/app.py
```

## 🌍 API Usage

GET http://127.0.0.1:5000/load-time?url=google.com

- ✅ JSON Response

```
{
  "url": "google.com",
  "load_time_seconds": 0.41
}
```

---

