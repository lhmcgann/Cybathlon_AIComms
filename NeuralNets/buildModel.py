from __future__ import absolute_import, division, print_function, unicode_literals 
import pathlib

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_docs as tfdocs
import neuralNetwork

# Builds the model for the Neural Net
# Takes in
def main() :
    dataSets = neuralNetwork.loadData('outputWithRegression.csv')
    model = createModel(dataSets)
    for i in range(4) :
        if (i != 1) :
            print(dataSets[i].shape())

    #model.fit(dataSets[0])
    #model.predict(dataSets[2])


    #print(model.summary())

def createModel(dataSets) :
    model = tf.keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=[1]),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])

    optimizer = tf.keras.optimizers.RMSprop(0.001)

    model.compile(loss='mse', 
    optimizer=optimizer,
    metrics=['mae', 'mse'])

    return model

if __name__ == '__main__' :
    main()
    