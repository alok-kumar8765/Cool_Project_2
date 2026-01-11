# **Folder Structure**

```
Convert_a_image_to_pdf/
│
├── src/
│   └── image_to_pdf/
│       ├── __init__.py
│       ├── converter.py            # CLI script
│       ├── api.py                  # FastAPI REST API
│       ├── tasks.py                # Celery tasks
│       └── auth.py                 # JWT + Rate limiting
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

## **1️⃣ src/image_to_pdf/converter.py** (CLI)

```python
import sys
import os
import img2pdf

def convert(path: str, output="output.pdf"):
    if os.path.isdir(path):
        images = [os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith(".jpg")]
        if not images:
            print("No JPG images found.")
            return
        with open(output, "wb") as f:
            f.write(img2pdf.convert(images))
    elif os.path.isfile(path) and path.lower().endswith(".jpg"):
        with open(output, "wb") as f:
            f.write(img2pdf.convert(path))
    else:
        print("Invalid file or directory.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python converter.py <file_or_folder>")
        return
    convert(sys.argv[1])

if __name__ == "__main__":
    main()
```

---

## **2️⃣ src/image_to_pdf/api.py** (REST API with FastAPI)

```python
from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from fastapi.responses import FileResponse
from auth import get_current_user
from tasks import convert_images_task
import os

app = FastAPI(title="Image to PDF Converter API")

UPLOAD_FOLDER = "./uploads"
OUTPUT_FOLDER = "./outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.post("/convert")
async def convert_image(file: UploadFile = File(...), user: str = Depends(get_current_user)):
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(filepath, "wb") as f:
        f.write(await file.read())

    # Send to Celery async
    output_file = os.path.join(OUTPUT_FOLDER, f"{file.filename}.pdf")
    convert_images_task.delay(filepath, output_file)
    return {"status": "processing", "pdf_file": output_file}

@app.get("/download/{filename}")
def download_pdf(filename: str):
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path, media_type='application/pdf')
```

---

## **3️⃣ src/image_to_pdf/tasks.py** (Celery Async Task)

```python
from celery import Celery
import img2pdf, os

celery = Celery('tasks', broker='redis://redis:6379/0')

@celery.task
def convert_images_task(input_path: str, output_path: str):
    if os.path.isdir(input_path):
        images = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.lower().endswith(".jpg")]
        with open(output_path, "wb") as f:
            f.write(img2pdf.convert(images))
    elif os.path.isfile(input_path) and input_path.lower().endswith(".jpg"):
        with open(output_path, "wb") as f:
            f.write(img2pdf.convert(input_path))
```

---

## **4️⃣ src/image_to_pdf/auth.py** (JWT + Rate Limiting Example)

```python
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from slowapi.util import get_remote_address
from slowapi import Limiter

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
limiter = Limiter(key_func=get_remote_address)

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Minimal JWT validation for example
    if token != "supersecrettoken":
        raise HTTPException(status_code=401, detail="Invalid Token")
    return "user"
```

---

## **5️⃣ requirements.txt**

```
fastapi
uvicorn
img2pdf
celery[redis]
redis
python-multipart
slowapi
```

---

## **6️⃣ Dockerfile**

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY ./src /app/src
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "src.image_to_pdf.api:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## **7️⃣ docker-compose.yml**

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - redis
  redis:
    image: redis:7
  worker:
    build: .
    command: celery -A src.image_to_pdf.tasks worker --loglevel=info
    environment:
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - redis
```

---

## **8️⃣ Kubernetes Deployment (k8s-deploy.yaml)**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: image-to-pdf-api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: image-to-pdf
  template:
    metadata:
      labels:
        app: image-to-pdf
    spec:
      containers:
        - name: web
          image: your-dockerhub/image-to-pdf:latest
          ports:
            - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: image-to-pdf-service
spec:
  type: LoadBalancer
  selector:
    app: image-to-pdf
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8000
```

---

## **9️⃣ .env.example**

```
REDIS_URL=redis://redis:6379/0
JWT_SECRET=supersecrettoken
OUTPUT_FOLDER=./outputs
UPLOAD_FOLDER=./uploads
```

---

## ✅ Next Steps

1. Build Docker:

```bash
docker-compose up --build
```

2. Run API:

```bash
uvicorn src.image_to_pdf.api:app --reload
```

3. Run Celery Worker:

```bash
celery -A src.image_to_pdf.tasks worker --loglevel=info
```

4. Deploy Kubernetes:

```bash
kubectl apply -f k8s-deploy.yaml
```

5. Use CLI:

```bash
python src/image_to_pdf/converter.py ./images/
```
---

