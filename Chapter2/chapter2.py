import cv2

img = cv2.imread('..\Resources\deer.jpg')

# Convert to grayscale

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur Image

imBlur = cv2.GaussianBlur(imgray,(7,7),0) # (7,7) is the kernel size. It should be an odd number

cv2.imshow('Gray Image', imgray)
cv2.imshow('Blurred Image', imBlur)

cv2.waitKey(0)                                  