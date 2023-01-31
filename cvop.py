import cv2 as cv

img = cv.imread("messi.jpg")
img2 = cv.imread("test.png")

print(img.shape) # returns a tuple with number of rows col and channel
print(img.size) #returns total pixels
print(img.dtype) #returns Image datatype

b,g,r = cv.split(img)
img = cv.merge((b,g,r))

'''ball = img[230:340, 330:390] # ball coordinates and copy
img[273:333, 110:160] = ball #paste the coordinate of balls in coordinates of image
'''
#Resize images for add

img = cv.resize(img, (512,512))
img2 = cv.resize(img2, (512,512))

new_image = cv.add(img, img2)

cv.imshow('image', new_image) #overlapping

#cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()

'''addWeighted(sc1, weight1, scr2, weight2,gama)