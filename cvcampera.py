#set property to capture

import cv2 as cv

cap = cv.VideoCapture(0)
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

#via set method 3/4 are number of the parameter

cap.set(3, 1208)
cap.set(4,720)
print(cap.get(3))
print(cap.get(4))
while(cap.isOpened()):
	ret, frame = cap.read() # read stream of video frame

	if ret == True:

		gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
		cv.imshow('frame', frame)

		if cv.waitKey(1) == ord('q'):
			break
	else:
		break

cap.release()
cv.destroyAllWindows()