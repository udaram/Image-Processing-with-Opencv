import cv2
import numpy as np

cap = cv2.VideoCapture(0)#0,1 ,2 specify camera no.
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4',fourcc,20.0,(640,480))

while True :
      ret,frame = cap.read()
      
      #to convert color to gray
      gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      out.write(frame)
      cv2.imshow('Gray',gray)
      cv2.imshow('frame',frame)
      
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
    
cap.release()
out.release()
cv2.destroyAllWindows()
