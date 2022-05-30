# Train a logistic regression classifier to predict whether
# a flower is iris virginica or not

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt

iris = datasets.load_iris()

# print(iris.keys())
# print(iris.data)  # features
# print(iris.target)  # labels

# label 0: setosa
# label 1: versicolour
# label 2: virginica

x = iris["data"][:, 3:]  # taking all rows of 3rd column
y = (iris["target"] == 2).astype(int)

# Train a logistic regression classifier
clf = LogisticRegression()
clf.fit(x, y)

example = clf.predict(([[2.6]]))
print(example)

# Using matplotlib to plot the visualization
x_new = np.linspace(0, 3, 1000).reshape(-1, 1)
y_prob = clf.predict_proba(x_new)
# print(x_new)
plt.plot(x_new, y_prob[:, 1], "g-", label="virginica")
plt.show()
