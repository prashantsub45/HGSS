import cvzone
import math
from cvzone.HandTrackingModule import HandDetector
import cv2 as cv
import pandas as pd
import urllib.request
import numpy as np
# ser.close()

import os
i=0


# Function to send commands to ESP32CAM

cv.namedWindow("hand detection", cv.WINDOW_AUTOSIZE)

def take_video(i=0):
    # url = "http://192.168.253.239/800x600.jpg"
    
    # print("inside take video")
    cap=cv.VideoCapture(0)
    # cap = cv.VideoCapture(url)
    



    detector=HandDetector(detectionCon=0.8,maxHands=2)
    play = False 
    pause = False
    previous = False
    next = False

    #ser=serial.Serial('com3',9600,timeout=1)
    while True:
        # img_resp = urllib.request.urlopen(url)
        # imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
        # img = cv.imdecode(imgnp, -1)   // Read the image from the URL of the ESP32CAM

        success, img = cap.read()
        if not success:
            print("Failed to grab frame from webcam")
            break




        #sucess,img=cap.read()
        hands,img = detector.findHands(img)
        if hands:
            
            hands1=hands[0]
            lmlist1=hands1['lmList']
            bbox1=hands1["bbox"]
            if lmlist1:
                fingers=detector.fingersUp(hands1) 
                # print(fingers)                                              #tells you about which finger is up
                #fingers detection
                if fingers==[1,1,1,1,1] : #or fingers==  [0,0,0,0,0]
                    if play== False : 
                        print('Play the music')#,fingers)
                        play = True
                        pause = False
                        data={"comm":["play"]}
                        df=pd.DataFrame(data)
                        df.to_csv("C:/Users/ASUS/Desktop/Final minor project/minorProject/gesture_engine/try.csv",index=False)
                    else : 
                        pass
                if fingers==[0,0,0,0,0]: #or fingers== [1,1,1,1,1]
                    if pause== False : 
                        print('Pause the music')#,fingers)
                        pause = True
                        play = False
                        data={"comm":["pause"]}
                        df=pd.DataFrame(data)
                        df.to_csv("C:/Users/ASUS/Desktop/Final minor project/minorProject/gesture_engine/try.csv",index=False)
                    else : 
                        pass
                    
                if fingers==[0,1,0,0,0] :
                    if previous== False : 
                        print('Previous music')
                        data={"comm":["previous"]}
                        df=pd.DataFrame(data)
                        df.to_csv("C:/Users/ASUS/Desktop/Final minor project/minorProject/gesture_engine/try.csv",index=False)
                        previous = True
                        next = False
                    else : 
                        pass
                if fingers==[0,1,1,0,0]:
                    if next== False : 
                        print('Next music')
                        data={"comm":["next"]}
                        df=pd.DataFrame(data)
                        df.to_csv("C:/Users/ASUS/Desktop/Final minor project/minorProject/gesture_engine/try.csv",index=False)
                        next = True
                        previous = False
                    else : 
                        pass
            
                if fingers[4]==1:
                    fourf=fingers
                    fourf.pop(0)
                    xt,yt=lmlist1[4][0],lmlist1[4][1]
                    xi,yi=lmlist1[8][0],lmlist1[8][1]
                    xib,yib=lmlist1[5][0],lmlist1[5][1]
                    xpb,ypb=lmlist1[17][0],lmlist1[17][1]
                    x0,y0=lmlist1[0][0],lmlist1[0][1]
                    
                    #print(xt,yt)
                    #print(lmlist1)
                    cv.circle(img,(xt,yt),5,(255,0,255),cv.FILLED)
                    cv.circle(img,(xi,yi),5,(255,0,255),cv.FILLED)
                    cv.circle(img,(xib,yib),5,(255,0,255),cv.FILLED)
                    cv.circle(img,(xpb,ypb),5,(255,0,255),cv.FILLED)
                    cv.circle(img,(x0,y0),5,(255,0,255),cv.FILLED)
                    cv.line(img,(x0,y0),(xi,yi),(255,0,255),2)
                    
                    #finding length
                    length_thumb=math.hypot(xt-x0,yt-y0)
                    length_roatate=math.hypot(xib-xpb,yib-ypb)
                    length_index=math.hypot(xi-x0,yi-y0)
                    #print(length_roatate)
                    #print(length_thumb)
                    if length_thumb <70:
                    # print("decrease height",length_thumb)
                        cv.circle(img,(xt,yt),5,(255,0,0),cv.FILLED)
                        #ser.write(b'a')
                    if length_thumb > 100:
                    #  print('increase height',length_thumb)
                        cv.circle(img,(xt,yt),5,(255,0,0),cv.FILLED)
                        #ser.write(b'b')
                    if length_index<80:
                    # print("contrcat")
                        cv.circle(img,(xi,yi),5,(255,0,0),cv.FILLED)
                    if length_index>150:
                    # print('expand')
                        cv.circle(img,(xi,yi),5,(255,0,0),cv.FILLED)
                    if length_roatate<30:
                        #print("rotate left")
                        (img,(xpb,ypb),5,(255,0,0),cv.FILLED)
    #                 if length_roatate>80:
    #                    # print("come to normal")

        i=i+1
        if i>60:
                play = False 
                pause = False
                previous = False
                next = False
                i=0

        cv.imshow("hand detection", img)


        key=cv.waitKey(1)
        if key==ord('q'):
            cap.release()
            break



if __name__ == '__main__':
    take_video()
  
   
