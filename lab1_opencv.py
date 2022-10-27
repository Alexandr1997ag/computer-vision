import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np




im = cv.imread("12.jpg")
cv.imshow("before", im)
plt.hist(im.ravel(), 256, [0,256])
plt.show()
cv.destroyAllWindows()

# split g,b,r
g = im[:,:,0]
b = im[:,:,1]
r = im[:,:,2]


# Histogram Equalization
r2 = cv.equalizeHist(r)
g2 = cv.equalizeHist(g)
b2 = cv.equalizeHist(b)

im2 = im.copy()
im2[:,:,0] = g2
im2[:,:,1] = b2
im2[:,:,2] = r2

plt.hist(im2.ravel(), 256, [0, 256])
cv.imshow("before", im2)
plt.show()
cv.destroyAllWindows()

