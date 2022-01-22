# RESIZING AND CROPPING IMAGES

from cv2 import cv2
import numpy as np

img = cv2.imread("RESOURCES\\car.jpg")
print(img.shape)  # Printing resolution of the image

# To resize an image
img_resize = cv2.resize(img, (200, 300))  # Parameters (Width, Height)
print(img_resize.shape)

# To crop an image
img_crop = img[0:100, 100:500]  # Parameters (Height, Width)
print(img_crop.shape)


cv2.imshow("Original", img)
cv2.imshow("Resized", img_resize)
cv2.imshow("Cropped", img_crop)

cv2.waitKey(0)
