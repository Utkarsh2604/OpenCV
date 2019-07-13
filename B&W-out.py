import numpy as np
import cv2

cap = cv2.VideoCapture(0) # Using Camera

while(True):

    ret, frame = cap.read() #Reading Frame

    bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#B&W frame


    cv2.imshow('frame',frame)#Showing Frame

    cv2.imshow('frame1',bw)#Showing B&w Frame


    if cv2.waitKey(20) & 0xFF == ord('x'):#Loop To Continue Showing Output
        break

cap.release()
cv2.destroyAllWindows()

"""Use 'x' Button to Quit"""
