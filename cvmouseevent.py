import cv2 as cv
import numpy as np
'''
Lists all the events:

events = [i for i in dir(cv) if 'EVENT' in i]
print(events)
'''
#mouse event
def click_event(event, x, y, flags, param):
	if event == cv.EVENT_LBUTTONDOWN:
		print(x,', ', y)
		fontf = cv.FONT_HERSHEY_SIMPLEX
		str_group = str(x) + ','+ str(y)
		cv.putText(img, str_group, (x, y), fontf, 1, (255, 255, 0), 2)
		cv.imshow('image', img)

	if event == cv.EVENT_RBUTTONDOWN:
		#print bgr channel
		blue = img[y, x, 0]
		green = img[y, x, 1]
		red = img[y, x, 2]
		fontf = cv.FONT_HERSHEY_SIMPLEX
		str_group = str(blue) + ','+ str(green)+ ','+ str(red)
		cv.putText(img, str_group, (x, y), fontf, 1, (255, 255, 0), 2)
		cv.imshow('image', img)

'''#image creation 
img = np.zeros((512, 512, 3), np.uint8)
cv.imshow('image', img)
'''
img = cv.imread('test.png')
cv.imshow('image', img)
cv.setMouseCallback('image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()