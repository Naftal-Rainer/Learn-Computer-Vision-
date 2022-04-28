import cv2

# Reading Images
img = cv2.imread('Resources/deer.jpg')

# Display Image

cv2.imshow('Output', img)
cv2.waitKey(0)

