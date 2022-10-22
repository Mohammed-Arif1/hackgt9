# TechVidvan hand Gesture Recognizer

# import necessary packages

import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model

# initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils
handednessTextCoords = {
    "Left":(10, 50),
    "Right":(550, 50)
}
# Load the gesture recognizer model
model = load_model('mp_hand_gesture')

# Load class names
f = open('gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)


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
        for handslms in result.multi_hand_landmarks:
            landmarks = []
            for lm in handslms.landmark:
                print(id, lm)
                lmx = int(lm.x * x)

                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            # Predict gesture
            prediction = model.predict([landmarks])
            print(prediction)
            classID = np.argmax(prediction)
            className = classNames[classID]

    # show the prediction on the frame
            handType = result.multi_handedness[i].classification[0].label
            cv2.putText(frame, className, handednessTextCoords[handType], cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0,0,255), 2, cv2.LINE_AA)
            i+=1

    # Show the final output
    cv2.imshow("Output", frame) 

    if cv2.waitKey(1) == ord('q'):
        break

# release the webcam and destroy all active windows
cap.release()

cv2.destroyAllWindows()