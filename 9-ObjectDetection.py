import numpy as np
import cv2 as cv

def output(x):
    pass
cv.namedWindow('Tracking')

# create the trackbars
cv.createTrackbar('LH', 'Tracking', 0, 255, output)
cv.createTrackbar('LS', 'Tracking', 0, 255, output)
cv.createTrackbar('LV', 'Tracking', 0, 255, output)
cv.createTrackbar('UH', 'Tracking', 255, 255, output)
cv.createTrackbar('US', 'Tracking', 255, 255, output)
cv.createTrackbar('UV', 'Tracking', 255, 255, output)

# loop for masking and detection
while(1):
    frame = cv.imread('colored.jpeg')
    newframe = cv.resize(frame, (512,512))
##Convert from BGR to HSV color-space
    hsv = cv.cvtColor(newframe, cv.COLOR_BGR2HSV)
    print(hsv)
    l_h = cv.getTrackbarPos('LH', 'Tracking')
    l_s = cv.getTrackbarPos('LS', 'Tracking')
    l_v = cv.getTrackbarPos('LV', 'Tracking')

    u_h = cv.getTrackbarPos('UH', 'Tracking')
    u_s = cv.getTrackbarPos('US', 'Tracking')
    u_v = cv.getTrackbarPos('UV', 'Tracking')

    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])
    mask = cv.inRange(hsv, lower_bound, upper_bound)
    resulted_img = cv.bitwise_and(newframe, newframe, mask=mask)

    cv.imshow('newframe', newframe)
    cv.imshow('mask', mask)
    cv.imshow('result', resulted_img)

    k = cv.waitKey(1)
    if k == 27:
        break

cv.destroyAllWindows()
