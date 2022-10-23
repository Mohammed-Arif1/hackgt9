import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, capture, mode=False, maxHands=2, detectionCon=1, trackCon=1):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.width = capture.get(3)
        self.height = capture.get(4)

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=False,
                      max_num_hands=2,
                      min_detection_confidence=0.7,
                      min_tracking_confidence=0.5)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):

        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
        return lmlist

    def leftRight(self,img,handNo=0,draw=True):
        leftOrRight='No Movement'
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]
            cx, cy = int(myHand.landmark[0].x*self.width + myHand.landmark[9].x*self.width) / 2, int(myHand.landmark[0].y*self.height + myHand.landmark[9].y*self.height)/2
            if cx<self.width/3:
                leftOrRight='left'
            elif cx>2*self.width/3:
                leftOrRight='right'
            #print(myHand.landmark[0].x*self.width)
            #print(myHand.landmark[9].x*self.width)
            #print(cx)
            #print(self.width/3)
            #print(2*self.width/3)
            #print("--------")
        #print("LOR", leftOrRight)
        return leftOrRight
    
    def upDown(self,img,handNo=0,draw=True):
        upDown='No Movement'
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]
            #print("yval", myHand.landmark[0].y)
            cx, cy = int(myHand.landmark[0].x*self.width + myHand.landmark[9].x*self.width) / 2, int(myHand.landmark[0].y*self.height + myHand.landmark[9].y*self.height)/2
            if cy<self.height/3:
                upDown='up'
            elif cy > 2*self.height/3:
                upDown='down'
            #print(cy)
            #print(self.height/3)
            #print(2*self.height/3)
            #print("------------")
        #print("UOD", upDown)
        return upDown

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.findHands(img)
        lmlist = detector.findPosition(img)
        leftOrRight=detector.leftRight(img)
        upOrDown=detector.upDown(img)
        #lmlist1 = detector.findPosition(img, handNo=1)
        if len(lmlist) != 0:
            #print(lmlist)
            print("Hand 1:",lmlist)
            file=open("lmlist", 'w' )
            file.write(str(lmlist))
            file.close()
        #if (len(lmlist1)) !=0:
            #print(lmlist)
        #    print("Hand 2:",lmlist1)
         #   file=open("lmlist1", 'w' )
          #  file.write(str(lmlist1))
           # file.close()

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        cv2.putText(img, str(leftOrRight),(10,100),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.putText(img, str(upOrDown),(10,150),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)


        cv2.imshow("Image", img)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()