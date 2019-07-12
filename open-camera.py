import numpy as np
import cv2

cap = cv2.VideoCapture(0) # Using Camera

while(True):

    ret, frame = cap.read() #Reading Frame

    cv2.imshow('frame',frame)#Showing Frame

    if cv2.waitKey(20) & 0xFF == ord('q'):#Loop To Continue Showing Output
        break

cap.release()
cv2.destroyAllWindows()