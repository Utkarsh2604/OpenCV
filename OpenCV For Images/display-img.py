import numpy as np
import cv2

img = cv2.imread('goku.jpg', 1)   #  imporing image

cv2.imshow('image',img)  #showing images 

k = cv2.waitKey(0) 

##### Press any Key TO close #########