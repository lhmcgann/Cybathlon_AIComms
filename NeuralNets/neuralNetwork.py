'''
* Neural Network
*
* Dimitri Charitou, Evan Morris, Dylan Mooers
* Cal Poly QL+ Cybathlon
* 01/25/2020
'''

import matplotlib.pyplot as plt
import csv
import tensorflow as tf
import numpy as np

# string -> (tf.data.Dataset, tf.data.Dataset, tf.data.Dataset])
# Returns a list of three dataset objects, [training dataset, validation dataset, testing dataset]
# Arrays are broken up into 85% training, 5% validation, 10% testing
def loadData(filename):
	# change these variables for tweak percentages
	TRAINING_PERCENTAGE = 0.85
	VALIDATION_PERCENTAGE = 0.5
	TESTING_PERCENTAGE = 0.10

	dataset = []
	trainingDataset = []
	validationDataset = []
	testingDataset = []

	with open(filename,'r') as csvFile :
		data = csv.reader(csvFile, delimiter=',')
		
		
		# read data into memory
		for column in data :
			dataset.append([float(column[0]), float(column[1]), float(column[2])])

		# partitions data into three distinct chunks
		trainingDataset = dataset[0 : int(len(dataset) * TRAINING_PERCENTAGE)]
		validationDataset = dataset[int(len(dataset) * TRAINING_PERCENTAGE) : 
			int(len(dataset) * VALIDATION_PERCENTAGE)]
		testingDataset = dataset[int(len(dataset) * VALIDATION_PERCENTAGE) :]

	print(type(tf.data.Dataset.from_tensor_slices(trainingDataset)))
	return (tf.data.Dataset.from_tensor_slices(trainingDataset), 
		int(len(dataset) * TRAINING_PERCENTAGE), 
		tf.data.Dataset.from_tensor_slices(validationDataset),
		tf.data.Dataset.from_tensor_slices(testingDataset))


def main():
	dataset = loadData('../data/outputWithRegression.csv')


if __name__ == '__main__':
	main()
