
import imutils
import cv2
import numpy as np
from motion_detection import Motion_Detection





cap = cv2.VideoCapture(0) 
_,frame=cap.read()

mtd=Motion_Detection(first_frame=frame)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret, frame = cap.read()
    
    if(mtd.detect(frame)):
        text="movement"
    else:
        text="No_movement"


    cv2.putText(frame, str(text), (10,35), font, 0.75, (255,255,255), 2, cv2.LINE_AA)
    cv2.imshow("image",frame)
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()
