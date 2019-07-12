import numpy as np
import cv2

cap = cv2.VideoCapture(0)

"""# Standard Video Dimensions Sizes
STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),    \\YOUR WEBCAM SHOULD SUPPORT RESOLUTION
    "1080p": (1920, 1080),   \\AFTER 1080P
    "4k": (3840, 2160),
}
"""

def change_res(width, height):#Defines Resoultion(3,4 are default parameters)
    cap.set(3, width)
    cap.set(4, height)

change_res(1280, 720)#change values here

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('c'):
        break

cap.release()
cvw.destoryAllWindows()

##############################  USE "C" BUTTON TO EXIT  ################################
