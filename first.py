import cv2
import os
import numpy as np


image_path=os.path.join('.','data','scenery.jpg')
image=cv2.imread(image_path)
cv2.imwrite(os.path.join('.','data','scenery_copy.jpg'),image) #creates a copy of image and stores

#in opencv , the channels are in order BGR but in matplotlib the channels are in order RGB. so we need to convert the image from BGR to RGB before displaying it using matplotlib.
# image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB) #converts theimage from BGR to RGB

# plt.imshow(image)
# plt.axis('off')
# plt.show()
# print(image.shape) #size of image (row,height,channels)
# cv2.imshow('scenery',image)  #winow popup name, image to be shown

#Image resizing
# resized_image=cv2.resize(image,(250,332)) #(height,width)
# print(resized_image.shape) 
# cv2.imshow('resized_scenery',resized_image)
# cv2.waitKey(0) #remains indefinitely open until u press any other key
# cv2.destroyAllWindows()

#image cropping
# cropped_img=image[221:442,167:334]  #([height,width)])
# print(cropped_img.shape) #(rows,cols) num of rows gives height and num of cols gives width.
# cv2.imshow('cropped_img',cropped_img)
# cv2.waitKey(0)

#Visualizing colorspaces
img_path=os.path.join('.','data','parrot.jpg')
img=cv2.imread(img_path)
# converted_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #interchange of red and blue values
# black_white_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converts to gray color space
# cv2.imshow('parrot',converted_img)
# cv2.imshow('original_img',img)
# cv2.imshow('black_white_img',black_white_img)

#hsv colorspcae-> better than rgb becoz helps u detect red vs darkread and many other applications
# hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow('hsv_img',hsv_img)
# cv2.waitKey(0)

#Blurring an image
# blurred_img=cv2.blur(img,(7,7))
# cv2.imshow('blurred_img',blurred_img)
# cv2.waitKey(0)

#image thresholding
#first convert to grayscale
# gray_parrot=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresholded_img=cv2.threshold(gray_parrot,80,255,cv2.THRESH_BINARY) #values lower than 80 are given 0 while greater are assigned 255
# cv2.imshow('original_img',img)
# cv2.imshow('thresholded_img',thresholded_img)
# cv2.waitKey(0)

#Edge detection
# edge_img_path=os.path.join('.','data','edgeDEtection.jpg')
# edge_img=cv2.imread(edge_img_path)
# edge_detect_img=cv2.Canny(edge_img,250,500) #lower thresholds detects more edges thus more noise while higher thershold may give cleaner but miss edges
# cv2.imshow('original_img',edge_img)
# cv2.imshow('edged_img',edge_detect_img)
# cv2.waitKey(0)

#contours
contour_img_path=os.path.join('.','data','birds.jpg')
contour_img=cv2.imread(contour_img_path)
ret,thresh=cv2.threshold(contour_img,127,255,cv2.THRESH_BINARY_INV) #thresholding the image to get a binary image
cv2.imshow('thresh',thresh)
cv2.imshow('original_img',contour_img)
cv2.waitKey(0)
