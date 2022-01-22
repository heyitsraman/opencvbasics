# BASIC PROCESSING OF IMAGES

from cv2 import cv2
import numpy as np

img = cv2.imread("RESOURCES\\desert.jpg")
kernel = np.ones((5,5),np.uint8)

# To read and display both original and gray image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# To use Gaussian Blur
img_blur = cv2.GaussianBlur(img, (7, 7), 0)

# To use Edge Detector using canny
img_edge = cv2.Canny(img,50,250)

# To use Dilation
img_dilate = cv2.dilate(img,kernel,iterations=5)

# To use Erosion
img_eroded = cv2.erode(img_dilate,kernel, iterations=1)

# OUTPUTS
cv2.imshow("Original", img)
cv2.imshow("Gray", img_gray)
cv2.imshow("Blurred", img_blur)
cv2.imshow("Edges", img_edge)
cv2.imshow("Dilation", img_dilate)
cv2.imshow("Eroded Image", img_eroded)
cv2.waitKey(0)
