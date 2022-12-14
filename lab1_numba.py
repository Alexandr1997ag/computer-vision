import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import numba
from numba import cuda
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
@numba.jit
def numba_hist():
    img = cv.imread("/media/alex/One Touch/учеба/комп зрение/lab1/12.jpg")
    cv.imshow("before", img)
    plt.hist(img.ravel(), 256, [0,256])
    plt.show()
    cv.destroyAllWindows()
    # split g,b,r
    g = img[:,:,0]
    b = img[:,:,1]
    r = img[:,:,2]

    # calculate hist
    hist_r, bins_r = np.histogram(r, 256)
    hist_g, bins_g = np.histogram(g, 256)
    hist_b, bins_b = np.histogram(b, 256)

    # calculate cdf
    cdf_r = hist_r.cumsum()
    cdf_g = hist_g.cumsum()
    cdf_b = hist_b.cumsum()

    # remap cdf to [0,255]
    cdf_r = (cdf_r-cdf_r[0])*255/(cdf_r[-1]-1)
    cdf_r = cdf_r.astype(np.uint8)# Transform from float64 back to unit8
    cdf_g = (cdf_g-cdf_g[0])*255/(cdf_g[-1]-1)
    cdf_g = cdf_g.astype(np.uint8)# Transform from float64 back to unit8
    cdf_b = (cdf_b-cdf_b[0])*255/(cdf_b[-1]-1)
    cdf_b = cdf_b.astype(np.uint8)# Transform from float64 back to unit8

    # get pixel by cdf table
    r2 = cdf_r[r]
    g2 = cdf_g[g]
    b2 = cdf_b[b]

    # merge g,b,r channel
    img2 = img.copy()
    img2[:,:,0] = g2
    img2[:,:,1] = b2
    img2[:,:,2] = r2

    # show img after histogram equalization
    cv.imshow("img2", img2)
    plt.hist(img2.ravel(), 256, [0,256])
    plt.show()
    cv.destroyAllWindows()

numba_hist()