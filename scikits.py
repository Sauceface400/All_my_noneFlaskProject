from sklearn import svm
from sklearn import datasets

iris = datasets.load_iris()
print(type(iris))
print(iris.data)
print(iris.feature_names)
print(iris.target)
print(iris.target_names)
x = iris.data[:,2]
y = iris.target




