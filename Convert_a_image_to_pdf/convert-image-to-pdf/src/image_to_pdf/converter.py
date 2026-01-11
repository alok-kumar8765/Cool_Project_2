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
