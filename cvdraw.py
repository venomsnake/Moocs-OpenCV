#set property to capture and show current date time

import cv2 as cv
import datetime

cap = cv.VideoCapture(0)
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

'''#via set method 3/4 are number of the parameter

cap.set(3, 1208)
cap.set(4,720)
print(cap.get(3))
print(cap.get(4))'''

while(cap.isOpened()):
	ret, frame = cap.read() # read stream of video frame

	if ret == True:
		fontf = cv.FONT_HERSHEY_SIMPLEX
		#frame will hold the data 
		datet = str(datetime.datetime.now())
		txt = 'Width: '+ str(cap.get(3)) + 'Height:' + str(cap.get(4))
		frame = cv.putText(frame, datet, (10,50), fontf, 1, (0,255,255),2,cv.LINE_AA)
		cv.imshow('frame', frame)

		if cv.waitKey(1) == ord('q'):
			break
	else:
		break

cap.release()
cv.destroyAllWindows()