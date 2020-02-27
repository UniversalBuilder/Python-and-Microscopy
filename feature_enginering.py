# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:10:33 2020

@author: ykrempp
"""

import cv2
from skimage.filters.rank import entropy
from skimage.filters import gaussian, hessian, sobel
from skimage.morphology import disk
import pandas as pd
import matplotlib.pyplot as plt

#get the image
print('Getting image...')
img = cv2.imread('images/bf_series.tif')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#build features
print('Building features ...')
entropy_img = entropy(img, disk(1))
gaussian_img = gaussian(img, sigma=5)
hessian_img = hessian(img)
sobel_img = sobel(img)

#show images
# cv2.imshow('entropy', entropy_img)
# cv2.imshow('hessian', hessian_img)
# cv2.imshow('gaussian', gaussian_img)
# cv2.imshow('sobel', sobel_img)
# cv2.imshow('original', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

#convert images into 1D array

print('Reshaping the data...')
img_unwrapped = img.reshape(-1)
entropy_unwrapped = entropy_img.reshape(-1)
gaussian_unwrapped = gaussian_img.reshape(-1)
hessian_unwrapped = hessian_img.reshape(-1)
sobel_unwrapped = sobel_img.reshape(-1)

#create the DataFrame
df = pd.DataFrame()

# Put the feature data into the Dataframe
print('Putting everything in a nice table...')
df['original_px'] = img_unwrapped
df['entropy_px'] = entropy_unwrapped
df['gaussian_px'] = gaussian_unwrapped
df['hessian_px'] = hessian_unwrapped
df['sobel_px'] = sobel_unwrapped

# data is now ready for ML
print('ML starts now (KMeans)...')
from sklearn.cluster import KMeans

km = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
model = km.fit(df)
print('ML finished !')
predictions = km.predict(df)

#show the results
print('Here is the segmentation: ')
segmented = predictions.reshape(img.shape)
plt.imshow(segmented)