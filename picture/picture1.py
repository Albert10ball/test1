# encoding = utf -8
__author__ = "Albert"

from PIL import Image, ImageFilter

im = Image.open("C:\\Users\\Albert\\Pictures\\你不管.jpg")
w, h = im.size
print("Image size : %sx%s" % (w, h))
# 缩放50%
# im.thumbnail(2*w, 2*h)
# print("Resize image size: %sx%s" % (2*w, 2*h))
im2 = im.filter(ImageFilter.BLUR)

im2.save("C:\\Users\\Albert\\Pictures\\你不管2.png", "png")



