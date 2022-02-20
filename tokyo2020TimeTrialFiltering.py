import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow, imread
from skimage.color import rgb2hsv, hsv2rgb
import cv2

track = imread("tokyo2020TimeTrial.png")
plt.figure(num = None, figsize = (8,6), dpi = 80)

track_filtered = (track[:,:,0] > 150) & (track[:,:,1] < 100) & (track[:,:,2] < 110)
track_new = track.copy()
track_new[:, :, 0] = track_new[:, :, 0] * track_filtered
track_new[:, :, 1] = track_new[:, :, 1] * track_filtered
track_new[:, :, 2] = track_new[:, :, 2] * track_filtered

track_dilated = track_new.copy()

# cv2.dilate(track_new, track_dilated)


plt.imshow(track_new)
plt.show()