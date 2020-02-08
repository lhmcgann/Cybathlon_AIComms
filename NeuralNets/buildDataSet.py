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

def generateDataSet(filePath) :
    """ Uses panda api to parse through CSV with the given column names and
    create a labeled, parseable dataset"""

    column_names = ['Left foot', 'Right foot', 'LeftFootSlope',
                    'RightFootSlope', 'Gait']
    raw_dataSet = pd.read_csv(filePath, names=column_names,
                    na_values = '?', comment='\t',
                    sep=",", skipinitialspace=True )
    dataSet = raw_dataSet.copy()
    dataSet = dataSet.dropna() # Drops null values and unknowns from the dataset
    
    trainDataSet = dataSet.sample(frac=0.8, random_state=0)
    testDataSet = dataSet.drop(trainDataSet.index)

    return [trainDataSet, testDataSet]
