# Loading required modules
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# loading dataset
iris = datasets.load_iris()

# To show description of dataset
# print(iris.DESCR) 

# features and labels
features = iris.data
labels = iris.target

# label 0: setosa
# label 1: versicolour
# label 2: virginica

# printing a example
# print(features[0], labels[0]) 
# class is 0 => setosa

# Training the classifier
clf = KNeighborsClassifier();
clf.fit(features, labels)

predis = clf.predict([[5.1, 3.5, 1.4, 0.2]])
print(predis)