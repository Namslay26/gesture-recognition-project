import cv2 
import mediapipe as mp
from HandTrackingModule import HandDetector
import pyautogui as py
import numpy as np
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
        if (fingers[1]==1 and fingers[2]==0 ):

            x1,y1=lmlist[8][1:]
            cv2.rectangle(img, (frameR,frameR), (540, 380), (255,0,255),3)
            cv2.cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)

            posX=np.interp(x1,(frameR,640-frameR),(0,1920))
            posY=np.interp(y1,(frameR,480-frameR),(0,1080))
            clocX=plocX+(posX-plocX)/smoothening
            clocY=plocY+(posY-plocY)/smoothening


            py.moveTo(1920-clocX,clocY) 

            plocX=clocX
            plocY=clocY
        elif (fingers==[0,1,1,0,0]):
            distance,img=detector.fingerDistance(8,12,img,lmlist)
            if (distance<30):
                py.click()

            
    cv2.imshow("video feed",img)
    key = cv2.waitKey(1)
    if (key==27):
        break



capture.release()
cv2.destroyAllWindows()    

