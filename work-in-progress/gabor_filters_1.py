# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:43:36 2020

@author: ykrempp
"""


import numpy as np
import cv2
import matplotlib.pyplot as plt

#gabor is a bandpass filter

#parameters (allow to generate a large set of features)

ksize = 5 #depends on the feature size you want to enhance
sigma = 5
theta = 1*np.pi/4 # orientation of the filter
lambd = 1*np.pi/4 # wavelenght
gamma = 0.5 # aspect ratio, circular = 1, elongated = 0
phi = 0 #offset

kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lambd, gamma, phi, ktype=cv2.CV_32F)

fig = plt.figure(figsize=(40,40))
cols = 2
rows = 2
fig.add_subplot(rows, cols, 1)
plt.title('kernel')
plt.imshow(kernel)

#get an image

img = cv2.imread('images/test_chart.jpg')
fig.add_subplot(rows, cols, 2)
plt.title('original')
plt.imshow(img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
filtered_img = cv2.filter2D(img, cv2.CV_8UC3, kernel)

fig.add_subplot(rows, cols, 3)
plt.title('filtered')
plt.imshow(filtered_img, cmap='gray') 

plt.show()