# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:59:27 2019

@author: ykrempp
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


img_path = 'images\qupath_image.tif'


                     
img = cv2.imread(img_path, 0)

scale_percent = 25 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height) 

img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

eq_img = cv2.equalizeHist(img)

clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize=(8,8))
cl_img = clahe.apply(img)

cv2.imshow("original", img)
cv2.imshow("equalized", eq_img)
cv2.imshow("CLAHE", cl_img)

plt.hist(cl_img.flat, bins=100)

ret, thresh1 = cv2.threshold(cl_img, 50, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(cl_img, 100, 255, cv2.THRESH_BINARY)
otsu_thresh, thresh3 = cv2.threshold(cl_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow("Threshold 1", thresh1)
cv2.imshow("Threshold 2", thresh2)
cv2.imshow("OTSU", thresh3)


cv2.waitKey(0)
cv2.destroyAllWindows()