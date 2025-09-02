from PIL import Image, ImageFilter

img = Image.open("sample.jpg")

blur_img = img.filter(ImageFilter.BLUR)
contour_img = img.filter(ImageFilter.CONTOUR)
emboss_img = img.filter(ImageFilter.EMBOSS)

w, h = img.size
blur_img = blur_img.resize((w, h))
contour_img = contour_img.resize((w, h))
emboss_img = emboss_img.resize((w, h))

collage = Image.new("RGB", (w * 2, h * 2))
collage.paste(img, (0, 0))
collage.paste(blur_img, (w, 0))
collage.paste(contour_img, (0, h))
collage.paste(emboss_img, (w, h))

collage.save("collage.jpg")
