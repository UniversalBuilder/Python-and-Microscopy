# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 11:05:36 2019

@author: ykrempp
"""


import numpy as np
import matplotlib.pyplot as plt

from skimage import io, img_as_float, img_as_ubyte
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage.metrics import peak_signal_noise_ratio
from skimage.util import random_noise

img = img_as_float(io.imread('S:/_Sample_images_for_development/TEM/Cross-Sections-of-Cilia-in-Mouse-Trachea.jpg'))

patch_kw = dict(patch_size=5,      # 5x5 patches
                patch_distance=3,  # 13x13 search area
                multichannel=True)

sigma_est = np.mean(estimate_sigma(img, multichannel=True))

denoise = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=True,
                           **patch_kw)
fig, ax = plt.subplots(nrows=1,ncols=2, figsize= (25,25))
ax[0].imshow(img, cmap='gray')
ax[1].imshow(denoise, cmap='gray')

denoise_ubyte = img_as_ubyte(denoise)

fig2, ax2 = plt.subplots(nrows=1,ncols=1)
ax2.hist(denoise_ubyte.flat, bins=255, range=(0, 255))

segm1 = (denoise_ubyte <=85)
segm2 = (denoise_ubyte > 86) & (denoise_ubyte <= 128 )
segm3 = (denoise_ubyte > 129) & (denoise_ubyte <= 180 )
segm4 = (denoise_ubyte > 181) & (denoise_ubyte <= 255 )

all_segments = np.zeros((denoise_ubyte.shape[0], denoise_ubyte.shape[1], 3))

all_segments[segm1] = (1,0,0)
all_segments[segm2] = (0,1,0)
all_segments[segm3] = (0,0,1)
all_segments[segm4] = (1,1,0)

fig3, ax3 = plt.subplots(nrows=1,ncols=2, figsize=(25,25))
ax3[0].imshow(all_segments)
ax3[1].imshow(segm1, cmap='gray')

plt.imsave('S:/CloudStation/2_Personnel/2.1_Cours/2.1.4_Python/Course - Python for Microscopy/newimage.png', format="png", arr=all_segments)

