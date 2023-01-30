#Geometry shapes on images/outlines 
import cv2 as cv
import numpy as np

#img = cv.imread('test.png',-1)

#Image using numpy
#height width 

img = np.zeros([512, 512, 3], np.uint8)


#draw line with lines method
#(image, starting pt ending pt, color, thickness)

img = cv.line(img, (0,0),(255,255), (255, 0, 0), 5)
img = cv.arrowedLine(img, (0,0),(255,255), (255, 0, 0), 5)

img = cv.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)
img = cv.circle(img, (447, 63), 63, (0, 255, 0), -1)
fontf = cv.FONT_HERSHEY_SIMPLEX
img = cv.putText(img, "Test", (255,100),fontf, 4, (255, 255, 255), 10, cv.LINE_AA)

cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()