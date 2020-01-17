from sklearn import svm
# take as input two arrays: an array X of size [n_samples, n_features] holding
#   the training samples, and an array y of class labels (strings or integers),
#   size [n_samples]
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)
# After being fitted, the model can then be used to predict new values:
print(clf.predict([[2., 2.]]))

# get support vectors
print(clf.support_vectors_)
# get indices of support vectors
print(clf.support_)
# get number of support vectors for each class
print(clf.n_support_)
