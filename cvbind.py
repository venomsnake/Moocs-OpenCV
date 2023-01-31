#Trackbars 
import cv2 as cv
import numpy as np

def nothing(x):
	print(x)

# create a black image 
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

#track bar
cv.createTrackbar('B', 'image', 0, 255, nothing)
# name, frame, start, end , callback method
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

#switch via track bar

switch = 'O : OFF\n 1: ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):

	cv.imshow('image', img)
	k = cv.waitKey(1)
	if k == 27:
		break

	#get trackbar pos for manipulation
	b = cv.getTrackbarPos('B', 'image')
	g = cv.getTrackbarPos('G', 'image')
	r = cv.getTrackbarPos('R', 'image')
	s = cv.getTrackbarPos(switch, 'image')
	if s == 0:
		img[:] = 0

	img[:] = [b, g, r] #changes the image's b g r to the trackbar 

cv.destroyAllWindows()