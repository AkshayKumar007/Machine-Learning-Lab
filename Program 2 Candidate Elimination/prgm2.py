#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:19:47 2021

@author: aswin
"""

import csv
a = []
print("\n The Given Training Dataset \n")

with open('enjoysport.csv','r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        a.append(row)
        print(row)
num_attributes = len(a[0]) - 1

print("\n The initial Value of hypothesis: ")
S = ['0']*num_attributes
G = ['?']*num_attributes

print("\n The most specific hypothesis S0 : [0,0,0,0,0,0]\n")
print("\n The most general hypothesis G0 : [?,?,?,?,?,?]\n")


for j in range(0,num_attributes):
    S[j] = a[0][j];
    

print("\nCandidate Elimination Algorithm Hypothesis Version Space Computation\n")
temp = []

for i in range(0,len(a)):
    print("--------------------------------------------")
    if a[i][num_attributes] == 'Yes':
        for j in range(0,num_attributes):
            if a[i][j] != S[j]:
                S[j]='?'
                
        for j in range(0,num_attributes):
            for k in range(1,len(temp)):
                if temp[k][j] != '?' and temp[k][j] != S[j]:
                    del temp[k]
                    
        print("For Training Example No : {0} the hypothesis is S{0} ".format(i+1),S)
        if(len(temp) == 0):
            print("For Training Example No : {0} the hypothesis is G{0} ".format(i+1),G)
        else :
            print("For Training Example No : {0},the hypothesis is G{0} ".format(i+1),temp)
            
    if a[i][num_attributes] == 'No':
        for j in range(0,num_attributes):
            if S[j] != a[i][j] and S[j]!='?':
                G[j] = S[j]
                temp.append(G)
                G = ['?']*num_attributes
                
        print("For Training Example No :{0} the hypothesis is S{0} ".format(i+1),S)
        print("For Training Example No :{0} the hypothesis is G{0} ".format(i+1),temp)
            
            
            
            
            
            
            
            