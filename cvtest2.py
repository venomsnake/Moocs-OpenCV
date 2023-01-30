import cv2 as cv

# video from the camera

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')

out = cv.VideoWriter("out.avi", fourcc, 20.0,  (640,480)) #save the frames
# parameters out_file name, fourcc codec, framespersecond, size of the frame

print(cap.isOpened())

while(True):
	ret, frame = cap.read() # read stream of video frame

	#change input stream color

	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	if ret == True:
		print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
		print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

		out.write(frame)

		cv.imshow('frame', frame)

		if cv.waitKey(1) == ord('q'):
			break;
	else:
		break

cap.release()
out.release()
cv.destroyAllWindows()