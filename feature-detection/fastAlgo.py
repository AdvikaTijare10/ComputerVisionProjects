# this not only detects corners but also other high intensity features like corners, edges, blobs etc

import numpy as np
import cv2 as cv
import os
image_path=os.path.join('data','scenery.jpg')
img = cv.imread(image_path, cv.IMREAD_GRAYSCALE) # `<opencv_root>/samples/data/blox.jpg`

# Initiate FAST object with default values
fast = cv.FastFeatureDetector_create()

fast.setThreshold(50)
fast.setNonmaxSuppression(True)
fast.setType(cv.FAST_FEATURE_DETECTOR_TYPE_9_16)

# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv.drawKeypoints(img, kp, None, color=(255,0,0))

# Print all default params
print( "Threshold: {}".format(fast.getThreshold()) )
print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
print( "neighborhood: {}".format(fast.getType()) )
print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )


cv.imwrite(os.path.join('data','fast_true.png'), img2)

# Disable nonmaxSuppression

kp = fast.detect(img, None)

print( "Total Keypoints without nonmaxSuppression: {}".format(len(kp)) )

img3 = cv.drawKeypoints(img, kp, None, color=(255,0,0))

cv.imwrite(os.path.join('data','fast_false.png'), img3)
cv.imshow('fast_true.png', img2)
cv.imshow('fast_false.png', img3)
cv.waitKey(0)