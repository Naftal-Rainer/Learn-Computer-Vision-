import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

# img[200:300, 100:300] = 255,0,0
# print(img.shape)

# Creating Lines

cv2.line(img,(0,0),(300,300),(0,255,0),3)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(2,10,125),2)

# Creating Rectangle

cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.rectangle(img,(250,350),(512,512),(0,0,255),cv2.FILLED)


# Creating Circles

cv2.circle(img, (400,50), 30, (255,255,0),5)

# Adding Texts to Images

cv2.putText(img, "Opencv ", (300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
cv2.putText(img, "Rainer ", (300,500),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)

cv2.imshow('Image', img)
cv2.waitKey(0)
