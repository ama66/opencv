import cv2 as cv

img1 = cv.imread('colored_balls.png')
img = cv.resize(img1, (700,700))
img_gry = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, thr = cv.threshold(img_gry, 235, 255, 0)
contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print('number of contours = ', str(len(contours)))
cv.drawContours(img, contours, -1, (0,0,255), 3)

cv.imshow('image', img_gry)
cv.imshow('img_colored', img)
cv.waitKey(0)
cv.destroyAllWindows
