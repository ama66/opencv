import cv2 as cv 
#print(cv.__version__)
path="/Users/ammar/opencv-samples/data/"
image=cv.imread(path+"aloeL.jpg",-1) # 0 grey -1 colored
image2=cv.imread(path+"butterfly.jpg")
#cv.imshow("new image",image)
# print("image 1 ...\n", image.size)
# print(image.shape)
# print(image.dtype,"\n image two...")

# print(image2.size)
# print(image2.shape)
# print(image2.dtype)

image_12 = cv.resize(image,(512,512))
image_22 = cv.resize(image2,(512,512))

print("image 1 ...\n", image.size)
print(image.shape)
print(image.dtype,"\n image two...")

print(image2.size)
print(image2.shape)
print(image2.dtype)
cv.imshow("new image",image_12)
cv.imshow("new image2",image_22)


cv.waitKey(5000) # number in millisec
cv.destroyAllWindows()

# k=cv.waitKey(0) # number in millisec
# if k ==27:  ## is you press Escape 
#     cv.destroyAllWindows()
# elif k==ord("s"):
#     cv.imwrite(path+"AmmarGrey.jpg",image)
#     cv.destroyAllWindows()

