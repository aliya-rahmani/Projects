from fpdf import FPDF
from PIL import Image
import glob
import os

image_extensions = ("*.png", "*.jpg")
images = []

pdf = FPDF()

w, h = 0, 0

for extension in image_extensions:
    images.extend(glob.glob(extension))

for i in range(0, len(images)):
    print(images[i])

for i in range(0, len(images)):
    cover = Image.open(images[i])
    w, h = cover.size

for image in images:
    pdf.add_page()

    pdf.image(image, 0, 0, 210, 297)

print("\nFound " + str(len(images)) +
      " image files. Converting to PDF....\n")
pdf.output("output.pdf", "F")
print("Done!")
