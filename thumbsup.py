import cv2
import mediapipe as mp
import pyttsx3
from HandTrackingModule import HandDetector


detector = HandDetector()
engine=pyttsx3.init()

capture = cv2.VideoCapture(0)

while True:
    success, img = capture.read()
    
    lmlist, img = detector.lmlist(img)
    thumbs_up=0
    if lmlist:
        fingers, img = detector.fingersUp(img, lmlist)

        if(fingers == [1,0,0,0,0]):
            if thumbs_up==0:
                engine.say("Thumbs up")
                engine.runAndWait()
                engine.stop()
                thumbs_up=1
        if(fingers == [0,0,0,0,0]):
            thumbs_up=0
                
   
        
    cv2.imshow("Video Feed",img)
    key = cv2.waitKey(1)
    if(key == 27):
        break

capture.release()
cv2.destroyAllWindows()
