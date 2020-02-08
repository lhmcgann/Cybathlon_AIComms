from sklearn import svm
from sklearn.model_selection import train_test_split
import csv
from matplotlib import pyplot as plt
# take as input two arrays: an array X of size [n_samples, n_features] holding
#   the training samples, and an array y of class labels (strings or integers),
#   size [n_samples]

# initialize lists to hold data
X = []
y = []

# open data file
with open('../data/usable_input_data.csv','r') as csvFile:

    plots = csv.reader(csvFile, delimiter=',')
    #read data into memory
    for column in plots:
        vector = [float(column[1]), float(column[2])]
        X.append(vector)
        y.append(float(column[3]))

# split into test and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# create the svm
clf = svm.SVC()
clf.fit(X_train, y_train)

# get support vectors
print(clf.support_vectors_)
# get indices of support vectors
print(clf.support_)
# get number of support vectors for each class
print(clf.n_support_)


# After being fitted, the model can then be used to predict new values:
predictions = clf.predict(X_test)

# print the accuracy score
print('Score: ', clf.score(X_test, y_test))

# plot the predictions vs the true y-vals (scatter will be more linear the better the model is)
plt.scatter(y_test, predictions)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.title('SVM Predicted Values vs Actual Values for X_test of Parkinson\'s Data')
plt.legend()
plt.show()
