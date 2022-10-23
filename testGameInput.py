from pickle import TRUE
import cv2
from multiprocessing import Process
from matplotlib.sankey import DOWN, UP
from pyautogui import LEFT, RIGHT
import stardewValleyCommands
import time
import handDetection
from enum import Enum
from threading import Thread

class upDown(Enum):
    INIT = 0
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

def main():
    currUpDown = upDown.INIT
    currLeftRight = upDown.INIT
    prevUpDown = upDown.INIT
    prevLeftRight = upDown.INIT
    person = stardewValleyCommands.StardewValleyCommands()
    detector = handDetection.handDetector()
    cap = cv2.VideoCapture(0)
    noHand = True

    while (True):
        #inDir = input("What direction?")
        noHand = True
        while noHand:
            success, img = cap.read()
            img = detector.findHands(img)
            lmlist = detector.findPosition(img)
            cv2.imshow("Image", img)
            cv2.waitKey(1)
            if len(lmlist) != 0:
                noHand = False

                #p.join()
            else:
                th = Thread(target=stopMoving, args=(person))
        leftOrRight = detector.leftRight(img)
        upOrDown = detector.upDown(img)
        



        if (upOrDown == 'up'):
            currUpDown = UP
        elif upOrDown == 'down':
            currUpDown = DOWN
        if leftOrRight == 'right':
            currLeftRight = RIGHT
        elif leftOrRight == 'left':
            currLeftRight = LEFT

        
        t = Thread(target=keyPress, args=(currUpDown, prevUpDown, currLeftRight, prevLeftRight, person))
        t.start()
        prevLeftRight = currLeftRight
        prevUpDown = currUpDown
        #p.join()
def keyPress(currUpDown, prevUpDown, currLeftRight, prevLeftRight, person):
    #stopMoving = False
    if (currUpDown != prevUpDown):
        person.stopMovingDown()
        person.stopMovingUp()
        if (currUpDown == UP):
            person.holdUp()
            #person.moveUp()
        elif currUpDown == DOWN:
            person.holdDown()
            #person.moveDown()
    #print(currLeftRight)
    if (currLeftRight != prevLeftRight):
        print(currLeftRight)
        person.stopMovingLeft()
        person.stopMovingRight()
        #time.sleep(1)
        if (currLeftRight == LEFT):
            person.holdLeft()
            #person.moveLeft()
        elif currLeftRight == RIGHT:
            person.holdRight()
            #person.moveRight()



def stopMoving(person):
        #person.stopMovingDown()
        #person.stopMovingUp()
        person.stopMovingLeft()
        person.stopMovingRight()
            

        

if __name__ == "__main__":
    main()
