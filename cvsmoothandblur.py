#smooth and blurry

import cv2 as cv
import numpy as np
from matplotlib import pyplot as pp

img = cv.imread("opencv-logo.png")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25

dst = cv.filter2D(img, -1, kernel)

blur = cv.blur(img, (5,5))

gaussianb = cv.GaussianBlur(img, (5,5), 0) #removes high frequency noise

median = cv.medianBlur(img, 5) #kernel size as odd

bilateral_filter = cv.bilateralFilter(img, 9, 75, 75) #keeps the sharp edges

titles = ['image', 'dst', 'blur', 'Gaussian', 'salt&paper', 'bilateralFilter']
images=[img, dst, blur, gaussianb, median, bilateral_filter]

for i in range(6):
	pp.subplot(3, 3, i+1), pp.imshow(images[i], 'gray')
	pp.title(titles[i])
	pp.xticks([]) ,pp.yticks([])

pp.show()