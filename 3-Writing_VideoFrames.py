import cv2 as cv

## opening videocapture
cap = cv.VideoCapture(0)

## some videowriter props
sz = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))

fps = 20
#fourcc = cv.VideoWriter_fourcc('m', 'p', '4', 'v')
#fourcc = cv.VideoWriter_fourcc('m', 'p', 'e', 'g')
fourcc = cv.VideoWriter_fourcc(*'mp4v')

## open and set props
vout = cv.VideoWriter()
vout.open('output.mp4',fourcc,fps,sz,True)

cnt = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frames")
        break
    frame=cv.flip(frame,0)
    vout.write(frame)
    cv.imshow("colored video",frame)
    if cv.waitKey(1)==ord("q"):
        break

    

vout.release()
cap.release()

