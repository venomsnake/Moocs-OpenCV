import cv2 as cv
import numpy as np

# create a black image 
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

while(1):

	cv.imshow('image', img)
	k = cv.waitKey(1)
	if k == 27:
		break

cv.destroyAllWindows()