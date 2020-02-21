from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import csv
from matplotlib import pyplot as plt
import seaborn as sn
from sklearn.metrics import confusion_matrix
import pandas as pd
import sklearn.metrics
import numpy as np
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
# Hopefully this damn things finds optimal parameters
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [.001, .01, .1, 1, 10, 100], 'C': [1, 10, 100, 1000]},
                   {'kernel': ['linear'], 'C':[1,10,100,1000]}]
grid = GridSearchCV(estimator= svm, param_grid= tuned_parameters, scoring='accuracy', n_jobs=-1)
grid.fit(X_train, y_train)
print("Best score is ", grid.best_score_)
print("Best C is ", grid.best_estimator_.C)
print("Best Kernel: ", grid.best_estimator_.kernel)
print("Best Gamma: ", grid.best_estimator_.gamma)

# Gives Precision and accuracy scores to 3 decimal places
print(sklearn.metrics.classification_report(y_test, predictions, digits=3 ))
# Prints test and predicted data into a heatmap of a confusion matrix
df_cm = pd.DataFrame(confusion_matrix(y_test, predictions))
sn.set(font_scale=1) # for label size
confusion = sn.heatmap(df_cm, annot=True, annot_kws={"size": 12}, xticklabels=(100, 200, 300, 400, 500, 600),
           yticklabels=(100,200,300,400,500,600), cbar=False, ) # font size
confusion.set(title= 'SVM Confusion Matrix',
              xlabel="Predictions",
              ylabel='Real Values',)

# print the accuracy score
print('Score: ', clf.score(X_test, y_test))

# plot the predictions vs the true y-vals (scatter will be more linear the better the model is)
plt.scatter(y_test, predictions)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.title('SVM Predicted Values vs Actual Values for X_test of Parkinson\'s Data')
plt.legend()
plt.show()
