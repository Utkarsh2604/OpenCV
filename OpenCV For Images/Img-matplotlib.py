import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('goku.jpg',1)#import image

img = img[:,:,::-1]#to show image in rgb

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')#matplotlib 
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
