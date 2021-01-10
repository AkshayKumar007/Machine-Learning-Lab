# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 00:29:03 2021

@author: Pratyush
"""

from numpy import *
import matplotlib.pyplot as plt
import pandas as pd

def kernel(point,xmat, k):
    m,n = shape(xmat)
    weights = mat(eye((m)))
    for j in range(m):
        diff = point - xmat[j]
        weights[j,j] = exp(diff*diff.T/(-2.0*k**2))
    return weights

def localWeight(point,xmat,ymat,k):
    wei = kernel(point,xmat,k)
    W = (X.T*(wei*X)).I*(X.T*(wei*ymat.T))
    return W

def localWeightRegression(xmat,ymat,k):
    m,n = shape(xmat)
    print('Shape xmat',xmat.shape)
    ypred = zeros(m)
    print('yPred shape:',ypred.shape)
    for i in range(m):
        print(xmat[i])
        ypred[i] = xmat[i]*localWeight(xmat[i],xmat,ymat,k)
    return ypred

data = pd.read_csv("tips.csv")
bill = array(data.total_bill)
tip = array(data.tip)
print('bill',bill)
print('tip',tip)
mbill = mat(bill)
mtip = mat(tip)

print('mbill',mbill.shape)
print('mtip',mtip)
m= shape(mbill)[1]
one = mat(ones(m))
print('one',one)
X= hstack((one.T,mbill.T))

print('X',X)
#set k here
ypred = localWeightRegression(X,mtip,10)
print('ypred',ypred)
SortIndex = X[:,1].argsort(0)
print('sort index',SortIndex)
xsort = X[SortIndex][:,0]
print(xsort)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(bill,tip, color="green")
ax.plot(xsort[:,1],ypred[SortIndex], color = "red", linewidth=5)
plt.xlabel("Total bill")
plt.ylabel("Tip")
plt.show()