# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from sklearn import tree

'''Data Set'''
'''Weight, 1 is smooth, 0 is bumpy'''
features = [[140,1], [130,1], [150,0], [170,1]]
''' 0 is apple, 1 is orange'''
labels = [0,0,1,1]

'''Decision Tree'''
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

'''Testing'''
print clf.predict([[160,0]])
print clf.predict([[135,0]])

