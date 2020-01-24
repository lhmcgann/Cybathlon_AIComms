from sklearn import svm
import csv
# take as input two arrays: an array X of size [n_samples, n_features] holding
#   the training samples, and an array y of class labels (strings or integers),
#   size [n_samples]

# initialize lists to hold data
input = []
stage = []

#open data file
with open('../data/usable_input_data.csv','r') as csvFile:

    plots = csv.reader(csvFile, delimiter=',')
    #read data into memory
    for column in plots:
        vector = [float(column[1]), float(column[2])]
        input.append(vector)
        stage.append(float(column[3]))

# create the svm
clf = svm.SVC()
clf.fit(input, stage)

# After being fitted, the model can then be used to predict new values:
print(clf.predict([[2., 2.]]))

# get support vectors
print(clf.support_vectors_)
# get indices of support vectors
print(clf.support_)
# get number of support vectors for each class
print(clf.n_support_)
