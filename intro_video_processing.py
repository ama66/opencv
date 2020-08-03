#
import cv2 as cv 
import numpy as np 
# if terminal does not appear amongst the apps allowed to access your camera
## issue these commands 
# https://apple.stackexchange.com/questions/360851/add-access-to-the-macbook-camera-for-the-terminal-application
# I used the following commands (these are meant to click a picture from your MacBook's camera):

# ffmpeg -f avfoundation -list_devices true -i ""

# List the devices attached to your computer. Get the device ID of your camera

# ffmpeg -ss 0.5 -f avfoundation -i "0" -t 1 capture.jpg

# Capture the photo.



cap=cv.VideoCapture(0)

print(cap.isOpened())

if cap is False:
    print("Cannot access the camera")
    exit()
while True:
    ret,frame=cap.read()
    if ret is False:
        print("Cannot recover frames")
        break
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # cv.imshow("frame_gray",gray)
    cv.imshow("colored video",frame)
    if cv.waitKey(1)==ord("q"):
        break


cap.release()
cv.destroyAllWindows()

