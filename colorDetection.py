import cv2
import numpy as np
from PIL import Image

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

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    mask_ = Image.fromarray(mask)
    bbox =mask_.getbbox()  # Get bounding box of the detected area
    if bbox is not None:
        x1 , y1 , x2 , y2 =bbox
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)

    #  show both windows
    cv2.imshow("Webcam", frame)
    # cv2.imshow("Mask", mask)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):  #press q to exit
        break

cap.release()
cv2.destroyAllWindows()

