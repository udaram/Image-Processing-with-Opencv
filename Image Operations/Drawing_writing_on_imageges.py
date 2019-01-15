import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)

#to draw line on image
cv2.line(img,(0,0),(150,150),(25,105,205),10)

#for rectangle
cv2.rectangle(img,(15,25),(200,150),(100,50,255),5)  #-5 wil fill color inside the rect..
#for circle
cv2.circle(img,(100,63),55,(50,255,100),3)

#polygone
points = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
cv2.polylines(img,[points],True,(0,255,255),3)

#to put text on image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'IIT Jammu',(380,480),font,1,(20,100,50),3,cv2.LINE_AA)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
