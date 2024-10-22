import cv2
import mediapipe as mp
from HandTrackingModule import HandDetector
import numpy as np

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]


detector = HandDetector()

capture = cv2.VideoCapture(0)

while True:
    success, img = capture.read()
    
    lmlist, img = detector.lmlist(img)

    if lmlist:
        fingers, img = detector.fingersUp(img, lmlist, False)
        # print(fingers)
        if(fingers == [1,1,1,1,1]):
            length, img = detector.fingerDistance(4,8,img,lmlist, True)
            # print(length)

            vol = np.interp(length, (20,200), (minVol, maxVol))
            volPer = np.interp(length, (20,200), (0, 100))
            volBar = np.interp(length, (20,200), (270, 120))
            cv2.putText(img, str(int(volPer)) + "%", (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            cv2.rectangle(img, (50,120), (80, 270), (255,0,0), 3)
            cv2.rectangle(img, (50,int(volBar)), (80, 270), (255,0,0), cv2.FILLED)

            volume.SetMasterVolumeLevel(vol, None)


    cv2.imshow("Video Feed",img)
    key = cv2.waitKey(1)
    if(key == 27):
        break

capture.release()
cv2.destroyAllWindows()