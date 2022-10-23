# TechVidvan hand Gesture Recognizer

# import necessary packages

import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
import pyautogui

# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils
handednessTextCoords = {
    "Left":(10, 50),
    "Right":(550, 50)
}

finger_Coord = [(8, 6, 5), (12, 10, 9), (16, 15, 13), (20, 18, 17)]
thumb_Coord = (4,2)
# Load the gesture recognizer model
model = load_model('mp_hand_gesture')

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
#print(classNames)


# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
        
    # Read each frame from the webcam
    _, frame = cap.read()

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Get hand landmark prediction
    result = hands.process(framergb)

    #print(result)
    
    className = ''

    # post process the result
    if result.multi_hand_landmarks:
        
        #for hand in result.multi_handedness:
        #    print("Hands", hand.classification)
        i = 0
        upCount = 0
        for handslms in result.multi_hand_landmarks:
            landmarks = []
            for lm in handslms.landmark:
                #print(id, lm)
                lmx = int(lm.x * x)

                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])
            #print(landmarks)
            #print("landmark-fingertip", finger_Coord[0][0])
            
            handType = result.multi_handedness[i].classification[0].label

            for coordinate in finger_Coord:
                #check if hand is upright
                #print(coordinate)
                #print(landmarks[coordinate[0]])
                #print(landmarks[coordinate[1]])
                #print(landmarks[coordinate[2]])

                if landmarks[0][1] > landmarks[coordinate[0]][1] and (abs(landmarks[coordinate[1]][1] - landmarks[coordinate[0]][1]) > (abs(landmarks[coordinate[2]][1] - landmarks[coordinate[1]][1])*0.1)) :
                    if landmarks[coordinate[0]][1] < landmarks[coordinate[1]][1]:
                        #print("coord",coordinate)
                        #print("top", landmarks[coordinate[0]][0])
                        #print("bottom", landmarks[coordinate[1]][0])

                        upCount += 1
            # Add thumb if all four other fingers are upright
            if (landmarks[thumb_Coord[0]][0] < landmarks[thumb_Coord[1]][0] and landmarks[thumb_Coord[0]][1] < landmarks[thumb_Coord[1]][1] and handType == "Right") or (landmarks[thumb_Coord[0]][0] > landmarks[thumb_Coord[1]][0] and landmarks[thumb_Coord[0]][1] < landmarks[thumb_Coord[1]][1] and handType == "Left"):
                #print(coordinate)
                #print("top-thumb", landmarks[thumb_Coord[0]][0])
                #print("bottom-thumb", landmarks[thumb_Coord[1]][0])
                upCount += 1
            #print("-------")
            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Predict gesture
            prediction = model.predict([landmarks])
            print([landmarks],', ',type(landmarks))
            #print(prediction)
            classID = np.argmax(prediction)
            className = classNames[classID]
        
    # show the prediction on the frame
            cv2.putText(frame, className, handednessTextCoords[handType], cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0,0,255), 2, cv2.LINE_AA)
            i+=1
        cv2.putText(frame, str(upCount), (300,300), cv2.FONT_HERSHEY_SIMPLEX, 
            1, (0,0,255), 2, cv2.LINE_AA)
    # Show the final output
    cv2.imshow("Output", frame) 

    if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and destroy all active windows
cap.release()

cv2.destroyAllWindows()