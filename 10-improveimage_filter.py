import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

imgInit = cv.imread('color_balls.jpg')
# imgInit = cv.imread('afganG.jpg')

# create the kernel filter
kernel = np.ones((5,5), np.float32) / 25

img = cv.cvtColor(imgInit, cv.COLOR_BGR2RGB)
img_kernel = cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (5,5))
Gblur = cv.GaussianBlur(img, (5,5), 0)

img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
img_gray_kernel = cv.cvtColor(img_kernel, cv.COLOR_RGB2GRAY)
img_gray_blur = cv.cvtColor(blur, cv.COLOR_RGB2GRAY)
img_gray_Gblur = cv.cvtColor(Gblur, cv.COLOR_RGB2GRAY)

_, th = cv.threshold(img_gray_Gblur, 245, 255, cv.THRESH_BINARY_INV)
kernel2 = np.ones((5,5), np.float32)
imdilated1 = cv.dilate(th, kernel2, iterations=1)
imeroded = cv.erode(th, kernel2, iterations=2)
im_morph = cv.morphologyEx(th, cv.MORPH_OPEN, kernel2)
imdilated2 = cv.dilate(imeroded, kernel2, iterations=5)


images = [
          img_gray, img_gray_kernel, img_gray_blur, img_gray_Gblur, imdilated1, imdilated2, imeroded, im_morph]
titles = ['img_gray', 'img_gray_kernel', 'img_gray_blur', 'img_gray_Gblur', 'imdilated1', 'imdilated2', 'imeroded', 'im_morph']

for ii in range(8):
    print(ii)
    plt.subplot(2, 4, ii+1)
    plt.imshow(images[ii], 'gray')
    plt.title(titles[ii])
    plt.xticks([]), plt.yticks([])

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
