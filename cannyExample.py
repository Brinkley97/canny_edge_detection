
from __future__ import print_function
import cv2 as cv
import argparse


max_lowThreshold = 100
window_name = 'Edge Detection'
title_trackbar = 'Detection Range :'
# in relation to the trackbar
    # if low, will show more edges but if high, then less edges
ratio = 3
# the size of the Sobel kernel to be used internally
kernel_size = 3

def CannyThreshold(val):
    low_threshold = val
    # cv.blur(image/source, size)
    # https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html
    img_blur = cv.blur(image_new_color, (1,1))
    # cv.Canny(image, threshold1, threshold2*ratio, apertureSize)
        # an array of values - I believe pixels of the image
    detected_edges = cv.Canny(img_blur, low_threshold, low_threshold*ratio, kernel_size)
    print(detected_edges)
    # search detected_edges array & compare each value
        # if = 0, then print False; otherwise print True
    mask = detected_edges != 0
    print('\n', mask)
    # for mask in range(0, len(detected_edges)):
    #     if detected_edges.any() != 0:
    #         mask = True
    #     else :
    #         mask = False
    # print('\n', mask)
    image = src * (mask[:,:,None].astype(src.dtype))
    cv.imshow(window_name, image)

parser = argparse.ArgumentParser(description='Code for Canny Edge Detector.')
parser.add_argument('--input', help='Path to input image.', default='images/testDataSetImage5.png')
args = parser.parse_args()
src = cv.imread(cv.samples.findFile(args.input))

if src is None:
    print("Can't open open of find image: ", args.input)
    exit(0)

image_new_color = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.namedWindow(window_name)
cv.createTrackbar(title_trackbar, window_name , 0, max_lowThreshold, CannyThreshold)

# implement function
CannyThreshold(0)
# CannyThreshold(10)
# CannyThreshold(50)

#waits for user to press any key
cv.waitKey(0)
