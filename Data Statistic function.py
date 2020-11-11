# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 11:38:29 2020

@author: ollie
"""

import numpy as np
# Takes a N by 3 matrix and a string as input.
# Outputs a scalar value desribing the statistic input.
def dataStatistics(data, statistic):
    
    # numpy function mean computes the average, i.e. the sum of all elements
    #in the first column of data matrix, and divides by the amoun of elements.
    if statistic == "Mean Temperature":
        result = np.mean(data[:,0]) 
        
    elif statistic == "Mean Growth rate":
        result = np.mean(data[:,1]) 
    
    # Computes the standard deviation, i.e. the square root of the average of the
        #squared deviations from the mean.           
    elif statistic == "Std Temperature":
        result = np.std(data[:,0]) 
        
    elif statistic == "Std Growth rate":
        result = np.std(data[:,1]) 
    
    # Counts amount of elements in first column          
    #result = np.size(data[:,1])
    elif statistic == "Rows":
        result = len(data) 
    
    # Creates a new array. For all rows, check if the temperature is under 20.       
    # If so, then add to new array and lastly compute mean. 
    elif statistic == "Mean Cold Growth rate":
        coldData = np.array([])
        for c in range(len(data[:,0])):
            if data[c,0] < 20:
                coldData = np.append(coldData, data[c,1])    
        result = np.mean(coldData) 
        
    elif statistic == "Mean Hot Growth rate":
        hotData = np.array([])
        for h in range(len(data[:,0])):
            if data[h,0] > 50:
                hotData = np.append(hotData, data[h,1])    
        result = np.mean(hotData) 
    
    # fjerne denne else og sætte i stedet tjekke gyldighed af statistic input i hovedscript
    else:
        print("Invalid statistic")
        result = 0
        
    return result
    
    
#print(dataStatistics(np.array([[24.297, 0.86149, 1],
#[37.183, 0.85134, 1],[59.239, 0.058406, 1],
#[28.616, 0.62475, 2],[43.739, 0.70429, 3]]),
#"Mean Temperature"))

#print(dataStatistics(np.array([[15.852, 0.45917, 3],
#[37.183, 0.85134, 1],[59.239, 0.058406, 1],
#[28.616, 0.62475, 2],[43.739, 0.70429, 3]]),
#"Mean Hot Growth rate"))
#"Mean Growth rate"))
#"Rows"))

#print(dataStatistics(np.array([[15.852, 0.45917, 3],
#[14.769, 0.17958, 4],[59.239, 0.058406, 1],
#[28.616, 0.62475, 2],[17.326, 0.23037, 4],
#[51.329, 0.50498, 3],[56.675, 0.40291, 2],
#[50.734, 0.52373, 3],[50.019, 0.4754, 1],
#[71.663, 0.9012, 1]]),"Mean Hot Growth rate"))




