import numpy as np
import cv2

cap = cv2.VideoCapture('video.avi')#Video Location

while(True):
    ret, frame = cap.read()

    cv2.imshow('video',frame)
    if cv2.waitKey(25)  & 0xFF == ord('q'):#in waitkey adjust values accordingly
        break

cap.release()
cv2.destroyAllWindows()