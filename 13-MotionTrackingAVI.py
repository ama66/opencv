import cv2 as cv

cap = cv.VideoCapture('vtest.avi')   # 1- capture the video

ret, frame1 = cap.read()
ret, frame2 = cap.read()    # 2- reading the the video frame through two channels
# start a while loop to take the difference in video frames
while cap.isOpened():
    try:

        # 3- take the difference between the two frames
        diff = cv.absdiff(frame1, frame2)
        # 4- mark the difference in grayscale
        gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
        # 5- Using a kernel filter with gaussian distribution
        blur = cv.GaussianBlur(gray, (5, 5), 0)
        # threshold on grayscale to tune motion detection
        _, thr = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
        # TO FILTER THE UNWANTED CONTOURS INSIDE THE RESULT
        dilated = cv.dilate(thr, None, iterations=3)
        # find the contours resulted from frames substraction
        contours, _ = cv.findContours(
            dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        # cv.drawContours(frame1, contours, -1, (255,0,0), 2) # draw all contours
        # *********This section to adjust the tracking boundaries to a rectangle..............
        for contour in contours:
            (x,y,w,h) = cv.boundingRect(contour)
            if cv.contourArea(contour) > 900:
                cv.rectangle(frame1, (x, y), (x+w, y+h), (255, 0, 0), 1)
            else:
                continue

        # *********This section to adjust the tracking boundaries to a rectangle..............
        cv.imshow('motion_track', frame1)
        frame1 = frame2
        # frame 2 is is captured after the first frame with time mentioned in waitkey()
        ret, frame2 = cap.read()
        K = cv.waitKey(40)
        if K == 27:
            break
    except:
        print('no more video frames')
        break
cv.destroyAllWindows()
