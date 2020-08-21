# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:53:06 2020
Simple script to run yolo MAP on every set of weights in the current dir.
@author: chris
"""

import os 
import glob
#########Scan for all weights files and put in to list #########
holdDir = "Y:/2020-VesselDetection/Annotations/weights/"
os.chdir(holdDir)
fileNo = 0
weightsList = []
for file in glob.glob("*.weights"):
    weightsList.append(file)

print(weightsList)


newHoldDir = "D:/yolov4/darknet/Release/"
os.chdir(newHoldDir)
weightLoc = "Y:/2020-VesselDetection/Annotations/weights/"


for i in range(len(weightsList)):
    weights = weightLoc + weightsList[i]
    cfg = "D:/yolov4/darknet/cfg/boattiny.cfg"
    data =  "D:/yolov4/darknet/cfg/boat.data"
    prog = "darknet.exe detector map"
    command = prog + " " + data + " " + cfg +" " + weights
    cmd = "cmd /c"
    newCmd = cmd + ' "' + command + '"'
    print(newCmd)
    os.system(newCmd)

