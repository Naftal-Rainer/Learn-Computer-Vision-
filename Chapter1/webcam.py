import cv2

# Displaying Video

cap = cv2.VideoCapture(0)  # Set camera ID
cap.set(3,640)             # Set video width
cap.set(4,480)             # Set video height
cap.set(10,100)            # Set brightness

while True:
    success, img = cap.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break