# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:17:47 2020

@author: ykrempp
"""

import numpy as np
import cv2

#get the image
img = cv2.imread('images/TEM_filter_sample.jpg')

#format the image to one column
img2 = img.reshape((-1,3))

#define and fit the model
from sklearn.mixture import GaussianMixture as GMM

gmm_model = GMM(n_components=2, covariance_type='tied').fit(img2)

#get the labels with the predictions
gmm_labels = gmm_model.predict(img2)

#turn the labels bakc into an image
original_shape = img.shape
segmented = gmm_labels.reshape(original_shape[0], original_shape[1])

#save the image as tiff (will be binary, needs brightness contrast adjustment)

cv2.imwrite('segmented_gmm.tif', segmented)

#use aic or bic to determine the right number of parameters

comp_range = np.arange(1,10)

gmm_models = [GMM(n_components=n, covariance_type='tied').fit(img2) for n in comp_range]

#plot the results

import matplotlib.pyplot as plt

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20,10))
ax[0].plot(comp_range, [m.bic(img2) for m in gmm_models], c='red', marker='+')
ax[1].plot(comp_range, [m.aic(img2) for m in gmm_models], c='blue', ls='--', marker='o')
ax[0].set(title='BIC', xlabel='components', ylabel='penalty')
ax[1].set(title='AIC', xlabel='components', ylabel='penalty')
#

# NOTE: I was alerted by one of the viewers that m.bic part needs more explanation so here it is. Both BIC and AIC are included as built in methods as part of Scikit-Learn's  GaussianMixture. Therefore we do not need to import any other libraries to compute these. The way you compute them (for example BIC) is by fitting a GMM model and then calling the method BIC. In the video I tried to achieve multiple things in one single line, compute BIC for each GMM calculated by changing number of components and also to plot them. Let me elaborate...

# Instead of changing number of components in a loop let us compute one at a time, for example let us define n = 2. Then fit a gmm model for n=2 and then calculate BIC. The code would look like ...

# import numpy as np

# import cv2



# img = cv2.imread("alloy.jpg")

# img2 = img.reshape((-1,3))



# from sklearn.mixture import GaussianMixture as GMM



# n = 2

# gmm_model = GMM(n, covariance_type='tied').fit(img2)
# #The above line generates GMM model for n=2
# #Now let us call the bic method (or aic if you want).

# bic_value = gmm_model.bic(img2)  #Remember to call the same model name from above)
# print(bic_value)  #You should see bic for GMM model generated using n=2.
# #Do this exercise for different n values and plot them to find the minimum.


# Now, to explain m.bic, here are the lines I used in the video. 
# n_components = np.arange(1,10)
# gmm_models = [GMM(n, covariance_type='tied').fit(img2) for n in n_components]
# plt.plot(n_components, [m.bic(img2) for m in gmm_models], label='BIC')

# Here, we are computing multiple GMM models each by changing n value from 1 to 10. 
# Then, for each n value we are computing bic via m.bic(img2) where m is replaced by gmm_models for each of the model generated. Think of this as typing gmm_model.bic(img2) each time you change n and generate a new GMM model. 

# I hope this explanation helps better understand the video content.