import cv2
import numpy as np

class Motion_Detection:
    def __init__(self,first_frame,MIN_SIZE_FOR_MOVEMENT=2000,Min_movement=3):
        self.MIN_SIZE_FOR_MOVEMENT = MIN_SIZE_FOR_MOVEMENT
        self.Min_movement = Min_movement
        self.first_frame=self.convert_gray(first_frame)
        self.counter_no_movement=0

    def convert_gray(self,frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        return gray

    def detect(self,next_frame):
        res=True
        transient_movement_flag=False
        next_frame=self.convert_gray(next_frame)
        frame_delta = cv2.absdiff(self.first_frame, next_frame)
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations = 2)
        cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            if cv2.contourArea(c) > self.MIN_SIZE_FOR_MOVEMENT:
                transient_movement_flag = True

                break

        if(not transient_movement_flag):
            self.counter_no_movement+=1
        else:
            self.counter_no_movement=0
        
        if(self.counter_no_movement>=self.Min_movement):
            res=False
        self.first_frame=next_frame
        return res



        
            


