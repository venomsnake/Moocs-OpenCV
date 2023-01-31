'''object detection and tracking in Images
'''
import cv2 as cv
import numpy as np

def nothing(x):
	pass

'''Trackbar will help to adjust color hsv
	track bar for all lower and upper hsv values
	'''
cv.namedWindow("Tracking")
cv.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv.createTrackbar("US", "Tracking", 255, 255, nothing)
cv.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
	frame = cv.imread('smarties.png')
	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV) #color conversion

	'''#threshold hsv

	l_b = np.array([110, 50, 50])
	u_b = np.array([130, 255, 255])

	mask = cv.inRange(hsv, l_b, u_b)

	res = cv.bitwise_and(frame, frame, mask=mask)'''
	l_h = cv.getTrackbarPos("LH", "Tracking")
	l_s = cv.getTrackbarPos("LS", "Tracking")
	l_v = cv.getTrackbarPos("LV", "Tracking")

	u_h = cv.getTrackbarPos("UH", "Tracking")
	u_s = cv.getTrackbarPos("US", "Tracking")
	u_v = cv.getTrackbarPos("UV", "Tracking")


	l_b = np.array([l_h, l_s, l_v])
	u_b = np.array([u_h, u_s, u_v])

	mask = cv.inRange(hsv, l_b, u_b)

	cv.imshow("frame", frame)
	cv.imshow("mask", mask)
	cv.imshow("frame", frame)

	key = cv.waitKey(1)
	if key == 27:
		break

cv.destroyAllWindows()