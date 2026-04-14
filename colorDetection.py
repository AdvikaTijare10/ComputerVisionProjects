import cv2
import numpy as np
from PIL import Image

#hsv-> hue (wht color), saturation(how strong) , value(how bright)
def get_limits(color):
    c = np.uint8([[color]])   #1 pixel image
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV) #converting to hsv color space to get the hue value of the color we want to detect

    hue = hsvC[0][0][0] 

    
    lowerLimit = np.array([max(hue-20, 0), 50, 50], dtype=np.uint8)
    upperLimit = np.array([min(hue+20, 179), 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit


cap = cv2.VideoCapture(0)

blue = [255, 0, 0]   # BGR for blue

while True:
    ret, frame = cap.read()
    if not ret:
        break

    #  slight blur to reduce noise
    frame = cv2.GaussianBlur(frame, (5, 5), 0)

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(blue)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)  #only the pixel values in this range are shown white
    ## detects only 1 blue object crtcly else draws a bounding box around all the blue objects in frame
    # mask_ = Image.fromarray(mask)
    # bbox =mask_.getbbox()  # Get bounding box of the detected area
    # if bbox is not None:
    #     x1 , y1 , x2 , y2 =bbox
    #     cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)
    #each contour corresponds to one blue object
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 500:   # ignore small noise
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)  # frame, bottom left corner, top right corner, color, thickness
    #  show both windows
    #cv2.imshow("Webcam", frame)
    cv2.imshow("Webcam", frame)
    cv2.imshow("Mask", mask)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):  #press q to exit
        break

cap.release()
cv2.destroyAllWindows()

