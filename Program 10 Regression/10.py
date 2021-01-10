#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 12:10:29 2021

@author: aswin
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def kernel(point,xmat,k):
    m,n = xmat.shape
    weights = np.mat(np.eye((m)))
    for i in range(m):
        diff = point-xmat[i]
        weights[i,i] = np.exp((diff*diff.T)/(-2.0*k**2))
    return weights

def localWeight(point,xmat,ymat,k):
    wei = kernel(point,xmat,k)
    W = (xmat.T*(wei*xmat)).I*(xmat.T*(wei*ymat.T))
    return W

def locallyWeightedRegression(xmat,ymat,k):
    m,n = xmat.shape
    ypred = np.zeros(m)
    for i in range(m):
        ypred[i] = xmat[i]*localWeight(xmat[i],xmat,ymat,k)
    return ypred

dataFrame = pd.read_csv('tips.csv')

totalBill = np.array(dataFrame.total_bill)
tip = np.array(dataFrame.tip)

totalBillMatrix = np.mat(totalBill)
tipMatrix = np.mat(tip)

m = totalBillMatrix.shape[1]
print(m)

ones = np.mat(np.ones(m))

print(ones)

X = np.hstack((ones.T,totalBillMatrix.T))

ypred = locallyWeightedRegression(X,tipMatrix,10)

sortIndex = X[:,1].argsort(axis=0)
xSort = X[sortIndex][:,0]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(totalBill,tip, color="green")
ax.plot(xSort[:,1],ypred[sortIndex], color = "red", linewidth=5)
plt.xlabel("Total bill")
plt.ylabel("Tip")
plt.show()