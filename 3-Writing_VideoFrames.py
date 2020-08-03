#

import cv2 as cv 
import numpy as np 


cap=cv.VideoCapture(0)
# you could also read existing video file xx.avi 
# and process it e.g. flip it, cv.VideoCapture('xx.avi') where xx.avi is in the same directory

# print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# # width 1280.0
# # Height 720.0

# cap.set(cv.CAP_PROP_FRAME_WIDTH,450)
# cap.set(cv.CAP_PROP_FRAME_HEIGHT,300)

# print("New Dimensions \n")
# print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# width 640.0
# Height 480.0

## Define Codec for generated video 

fourcc=cv.VideoWriter_fourcc(*'XVID')
## Filename is output.avi 

out=cv.VideoWriter('output.avi',fourcc,20 , (640,480),True ) 
## 20 frame per sec, size, corlor=True

while cap.isOpened():

    ret,frame=cap.read()

    if not ret:
        print("Cannot receive frames")
        break

    frame=cv.flip(frame,0)
    out.write(frame)
    cv.imshow("colored video",frame)
    if cv.waitKey(1)==ord("q"):
        break
    

cap.release()
out.release()
cv.destroyAllWindows()




