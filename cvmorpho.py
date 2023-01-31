import cv2 as cv
import numpy as np
from matplotlib import pyplot as pp

img = cv.imread("smarties.png", cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

'''dilation transformation to hide black dot with white kernal'''
kernal = np.ones((3,3), np.uint8) #square shape kernal
dilation = cv.dilate(mask,kernal, iterations=2)

'''erosion transformation
'''
erosion = cv.erode(mask, kernal, iterations=1)

opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal) #erosion then dialation

closeing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening']
images=[img, mask, dilation, erosion, opening]

for i in range(5):
	pp.subplot(2, 3, i+1), pp.imshow(images[i], 'gray')
	pp.title(titles[i])
	pp.xticks([]) ,pp.yticks([])

pp.show()