import cv2
import numpy as np
import matplotlib.pyplot as plt

#Reading th e image 
img = cv2.imread("watch.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',img)
cv2.waitKey(0)   #tape any key to destroy the window
cv2.destroyAllWindows()

"""
plt.imshow(img,interpolation='bicubic',cmap='gray')
plt.show()
"""
cv2.imwrite('watchgray.png',img)
