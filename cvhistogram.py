# intensity

import cv2 as cv
import numpy as np
from matplotlib import pyplot as pp

#img = np.zeros((200, 200), np.uint8)
#cv.rectangle(img, (0, 100), (200,200), (255), -1)

img = cv.imread("test.png")

b, g, r = cv.split(img)

cv.imshow("img", img)
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)

pp.hist(img.ravel(), 256, [0, 256])
pp.show()

#calcHist

hist = cv.calcHist([img], [0], None, [256], [0, 256])
pp.plot(hist)

cv.waitKey(0)
cv.destroyAllWindows()