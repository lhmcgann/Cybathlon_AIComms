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
import tensorflow_docs.plots
import tensorflow_docs.modeling
import buildDataSet

def buildModel(trainDataSet) :
    """This builds the model with three distinct layers, based off of the shape of
    our training dataset (3)"""

    model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[len(trainDataSet.keys())]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
  ])

    optimizer = tf.keras.optimizers.RMSprop(0.001)

    model.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])
    return model

def norm(x) :
    """This normalizes the raw data"""
    return (x - train_stats['mean']) / train_stats['std']

def trainModel(model, trainDataSet, testData, testLabels, trainLabels) :
    """Trains the data for 100 epochs - anything past 100 epochs only provides marginal
    benefit and isnt worth the time"""

    EPOCHS = 100

    history = model.fit(
        trainDataSet, trainLabels,
        epochs=EPOCHS, validation_split = 0.2, verbose=0,
        callbacks=[tfdocs.modeling.EpochDots()])
    """Normally this would not go in the training function but I just wanted to make
    sure it works"""

    testPredictions = model.predict(testData).flatten()
    """Plots the expected vs actual"""
    a = plt.axes(aspect='equal')
    plt.scatter(testLabels, testPredictions)
    plt.xlabel('True Values [Gait]')
    plt.ylabel('Predictions [Gait]')
    lims = [0, 50]
    plt.xlim(lims)
    plt.ylim(lims)
    _ = plt.plot(lims, lims)
    


def main() :
    dataSet = buildDataSet.generateDataSet('outputWithRegression.csv')
    trainDataSet = dataSet[0]
    testData = dataSet[1]
    trainLabels = trainDataSet.pop("Gait")
    testLabels = testData.pop("Gait")
    model = buildModel(trainDataSet)

    trainModel(model, trainDataSet, testData, testLabels, trainLabels)

if __name__ == "__main__" :
    main()
