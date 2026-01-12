# 🧠 Dominant Color Detection using **K-Means Clustering** (Upgraded Logic)

## ✅ Why K-Means is Better than Pixel Frequency

Our current logic:

* Counts **exact pixel values**
* Fails when image has **shades / gradients**
* Sensitive to noise

**K-Means solves this by:**

* Grouping similar colors together
* Finding *true visual dominant colors*
* Works well for real photos

---

## 🔥 Upgraded K-Means Code (OpenCV + NumPy)

```python
import cv2
import numpy as np

# ===============================
# 1. Read Image
# ===============================
path = input("Enter Image Path: ")

img = cv2.imread(path)
if img is None:
    print("❌ Image not found!")
    exit()

cv2.imshow("Original Image", img)

# ===============================
# 2. Reshape Image for K-Means
# ===============================
# Convert image to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Reshape to (pixels, 3)
pixels = img_rgb.reshape((-1, 3))
pixels = np.float32(pixels)

# ===============================
# 3. Apply K-Means
# ===============================
K = 3  # Number of dominant colors
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

_, labels, centers = cv2.kmeans(
    pixels,
    K,
    None,
    criteria,
    10,
    cv2.KMEANS_RANDOM_CENTERS
)

# Convert centers to uint8
centers = np.uint8(centers)

# ===============================
# 4. Find Dominant Color
# ===============================
unique_labels, counts = np.unique(labels, return_counts=True)
dominant_index = unique_labels[np.argmax(counts)]
dominant_color = centers[dominant_index]

print("🎨 Dominant Colors (RGB):", centers.tolist())
print("🏆 Most Dominant Color:", dominant_color.tolist())

# ===============================
# 5. Visualization
# ===============================
# Create color palette
palette = np.zeros((100, 300, 3), np.uint8)

for i, color in enumerate(centers):
    palette[:, i*100:(i+1)*100] = color

# Dominant color image
dominant_img = np.zeros((300, 300, 3), np.uint8)
dominant_img[:] = dominant_color

cv2.imshow("Dominant Color Palette", cv2.cvtColor(palette, cv2.COLOR_RGB2BGR))
cv2.imshow("Most Dominant Color", cv2.cvtColor(dominant_img, cv2.COLOR_RGB2BGR))

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## 🧩 How This Logic Works (Step-by-Step)

### 1️⃣ Image Preprocessing

* Image converted to **RGB**
* Flattened into `(N, 3)` pixels

### 2️⃣ K-Means Clustering

* Pixels grouped into **K clusters**
* Each cluster center = **dominant color**

### 3️⃣ Dominance Detection

* Count pixels per cluster
* Cluster with highest count = **main dominant color**

### 4️⃣ Visualization

* Palette of all dominant colors
* Separate full image of most dominant color

---

## 📊 Algorithm Flow (Mental Model)

```
Image → Pixels → K-Means → Color Clusters
                 ↓
          Most Populated Cluster
                 ↓
            Dominant Color
```

---

## 🌍 Real-World Applications (Improved Accuracy)

| Industry        | Use Case              |
| --------------- | --------------------- |
| 🎨 UI/UX        | Auto theme extraction |
| 🛒 E-Commerce   | Product color tagging |
| 📸 Photography  | Color grading         |
| 🧠 ML Pipelines | Feature extraction    |
| 🎥 Video        | Scene color analysis  |

---

## ⚖️ Comparison: Old vs New

| Feature           | Old Logic | K-Means    |
| ----------------- | --------- | ---------- |
| Gradient handling | ❌ No      | ✅ Yes      |
| Noise resistance  | ❌ Low     | ✅ High     |
| Real photos       | ❌ Weak    | ✅ Strong   |
| Industry usage    | ❌ Rare    | ✅ Standard |

---

