import cv2 as cv
import numpy as np

#draw circles and connect them 
def click_event(event, x, y, flags, param):
	if event == cv.EVENT_LBUTTONDOWN:
		cv.circle(img, (x, y),3, (0, 0, 255), -1)
		points.append((x, y))
		if len(points) >=2:
			#-1 last element of array and -2 second last
			cv.line(img, points[-1], points[-2], (255, 0, 0), 5)
		cv.imshow('image', img)
		

#image creation 
img = np.zeros((512, 512, 3), np.uint8)
cv.imshow('image', img)

points = []

cv.setMouseCallback('image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()