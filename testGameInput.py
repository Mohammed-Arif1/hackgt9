from pickle import TRUE
import cv2
from multiprocessing import Process
import stardewValleyCommands
import time
import handDetection
from enum import Enum
from threading import Thread

class dir(Enum):
    INIT = 0
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

def main():
    currUpDown = dir.INIT
    currLeftRight = dir.INIT
    prevUpDown = dir.INIT
    prevLeftRight = dir.INIT
    person = stardewValleyCommands.StardewValleyCommands()

    cap = cv2.VideoCapture(0)
    detector = handDetection.handDetector(cap)
    noHand = True

    while (True):
        #inDir = input("What direction?")
        noHand = True
        while noHand:
            success, img = cap.read()
            img = cv2.flip(img, 1)
            img = detector.findHands(img)
            lmlist = detector.findPosition(img)
            cv2.imshow("Image", img)
            cv2.waitKey(1)
            if len(lmlist) != 0:
                noHand = False
            else:
                th = Thread(target=stopMoving, args=(person))
                
        leftOrRight = detector.leftRight(img)
        # Handle mirrored camera
        if leftOrRight == "right":
            leftOrRight = "left"
        elif leftOrRight == "left":
            leftOrRight = "right"
        upOrDown = detector.upDown(img)
        



        if (upOrDown == 'up'):
            currUpDown = dir.UP
        elif upOrDown == 'down':
            currUpDown = dir.DOWN
        elif upOrDown == 'No Movement':
            currUpDown = dir.INIT
        if leftOrRight == 'right':
            currLeftRight = dir.RIGHT
        elif leftOrRight == 'left':
            currLeftRight = dir.LEFT
        elif leftOrRight == "No Movement":
            currLeftRight = dir.INIT

        
        t = Thread(target=keyPressUpDown, args=(currUpDown, prevUpDown, person))
        t2 = Thread(target=keyPressLeftRight, args=(currLeftRight, prevLeftRight, person))
        t.start()
        t2.start()
        prevLeftRight = currLeftRight
        prevUpDown = currUpDown
        #p.join()
def keyPressUpDown(currUpDown, prevUpDown, person):
    #stopMoving = False
    if (currUpDown != prevUpDown):
        person.stopMovingDown()
        person.stopMovingUp()
        if (currUpDown == dir.UP):
            person.holdUp()
            #person.moveUp()
        elif currUpDown == dir.DOWN:
            person.holdDown()
            #person.moveDown()
    #print(currLeftRight)
def keyPressLeftRight(currLeftRight, prevLeftRight, person):
    if (currLeftRight != prevLeftRight):
        #print(currLeftRight)
        #stopMoving(person)
        person.stopMovingLeft()
        person.stopMovingRight()
        #time.sleep(1)
        if (currLeftRight == dir.LEFT):
            person.holdLeft()
            #person.moveLeft()
        elif currLeftRight == dir.RIGHT:
            person.holdRight()
            #person.moveRight()



def stopMoving(person):
        #print("stopping movement")
        person.stopMovingDown()
        person.stopMovingUp()
        person.stopMovingLeft()
        person.stopMovingRight()
            

        

if __name__ == "__main__":
    main()
