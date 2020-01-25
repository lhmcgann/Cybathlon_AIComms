import matplotlib.pyplot as plt
import csv
import tensorflow as tf


def main() :
    dataSet = []

    with open('outputWithRegression.csv','r') as csvFile :
        data = csv.reader(csvFile, delimiter=',')
        
        for column in data :
            dataSet.append([float(column[1]),
            float(column[2]), 
            float(column[4])])
    
    
    dataset = tf.data.Dataset.from_tensor_slices(dataSet)
    for element in dataset :
        print(element)

    #print(dataSet[0])

main()
