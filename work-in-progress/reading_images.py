# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:49:27 2019

@author: ykrempp
"""

from PIL import Image

import matplotlib.pyplot as plt
import cv2


folder = "c:/CloudStation/2_Personnel/2.1_Cours/2.1.4_Python/images"
folder2 = "S:/_Sample_images_for_development/time-lapse lsm 900 tracking group vassiliki - akrivi/"
image = "/embryos.tif"
image2 = "/embryos_clean_rgb.tif"
image3 = "Ctrl_1.czi"
path = folder+image
path2 = folder+image2
path3 =folder2+image3

#img = Image.open(path)
#img.show()

grey_img_cv2 = cv2.imread(path, 0)
color_img_cv2 = cv2.imread(path2, 1)

# cv2.imshow("CV2 Grey Image", grey_img_cv2)
# cv2.imshow("CV2 Color Image", color_img_cv2)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(color_img_cv2)
#note that cv2 encodes images in BGR, not RGB



#pip install czifile

# import czifile

# czi_image = czifile.imread(path3)
# print(czi_image.shape)
#plt.imshow(czi_image[0,1,0,0,:,:,0])


# brightfield = czi_image[0,1,0,0,:,:,0]
# fluorescence = czi_image[0,0,0,0,:,:,0]
# print(brightfield.shape)
# print(fluorescence.shape)


# cv2.imshow("BF", brightfield)
# cv2.imshow("Fluo", fluorescence)

cv2.waitKey(0)
cv2.destroyAllWindows()