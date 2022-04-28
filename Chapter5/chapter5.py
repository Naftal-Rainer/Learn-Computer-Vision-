import cv2
import numpy as np

img = cv2.imread('../Resources/card.jpg')

width,height = 192,316
pts1 = np.float32([[343,40],[342,440],[616,40],[618,442]])
pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow('Card',img)
cv2.imshow('Output',imgOutput)
print(img.shape)
cv2.waitKey(0)