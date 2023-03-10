#Template matching

import cv2 as cv
import numpy as np

img = cv.imread("messi.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

template = cv.imread("messi-t.jpg", 0)

w, h = template.shape[::-1]

res = cv.matchTemplate(gray, template, cv.TM_CCOEFF_NORMED)
print(res)
#filtering the array points with threshold to get exact value
threshold = 0.96
loc = np.where(res >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
	cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()