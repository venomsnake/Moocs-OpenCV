#Canny Edge 5 Step process

import cv2 as cv
import numpy as np
from matplotlib import pyplot as pp

img = cv.imread("messi.jpg", 0)
#img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
canny = cv.Canny(img, 100, 200)

titles = ['image', 'canny']
images=[img, canny]

for i in range(2):
	pp.subplot(1, 2, i+1), pp.imshow(images[i], 'gray')
	pp.title(titles[i])
	pp.xticks([]) ,pp.yticks([])

pp.show()