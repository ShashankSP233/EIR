#Use to record and store a video 

import numpy as ny  #importing numpy library
import cv2  #importing cv2 library

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')    #writer object
'''
   Name of File : Video_Output.mp4     
   Frame per second (fps) : 30        
   Resolution : 845,480
'''
out = cv2.VideoWriter("Video_Output.mp4",fourcc,30.0,(845,480))

while (cap.isOpened()):
    ret, frame = cap.read()
    if (ret==True):
        out.write(frame)    #write frame if capture
        cv2.imshow('Output',frame)
        if(cv2.waitKey(1) & 0XFF == ord('q')): 
            #if user press the key 'q' the video will end 
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
