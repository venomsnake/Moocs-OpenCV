'''Image scaling via matplotlib
'''

import cv2 as cv
from matplotlib import pyplot as pp
import numpy as np

'''img = cv.imread("test.png", -1)
cv.imshow("image", img)'''

img = cv.imread("gradient.png",0)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
	pp.subplot(2, 3, i+1), pp.imshow(images[i], 'gray')
	pp.title(titles[i])

'''conversion from bgr to rgb
'''
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

pp.imshow(img)
#pp.xticks([]), pp.yticks([]) #hide the y and x ticks
pp.show()

cv.waitKey(0)
cv.destroyAllWindows()
