# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:31:30 2020

@author: ykrempp
"""


from skimage import io, img_as_float
import numpy as np
import cv2
import matplotlib.pyplot as plt

#import image and convert to float
img = io.imread('images/embryos_noisy.tif')
float_img =  img_as_float(img)

#build kernels
kernel =  np.ones((5,5), np.float32)/25

gaussian_kernel = np.array([[1/16, 1/8, 1/16],
                            [1/8, 1/4, 1/8],
                            [1/16, 1/8, 1/16]])

#filter images
conv_cv2_kernel = cv2.filter2D(float_img, -1, kernel, borderType=cv2.BORDER_CONSTANT)
conv_cv2_gaussian = cv2.filter2D(float_img, -1, gaussian_kernel, borderType=cv2.BORDER_CONSTANT)


#show results
fig = plt.figure(figsize = (20,20))

fig.add_subplot(3, 1, 1)
plt.title('original')
plt.imshow(float_img)

fig.add_subplot(3, 1, 2)
plt.title('kernel')
plt.imshow(conv_cv2_kernel)

fig.add_subplot(3, 1, 3)
plt.title('gaussian')
plt.imshow(conv_cv2_gaussian)