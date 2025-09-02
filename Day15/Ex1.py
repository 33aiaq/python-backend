import numpy as np  
import pandas as pd
from PIL import Image, ImageDraw

data = {
    "Name": ["Ahmad", "Noor", "Hamza", "Anas", "Laith"],
    "Math": [85, 92, 78, 88, 90],
    "Science": [89, 94, 76, 85, 92],
    "English": [80, 85, 88, 90, 95]
}

df = pd.DataFrame(data)
print("Original Dataset:\n", df)

df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)
print("\nDataset with Averages:\n", df)

top_student = df.loc[df["Average"].idxmax()]
print("\nTop Student:\n", top_student)

img = Image.new("RGB", (200, 200), color="red")
draw = ImageDraw.Draw(img)
draw.rectangle([50, 50, 150, 150], fill="blue")
img.save("test_image.jpg")

gray_img = img.convert("L")
gray_img.save("test_image_gray.jpg")
print("\nTest image created and converted to grayscale.")
