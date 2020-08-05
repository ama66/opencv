import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('gradient_grayscale.jpg')
threshold_var = 80
_, th1 = cv.threshold(img, threshold_var, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, threshold_var, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, threshold_var, 255, cv.THRESH_TOZERO)
_, th4 = cv.threshold(img, threshold_var, 255, cv.THRESH_TOZERO_INV)


images = [img, th1, th2, th3, th4]
titles =['Original', 'Binary', 'BinaryINV', 'tozero', 'tozeroINV']

for ii in range(5):
    print(ii)
    plt.subplot(2,3,ii+1)
    plt.imshow(images[ii], 'gray')
    plt.title(titles[ii])
    plt.xticks([]), plt.yticks([])

plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
