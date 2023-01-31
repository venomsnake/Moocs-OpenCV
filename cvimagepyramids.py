#Image Pyramids Gaussian and Laplasican 

import cv2 as cv
import numpy as np

img = cv.imread("lena.jpg")
'''
	pyrDown and pyrUp methods

lr = cv.pyrDown(img)
lr1 = cv.pyrDown(lr)
hr = cv.pyrUp(img)

cv.imshow("Original Image", img)
cv.imshow("pyrDown", lr)
cv.imshow("Image", lr1)
cv.imshow("PyrUp", hr)
'''
layer = img.copy() #copy image from source
gp = [layer] #Gaussian pyramid 

for i in range(6):
	layer = cv.pyrDown(layer)
	gp.append(layer)
	#cv.imshow(str(i), layer)

'''laplacian'''
layer = gp[5]
cv.imshow("upper level ",layer)
lp = [layer]

for i in range(5, 0, -1):
	gaussian_extended = cv.pyrUp(gp[i])
	laplacian = cv.subtract(gp[i-1], gaussian_extended)
	cv.imshow(str(i), laplacian)
cv.waitKey(0)
cv.destroyAllWindows()