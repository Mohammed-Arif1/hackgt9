import cv2
import mediapipe as mp
import numpy as np
import time
import gesturePrediction as gP


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
                lmlist.append([cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
        return lmlist

    def multiHand(self,img):
        hand_dict = {}
        hand_order_list = []
        hand_num = 0
        i = 0
        x, y, c = img.shape
        multi_lmlist = []
        if self.results.multi_hand_landmarks:
            for handslms in self.results.multi_hand_landmarks:
                multi_lmlist.append([])
                for lm in handslms.landmark:
                    lmx = (int(lm.x * x))
                    lmy = (int(lm.y * y))
                    multi_lmlist[-1].append([lmx, lmy])
                    
                handType = self.results.multi_handedness[i].classification[0].label
                i+=1
                hand_dict[handType] = hand_num
                hand_order_list.append(handType)
                hand_num+=1

        return multi_lmlist, hand_dict, hand_order_list



    def leftRight(self,img, hand_dict, handNo=0,draw=True):
        leftOrRight='No Movement'
        
        if self.results.multi_hand_landmarks:
            if (len(hand_dict) == 1):
                myHand=self.results.multi_hand_landmarks[handNo]
            elif (len(hand_dict) == 2):
                myHand=self.results.multi_hand_landmarks[hand_dict['Right']]
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
    
    def upDown(self,img, hand_dict, handNo=0,draw=True):
        upDown='No Movement'
        if self.results.multi_hand_landmarks:
            if (len(hand_dict) == 1):
                myHand=self.results.multi_hand_landmarks[handNo]
            elif (len(hand_dict) == 2):
                myHand=self.results.multi_hand_landmarks[hand_dict['Right']]
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

    def useTool(self,hand_dict):
        if len(hand_dict) > 1:
            return True

def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector(cap)
    model, classNames = gP.getModel()
    

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.findHands(img)
        lmlist = detector.findPosition(img)
        multi_lmlist, hand_dict, hand_order_list = detector.multiHand(img)
        #print("Hand order list: ",hand_order_list)
        #print(len(hand_dict))
        #print("hand_dict: ",hand_dict)
        leftOrRight=detector.leftRight(img, hand_dict)
        upOrDown=detector.upDown(img, hand_dict)
        useTool = detector.useTool(hand_dict)
        print([leftOrRight,upOrDown,useTool])
        #lmlist1 = detector.findPosition(img, handNo=1)
        if len(lmlist) != 0:
            #print(lmlist)
            #print("Hand 1:",lmlist)
            file=open("lmlist", 'w' )
            file.write(str(lmlist))
            file.close()

            #if len(multi_lmlist) == 2:
                #gestureName1 = gP.getGestures(multi_lmlist[0], model, classNames)
                #gestureName2 = gP.getGestures(multi_lmlist[1], model, classNames)

                #hand_dict[hand_dict[0]].append(gestureName1)
                #hand_dict[hand_dict[1]].append(gestureName2)
                #print(hand_dict)
            
            #print("Normal:",lmlist)
            #print("numpy array:",[np.ndarray.tolist(np.array(lmlist)[:,1:3])])
            #cv2.putText(img, str(gestureName),(10,200),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
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