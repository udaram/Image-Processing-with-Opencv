"""
@Author 
Udaram Prajapat
This Few lines of code will take a image as input and will mark the 
faces of people inside the image and also counts the number of poples inside the image.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
face_cascade = cv2.CascadeClassifier("/home/udaram/Downloads/haarcascade_frontalface_default.xml")

#im_name='person.jpeg'
#im_name='2faceimage.jpeg'
#im_name = "program.jpg"
im_name='multiimage.jpg'

img=cv2.imread(im_name)
img=cv2.resize(img,(1600,1000))#for last image 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.3,5)
i=0
if len(faces)>0:
    print("No of people detected in the Image::",len(faces))   
    for (x,y,w,h) in faces:
        #uncomment the below code to take snapshots of faces
        """sub_face = img[y:y+h, x:x+w]
        face_file_name = "face_" + str(i) + ".jpg"
        #cv2.imwrite(face_file_name, sub_face)
        cv2.imshow(face_file_name, sub_face)
        i+=1"""
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)      
else :
    print("There is no person in the image") 
   
cv2.imshow('img',img)
    
cv2.waitKey(0)
cv2.destroyAllWindows() 
