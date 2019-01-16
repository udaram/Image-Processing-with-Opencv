import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("/home/udaram/Downloads/haarcascade_frontalface_default.xml")
#videofile='output.mp4'
videofile="WhatsApp_Video.mp4"
cap =cv2.VideoCapture(videofile)

while True:
      ret,img=cap.read()
      gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray,1.3,5)
      for (x,y,w,h) in faces:
          cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
          
      cv2.imshow('img',img)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break

cap.release()
cv2.destroyAllWindows()
      
