#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 21:01:18 2021

@author: aswin
"""

import csv

def read_data(filename):
    with open(filename,'r') as csvFile:
        datareader = csv.reader(csvFile,delimiter=',')
        headers = next(datareader)
        metadata = []
        traindata = []
        for name in headers:
            metadata.append(name)
        for row in datareader:
            traindata.append(row)
        
        return (metadata,traindata)