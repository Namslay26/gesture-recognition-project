import cv2 
import mediapipe as mp
from HandTrackingModule import HandDetector
import screen_brightness_control as sbc
import numpy as np

detector = HandDetector()

mpHands = mp.solutions.hands
hands = mpHands.Hands()
drawTools=mp.solutions.drawing_utils

capture = cv2.VideoCapture(0)
while True:
    success, img = capture.read()
    lmlist,img=detector.lmlist(img)
    if lmlist:
       
        fingers, img = detector.fingersUp(img, lmlist, False)
        
        if(fingers == [1,1,1,1,1]):
            length, img = detector.fingerDistance(4,8,img,lmlist, True)
            brightness=sbc.get_brightness(display=0)
            min_b=0
            max_b=100
            bright=np.interp(length, (20,200), (min_b, max_b))
            brightBar = np.interp(length, (20,200), (270, 120))
            cv2.putText(img, str(int(brightness)) + "%", (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            cv2.rectangle(img, (50,120), (80, 270), (255,0,0), 3)
            cv2.rectangle(img, (50,int(brightBar)), (80, 270), (255,0,0), cv2.FILLED)

            sbc.set_brightness(bright)

            
    cv2.imshow("video feed",img)
    key = cv2.waitKey(1)
    if (key==27):
        break



capture.release()
cv2.destroyAllWindows()    
