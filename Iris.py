#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 15:20:20 2018

@author: AyushArora
"""
from sklearn.datasets import load_iris

iris = load_iris()
print iris.feature_names
print 
print iris.target_names
print
print iris.data[0]
print
print iris.target[0]
print
for i in range(len(iris.target)):
    print "Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i])
    
print

import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
test_idx = [0,50,100]

# training data
train_target = np.delete(iris.target,test_idx)
train_data = np.delete(iris.data, test_idx, axis = 0)

# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print test_target
print
print clf.predict([[5.1,3.5,1.4,0.2]])
print clf.predict([[7.0,3.2,4.7,1.4]])
print clf.predict([[6.3,3.3,6.0,2.5]])


