import os
import cv2
from cvzone.HandTrackingModule import HandDetector



#Variables
width, height = 1280, 720
folderPath = ("slide")


#Set the list images
pathImages = sorted(os.listdir(folderPath), key=len)
# print(pathImages)

#Camera setup
cap = cv2.VideoCapture(0)       #parameter 0 for webcam
cap.set(3, width)
cap.set(4, height)

#Variables
imgNumber = 0
hs, ws = int(120*1), int(180*1)
gestureThreshold = 200
buttonCounter = 0
buttonPressed = False
buttonDelay = 5                 #depend on how fast webcam read the frame

#Hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    #Importing images

    success, img = cap.read()
    img = cv2.flip(img, 1)
    pathFullImages = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImages)
    
    hands, img = detector.findHands(img)
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0,255,0), 10)

    if hands and buttonPressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand['center']
        lmList = hand['lmList']
        indexFingers = lmList[8][0], lmList[8][1]

        #Gesture #1 - Left
        if cy <= gestureThreshold:
            if fingers == [1,0,0,0,0]:
                print("left")
                if imgNumber > 0:
                    buttonPressed = True
                    imgNumber -= 1

        #Gesture #2 - Right
            if fingers == [0,0,0,0,1]:
                print("right")
                if imgNumber < len(pathImages) - 1:
                    buttonPressed = True
                    imgNumber += 1
        
        #Gesture #3 - Drawer
        if fingers == [0,1,1,0,0]:
            cv2.circle(imgCurrent, indexFingers, 12, (0,0,255), cv2.FILLED)
        

    #Button press iteration
    if buttonPressed:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPressed = False



    #Adding webcam to images
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w - ws:w] = imgSmall



    cv2.imshow("image", img)
    cv2.imshow("slide", imgCurrent)
    
    key = cv2.waitKey(1)
    if key == ord('q'):         #keyboard input for interupt program
        break