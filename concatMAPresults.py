# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 16:50:30 2020

@author: chris
"""

import glob
import os

#Dir = "D:/tekvids/imgs/weights/boattinythird/"
Dir = "Y:/2020-VesselDetection/Annotations/weights/"
csvList = []
os.chdir(Dir)
csvtotals = 0
for file in glob.glob("*.csv"):
    loc = Dir + file
    csvList.append(loc)
    #print(loc)
    csvtotals+=1

csv = []
csvtwo = []
for i in range(len(csvList)):
    file = open(csvList[i], "r")
    csv.append(csvList[i])
    #print(csvList[i])
    for line in file:
        csv.append(line)
       
    csvtwo.append(csv)
    print(csvtwo[i])
    file.close()
    csv = []

newfile = Dir + "mapresults.csv"
file = open(newfile, "w+")
for i in range(len(csvtwo)):
    file.write(csvtwo[i][0])
    file.write("\n")
    file.write(csvtwo[i][1])
    
    file.write(csvtwo[i][2])
    file.write("\n")
    file.write("\n")

file.close()
    

"""
for i in range(len(csvtwo)):
    print(csvtwo[i][i])"""
"""   
for j in range(len(csvtwo)):
    for k in range(len(csvtwo[0])):
        print(csvtwo[i])
"""
#print(csvtwo[3])
    
  
