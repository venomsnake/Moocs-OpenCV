import cv2 as cv

#read image
img = cv.imread('test.png',1) #flag 0, 1, -1

print(img)

#display

cv.imshow('image',img)

cv.waitKey(5000) #delays the fade off the window

cv.destroyAllWindows() #destroys all the windows

#WRITE image

cv.imwrite('testcopy.jpg',img)
