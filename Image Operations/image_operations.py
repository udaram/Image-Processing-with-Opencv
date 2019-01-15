import cv2
import numpy as np
import matplotlib.pyplot as plt

#Reading th e image 
img = cv2.imread("watch.jpg",cv2.IMREAD_COLOR)
img[55,55]=[25,124,178]
px = img[55,55]
print(px)

"""
#ROI of image(reagion of image)
roi = img[100:150,100:150]
plt.imshow(roi)
plt.show()
"""

#roi = img[100:150,100:150]=[232,34,56]

watch_face=img[152:392,104:305]
img[0:240,0:201]=watch_face
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()











