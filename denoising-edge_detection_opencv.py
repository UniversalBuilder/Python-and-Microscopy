# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 14:50:19 2019

@author: ykrempp
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

path = "S:/CloudStation/2_Personnel/2.1_Cours/2.1.4_Python/images/"

img = cv2.imread(path+"embryos_clean_rgb.tif", 0)
kernel = np.ones((3,3), np.float32)/9

filt_2D = cv2.filter2D(img, -1, kernel)

blur = cv2.blur(img, (3,3))

gaussian_blur = cv2.GaussianBlur(img, (3,3), 0)

median_blur = cv2.medianBlur(img, 3)

bilateral_blur = cv2.bilateralFilter(img, 9, 75, 75)

edges = cv2.Canny(img, 50, 150)


cv2.imshow("original", img)
#cv2.imshow("2D custom filter", filt_2D)
#cv2.imshow("Blur", blur)
cv2.imshow("Gaussian blur", gaussian_blur)
cv2.imshow("Median filter", median_blur)
cv2.imshow("Bilateral filter", bilateral_blur)
cv2.imshow("Canny Edges", edges)




cv2.waitKey(0)
cv2.destroyAllWindows()