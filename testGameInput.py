from multiprocessing.pool import INIT
from pickle import TRUE
import cv2

from matplotlib.sankey import DOWN, UP
from pyautogui import LEFT, RIGHT
import stardewValleyCommands
import time
import handDetection
from enum import Enum

class upDown(Enum):
    INIT = 0
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

def main():

    


    currUpDown = INIT
    currLeftRight = INIT
    prevUpDown = INIT
    prevLeftRight = INIT
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

        leftOrRight = detector.leftRight(img)
        upOrDown = detector.upDown(img)




        if (upOrDown == 'up'):
            currUpDown = UP
        elif upOrDown == 'down':
            currUpDown = DOWN
        if  leftOrRight == 'right':
            currLeftRight = RIGHT
        elif leftOrRight == 'left':
            currLeftRight = LEFT
        

        if (currUpDown != prevUpDown):
            person.stopMovingDown()
            person.stopMovingUp()
        if (currLeftRight != prevLeftRight):
            person.stopMovingLeft()
            person.stopMovingRight()
            time.sleep(1)

        if (currUpDown == UP):
            person.holdUp()
        elif currUpDown == DOWN:
            person.holdDown()
        if (currLeftRight == LEFT):
            person.holdLeft()
        elif currLeftRight == RIGHT:
            person.holdRight()
        else:
            person.stopMovingDown()
            person.stopMovingUp()
            person.stopMovingLeft()
            person.stopMovingRight()
            

        

if __name__ == "__main__":
    main()
