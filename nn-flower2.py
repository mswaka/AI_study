# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 20:07:04 2020

@author: chimochimo
"""

from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Activation, Dense
from keras.utils import np_utils
import numpy as np

classes = 3
data_size = 75 * 75 * 3

def main():
    data = np.load("./photo-min.npz")
    x = data["x"]
    y = data["y"]
    
    x = np.reshape(x, (-1, data_size))
    x_train, x_test, y_train, y_test = train_test_split(x, y)
    
    model = train(x_train, y_train)
    model_eval(model, x_test, y_test)
    
def train(x, y):
    model = Sequential()
    model.add(Dense(units=64, input_dim=(data_size)))
    model.add(Activation('relu'))
    model.add(Dense(units=classes))
    model.add(Activation('softmax'))
    model.compile(loss='sparse_categorical_crossentropy', 
                  optimizer='sgd', metrics=['accuracy'])
    model.fit(x, y, epochs=60)
    model.save_weights("flower.hdf5")
    return model

def model_eval(model, x_test, y_test):
    score = model.evaluate(x_test, y_test)
    print('loss=', score[0])
    print('accuracy=', score[1])
    
if __name__ == "__main__":
    main()
