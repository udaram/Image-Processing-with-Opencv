#WEBCAM REALTIME READ
import cv2
import  numpy as np
import matplotlib.pyplot as plt


cap = cv2.VideoCapture('video.avi')

face_cascade = cv2.CascadeClassifier('car.xml')

count=0

while True:
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#creates a frame with gray layer)
    faces = face_cascade.detectMultiScale(gray, 1.1, 1) 
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
        count+=1
    cv2.putText(frame, str(count),(10,400), cv2.FONT_ITALIC, 2,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow('frame',frame)
   
    if cv2.waitKey(1) & 0xFF==ord('q'):#if wait key is not declared the frame is opened but not seen.
        break
print(count)
cap.release()
cv2.destroyAllWindows()
