# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 14:58:11 2020

@author: ykrempp
"""


import numpy as np
import cv2

img = cv2.imread('images/embryos_rgb.tif')
img2 = img.reshape((-1,3))

# convert to np.float32
img3 = np.float32(img2)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 1.0)
K = 3
ret,label,center=cv2.kmeans(img3,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('res2',res2)
cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
