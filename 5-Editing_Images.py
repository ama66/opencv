import cv2 as cv
import numpy as np

img = np.zeros((700, 700, 3), np.uint8)

# cv.line(img, (0,0), (700, 700), (255,0,255), 1)
# cv.arrowedLine(img, (0, 0), (400, 400), (0, 0, 255), 3)
cv.rectangle(img, (600, 600), (400, 400), (0, 0, 255), -1)
cv.circle(img, (200, 200), 50, (0, 0, 255), -1)

font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'Dr. Ammar Abdilghanie', (100,100), font, 1, (255,255,255), 2, cv.LINE_AA)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows
