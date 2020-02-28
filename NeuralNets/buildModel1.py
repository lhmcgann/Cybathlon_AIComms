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

def buildModel(trainDataSet, trainLabels) :
    """This builds the model with three distinct layers, based off of the shape of our training dataset"""
    
    model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[len(trainDataSet.keys())]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
  ])


    optimizer = tf.keras.optimizers.RMSprop(0.001)

    model.compile(loss='mse',
                optimizer=optimizer,
                metrics=[tf.keras.metrics.Accuracy()]) # 'mae', 'mse'])
    return model

def norm(x) :
    """This normalizes the raw data"""
    return (x - train_stats['mean']) / train_stats['std']

def trainModel(model, trainDataSet, testData, testLabels, trainLabels) :
    """Trains the data for 100 epochs - anything past 100 epochs only provides marginal benefit and isnt worth the time"""

    EPOCHS = 150

    history = model.fit(
        trainDataSet, trainLabels,
        epochs=EPOCHS, validation_split = 0.2, verbose=1,
        callbacks=[tfdocs.modeling.EpochDots()])
    
def testModel(model, testData, testLabels) :
    testPredictions = model.predict(testData).flatten()
    return testPredictions
    #testLeft = testData.pop("Left foot")
    #testRight = testData.pop("Right foot")
    #time = [i for i in range(len(testLabels))]
    
   
    """
    # Uncomment to plot actual v expected
    plt.figure(figsize=(15,6))
    plot left foot force by x
    plt.plot(time, testLeft, color='blue', label='Left Foot')
    plot right foot force by y
    plt.plot(time, testRight, color='red', label='Right Foot')
    plot gait 
    plt.plot(time, testPredictions,color='green', label='Predicted Gait')
    plt.plot(time, testLabels,color='blue', label='Actual Gait')
    set range for x axis (X axis is truncated for readability)
    plt.xlim([0.0, 500.0])
    
    plt.xlabel('Time (seconds)')
    plt.ylabel('Force (N)')
    plt.title('Gait in Parkinson\'s Disease')
    plt.legend()
    plt.show()
    """

def calcPercentError(testLabels, predictions) :
    errors = []
    train = []
    predict = []
    averagePercentError = 0
    averageError = 0

    for data in testLabels :
        train.append(data)
    
    for data in predictions :
        predict.append(data)

    for i in range(len(train)) :
        difference = abs(predict[i] - train[i])
        error = difference
        errors.append(error)
        averageError += error
        averagePercentError += error / train[i]

    averageError = averageError / len(errors)
    averagePercentError = averagePercentError / len(errors)
    print("Your average error is:", averageError)
    print("Your average percent error is:", averagePercentError * 100, "%")
    print("Your average accuracy is:", 
            str((1 - averagePercentError) * 100) + "%")
    

    
   

"""
To do: Generate a new dataset by using the parkinson data, except add a random 
number from 0 to 130 to each data point for left sensor or right sensor
Use this data to both train and test the neural net and see how it handles / if 
it can see through the marginal error introduced by a random number addition
"""

def main() :
    dataSet = buildDataSet.generateDataSet('../data/outputWithRegression.csv')
    trainDataSet = dataSet[0]
    testData = dataSet[1]
    trainLabels = trainDataSet.pop("Gait")
    testLabels = testData.pop("Gait")
    model = buildModel(trainDataSet, trainLabels)

    trainModel(model, trainDataSet, trainDataSet, trainLabels, trainLabels)
    predictions = testModel(model, testData, testLabels)
    calcPercentError(testLabels, predictions)

if __name__ == "__main__" :
    main()
