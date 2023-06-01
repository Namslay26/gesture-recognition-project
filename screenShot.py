import cv2 
import mediapipe as mp
from HandTrackingModule import HandDetector
import pyautogui as py

detector = HandDetector()

mpHands = mp.solutions.hands
hands = mpHands.Hands()
drawTools=mp.solutions.drawing_utils

capture = cv2.VideoCapture(0)
clocX,clocY,plocX,plocY=0,0,0,0
smoothening=7
frameR=100
while True:
    success, img = capture.read()
    lmlist,img=detector.lmlist(img)
    if lmlist:
        fingers, img=detector.fingersUp(img,lmlist,False)
        if (fingers==[0,1,0,0,1]):
            py.screenshot('screenshoting.png')
            py.alert(text='Screenshot taken', title='Successful', button='OK')
            
    cv2.imshow("video feed",img)
    key = cv2.waitKey(1)
    if (key==27):
        break



capture.release()
cv2.destroyAllWindows()    

