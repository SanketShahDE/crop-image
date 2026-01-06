
# 📸 Image Cropper Utility

A lightweight Python utility designed to crop specific regions from images using the **Pillow (PIL)** library. This tool is perfect for extracting fixed-coordinate regions like facial features, UI elements, sprites, or any defined pixel area for datasets and assets.

## 🚀 Features

* **Coordinate-Based Cropping:** Extract any rectangular region using pixel coordinates.
* **Precision Control:** Define exact $x, y$ starting points along with width and height with help of pixspy.com.
* **Batch Ready:** Easily extensible for processing multiple images at once.
* **Lightweight:** Minimal dependencies using the industry-standard Pillow library.

---

## 📦 Requirements

To run this script, you need Python installed on your system. The only external dependency is `Pillow`.

Create a file named `requirements.txt` and add:
```text
Pillow

```

---

## 🛠️ Setup Instructions

Follow these steps to set up an isolated environment and run the utility.

### 1. Create a Virtual Environment

Open a terminal in the project folder and run:

```bash
python -m venv venv

```

### 2. Activate the Virtual Environment

* **Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1

```


* **Windows (CMD):**
```cmd
.\venv\Scripts\activate.bat

```


* **macOS / Linux:**
```bash
source venv/bin/activate

```



### 3. Install Dependencies

With the virtual environment active, install the required library:

```bash
pip install -r requirements.txt

```

---

## 🧩 Usage & Logic

The script uses a coordinate system where  is the **top-left** corner of the image.

### Example Code (`cropper.py`)

```python
from PIL import Image

def crop_image(input_path, output_path, x, y, w, h):
    """
    Crops an image based on provided coordinates and dimensions.
    
    Args:
        input_path (str): Path to source image.
        output_path (str): Path to save the result.
        x (int): Starting X coordinate (left).
        y (int): Starting Y coordinate (top).
        w (int): Width of the crop.
        h (int): Height of the crop.
    """
    try:
        img = Image.open(input_path)
        # Pillow uses (left, top, right, bottom) tuple
        crop_box = (x, y, x + w, y + h)
        cropped_img = img.crop(crop_box)
        cropped_img.save(output_path)
        print(f"✅ Saved: {output_path}")
    except FileNotFoundError:
        print(f"❌ Error: {input_path} not found.")

if __name__ == "__main__":
    # Example coordinates for facial feature extraction
    MOUTH_X, MOUTH_Y = 485, 100
    MOUTH_W, MOUTH_H = 390, 550

    crop_image("input_image.png", "output_crop.png", MOUTH_X, MOUTH_Y, MOUTH_W, MOUTH_H)

```

### Running the Script

Simply execute the Python file:

```bash
python cropper.py

```

---

## 🧹 Cleanup

When you are finished working, you can exit the virtual environment by typing:

```bash
deactivate

```
