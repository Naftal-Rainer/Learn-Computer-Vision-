import cv2
import numpy as np

img = cv2.imread('..\Resources\deer.jpg')
kernel = np.ones((5,5), np.uint8)

# Convert to grayscale

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur Image

imBlur = cv2.GaussianBlur(imgray,(7,7),0) # (7,7) is the kernel size. It should be an odd number

# Image Edge Detector

immgCanny = cv2.Canny(img, 150,200)

# Increasing Image-line Thickness

imgDilation = cv2.dilate(immgCanny, kernel, iterations=1)

# Decreasing Image - lines

imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow('Gray Image', imgray)
cv2.imshow('Blurred Image', imBlur)
cv2.imshow('Canny Image', immgCanny)
cv2.imshow('Dilation Image', imgDilation)
cv2.imshow('Erosion Image', imgEroded)
cv2.waitKey(0)                                  