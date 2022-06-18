import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('images/me_winthrop.jpg', 0)
# cv.Canny(input image, minVal, maxVal )
edges = cv.Canny(img, 100, 200)

plt.subplot(1,2,1)
plt.imshow(img, cmap = 'gray')
plt.title('Original Image')

plt.subplot(1,2,2)
plt.imshow(edges, cmap = 'gray')
plt.title('Edge Image')


plt.show()
