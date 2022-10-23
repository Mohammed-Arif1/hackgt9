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
                #print("no hands detected")
                th = Thread(target=stopMoving, args=(person,))
                th.start()
                currUpDown = dir.INIT
                currLeftRight = dir.INIT
                prevUpDown = dir.INIT
                prevLeftRight = dir.INIT
        _, hand_dict, _ = detector.multiHand(img)
        leftOrRight = detector.leftRight(img,hand_dict)
        upOrDown = detector.upDown(img, hand_dict)
        useTool = detector.useTool(hand_dict)
        



        if (upOrDown == 'up'):
            currUpDown = dir.UP
            print("up")
        elif upOrDown == 'down':
            currUpDown = dir.DOWN
            print("down")
        elif upOrDown == 'No Movement':
            currUpDown = dir.INIT
            print("none-ud")
        if leftOrRight == 'right':
            currLeftRight = dir.RIGHT
            print("right")
        elif leftOrRight == 'left':
            currLeftRight = dir.LEFT
            print("left")
        elif leftOrRight == "No Movement":
            print("none-lr")
            currLeftRight = dir.INIT

        
        t = Thread(target=keyPress, args=(currUpDown, prevUpDown,currLeftRight, prevLeftRight, person, useTool))
        #t2 = Thread(target=keyPressLeftRight, args=(currLeftRight, prevLeftRight, person))
        t.start()
        prevLeftRight = currLeftRight
        prevUpDown = currUpDown
        #p.join()
def keyPress(currUpDown, prevUpDown, currLeftRight, prevLeftRight, person, useTool):
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
    if (currLeftRight != prevLeftRight):
        #print(currLeftRight)
        #stopMoving(person)
        person.stopMovingLeft()
        person.stopMovingRight()
        time.sleep(0.2)
        #print("---------------------------")
        #print(currLeftRight)
        #print(prevLeftRight)
        #print("----------------------------")
        if (currLeftRight == dir.LEFT):
            print("hold left")
            person.holdLeft()
            #person.moveLeft()
        elif currLeftRight == dir.RIGHT:
            print("holdright")
            person.holdRight()
            #person.moveRight()
    if (useTool):
        person.holdTool()
    else:
        person.stopTool()
#def keyPressLeftRight(currLeftRight, prevLeftRight, person):




def stopMoving(person):
        #print("stopping movement")
        person.stopMovingDown()
        person.stopMovingUp()
        person.stopMovingLeft()
        person.stopMovingRight()


        

if __name__ == "__main__":
    main()
