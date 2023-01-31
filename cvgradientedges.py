#gradient and edge detection

import cv2 as cv
import numpy as np
from matplotlib import pyplot as pp

img = cv.imread("messi.jpg", cv.IMREAD_GRAYSCALE)
#img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

#laplacian method
lap = cv.Laplacian(img, cv.CV_64F, ksize = 3)
lap =np.uint8(np.absolute(lap))

#sobelx
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0) #change in intensity in X dir
sobely = cv.Sobel(img, cv.CV_64F, 0, 1) #change in intensity in Y dir
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

sobelcombined = cv.bitwise_or(sobely, sobelx)

titles = ['image','Laplacian', 'SobelX', 'SobelY', 'sobelcombined']
images=[img, lap, sobelx, sobely, sobelcombined]

for i in range(4):
	pp.subplot(2, 2, i+1), pp.imshow(images[i], 'gray')
	pp.title(titles[i])
	pp.xticks([]) ,pp.yticks([])

pp.show()