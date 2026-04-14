import numpy as np
import cv2 as cv
import os
img_path=os.path.join('data','table.jpg')
img = cv.imread(img_path)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray,50,0.08,5) #img,max no of corners to detect, quality level,min distance in pixels between 2 corners
corners = np.int32(corners)

for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),3,255,-1)
cv.imwrite(os.path.join('data','cornersMarkedTableShi_Tomasi.jpg'),img)
cv.imshow('marked_Tableimg',img)
cv.waitKey(0)