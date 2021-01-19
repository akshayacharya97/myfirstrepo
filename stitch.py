# import the necessary packages
from Stitcher import Stitcher
import argparse
import imutils
import cv2

# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageA = cv2.imread("frame001.jpg")
imageB = cv2.imread("frame008.jpg")
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)
stitcher = Stitcher()
# stitch the images together to create a panorama
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
print(type(result))
cv2.imwrite("Result.jpg", result)