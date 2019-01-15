import cv2
import numpy as np

img1 = cv2.imread('image.jpeg')
img2 = cv2.imread('logo.png')
img1=cv2.resize(img1,(200,200))
img2=cv2.resize(img2,(200,200))
add = img1+img2
#add = cv2.(img1,img2)
cv2.imshow('add',add)
#weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)
#cv2.imshow('Weighted',weighted)

cv2.waitKey(0)
cv2.destroyAllWindows()

