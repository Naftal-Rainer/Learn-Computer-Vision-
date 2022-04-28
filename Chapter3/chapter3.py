import cv2

img = cv2.imread('../Resources/lambo.jpg')


# Resizing Image

imgResize = cv2.resize(img, (1000,500))

# Cropping Image

imgcrop = img[0:200, 100:500]

cv2.imshow('Lamborghini', img)
# cv2.imshow('Resized Image', imgResize)
cv2.imshow('Croped Image', imgcrop)

print(img.shape)
print(imgResize.shape)
print(imgcrop.shape)
cv2.waitKey(0)