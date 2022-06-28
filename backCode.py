import os
import cv2

#Variables
width, height = 1280, 720
folderPath = ("slide")


#Set the list images
pathImages = sorted(os.listdir(folderPath), key=len)
print(pathImages)

#Camera setup
cap = cv2.VideoCapture(0)       #parameter 0 for webcam
cap.set(3, width)
cap.set(4, height)

#Variables
imgNumber = 0

while True:
    #Importing images
    success, img = cap.read()
    pathFullImages = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImages)





    cv2.imshow("image", img)
    cv2.imshow("slide", imgCurrent)
    
    key = cv2.waitKey(1)
    if key == ord('q'):         #keyboard input for interupt program
        break