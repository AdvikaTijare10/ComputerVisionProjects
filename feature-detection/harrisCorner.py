import os
import cv2
import numpy as np
 # to find corners, the image should be gray and float32 type
#image_path=os.path.join('data','chessBoard.png')
image_path=os.path.join('data','table.jpg')

img = cv2.imread(image_path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # harris works on intensity chnages an dnot color, thus grayscale

gray = np.float32(gray)
gray = cv2.GaussianBlur(gray, (7,7), 0)
dst = cv2.cornerHarris(gray,5,3,0.04) #it is a score map, ecah pixel shows how much 'corner-like' it is , high value emans strong corner

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.1*dst.max()]=[0,0,255] #the pixels with score gretaer than that are marked red 
cv2.imwrite(os.path.join('data','cornersMarkedTable.jpg'),img)
cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()