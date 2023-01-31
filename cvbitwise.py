# Bitwise operations

import cv2 as cv
import numpy as np

img_1 = np.zeros((250, 500, 3), np.uint8)
img_2 = cv.rectangle(img_1,(200, 0), (300, 100), (255, 255, 255), -1)
img_3 = cv.imread("test.png")

#bit operations
bitAnd = cv.bitwise_and(img_2, img_1)
bitOr = cv.bitwise_or(img_2, img_1)
bitXor = cv.bitwise_xor(img_2, img_1)
bitNot = cv.bitwise_not(img_1)

cv.imshow('img1', img_1)
cv.imshow('img2', img_2)
cv.imshow('bitAnd', bitAnd)

cv.waitKey(0)
cv.destroyAllWindows()