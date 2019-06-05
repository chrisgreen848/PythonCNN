# -*- coding: utf-8 -*-
import argparse
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#calculate area of label
def areaCalculation(w,h):
    labelArea = w * h
    return labelArea

def plotHistogram(areaList,total, binAmount):
    #hist calc
    plt.hist(areaList, bins=binAmount)
    plt.ylabel('Amount')
    plt.xlabel('Area')
    plt.show()

def saveListAsTextFile(textfile,areaCalculationList):
    
    for a in range(len(areaCalculationList)):
        line = str(areaCalculationList[a]) + "\n"
        textfile.write(line)
        
    
def generateTextFileName(filename):
    textFileName = filename.split("/")
    textFileName = textFileName[1].split(".")
    newTextFileName=textFileName[0]+'_area.csv'
    return newTextFileName

#command line arguements
parser = argparse.ArgumentParser(description='Plot histograms of labelled data')
parser.add_argument('--File', action='store', dest = 'filename',
                    help='CSV File location')
parser.add_argument('--bins', action='store', dest = 'binTotal',
                   
                    help='Amount of bins for histogram')

args = parser.parse_args()
print("File name is : ", args.filename)
print("Total bins are : ", args.binTotal)
binTotal = int(args.binTotal)
filename = args.filename



########main#########
maxValue = 0
minValue = 0
iterator = 0
areaList = []
listLength = 0
#generate text file name to save areas to
textfile = generateTextFileName(filename)
textfile = "DroneData/"+textfile
print("Textfile of areas will generate as '", textfile, "'")
#create new file for areas to be stored
f = open(textfile, "w+")
#f.close()
#parse text file and get values for area calculation
with open(filename) as csvfile:
    csvReader = csv.reader(csvfile,delimiter=',')
    for row in csvReader:
        w = int(row[4])
        h = int(row[5])
        
        #obtain min value of histogram limit
        areaList.append(areaCalculation(w, h))
        
        if minValue == 0:
            minValue = areaList[iterator]
        else:
            if areaList[iterator] < minValue:
                minValue = areaList[iterator]
                
         #obtain max value of histogram limit       
        if areaList[iterator] > maxValue:
            maxValue = areaList[iterator]
        iterator+=1 
            
listLength = len(areaList)            
       
print("Max hist value is : ", maxValue) #histogram upper limit
print("Min hist value is : ", minValue)#histogram lowerlimit
print("Total Histogram count is ", listLength)
    
plotHistogram(areaList, listLength, binTotal)       
saveListAsTextFile(f, areaList)    
f.close()

