import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np

def getModel():
    model = load_model('mp_hand_gesture')
    f = open('gesture.names', 'r')
    classNames = f.read().split('\n')
    f.close()
    return model, classNames

def getGestures(landmarks, model, classNames):
    className = ''
    prediction = model.predict(tf.convert_to_tensor([landmarks])) 
    #the landmarks are where the indices of all the hand points are stored. its a list of coordinates
    classID = np.argmax(prediction)
    className = classNames[classID]

    return className