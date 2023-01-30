import cv2 as cv

# video from the camera

cap = cv.VideoCapture(0)

while(True):
	ret, frame = cap.read() # read stream of video frame

	cv.imshow('frame', frame)

	if cv.waitKey(1) == ord('q'):
		break;

cap.release()
cv.destroyAllWindows()