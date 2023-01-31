import cv2 as cv
import numpy as np
from matplotlib import pyplot as pp

img = cv.imread("smarties.png", cv.IMREAD_GRAYSCALE)

titles = ['image']
images=[img]

for i in range(1):
	pp.subplot(1, 1, i+1), pp.imshow(images[i], 'gray')
	pp.title(titles[i])
	pp.xticks([]) ,pp.yticks([])

pp.show()