# READ IMAGES AND VIDEOS

import cv2.cv2
from cv2 import cv2

print("Fine")

# To read and display image
img = cv2.imread("RESOURCES\\beach.jpg")
cv2.imshow("Output", img)
cv2.waitKey(0)

# To read and display video
vid = cv2.VideoCapture("C:\\Users\\sff\\Downloads\\video.mp4")

while True:
    success, image = vid.read()
    cv2.imshow("Output Video", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
