from kivy.app import App
from kivy.uix.widget import Widget
import numpy as np
import pandas as pd
import threading
from kivy.clock import Clock

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
import glob
import shutil
import os
import cv2
import v4_training as v4
from os import path

def scanArrayForPopulatedValues(array, classList):
    newArray = []
    row = 0
    col = 0
    sizeOfx = 0
    sizeOfY = 0
    minHitNum = 0
    maxHitNumber = 0
    for i in(range(len(array))):
        classHitFlag = 0
        for j in range(len(array[0])):
            if array[i][j] != 0:
                if minHitNum == 0:
                    minHitNum= j
                if i > maxHitNumber:
                    maxHitNumber = i

    print("MIN IS : ", minHitNum, "MAX IS: ", maxHitNumber)


    size = maxHitNumber-minHitNum
    size = size + 1 # conpensate for 0 vlaue
    newArray = np.zeros((size,size))
    for i in range(size):

        for j in range(size):
            print("(", minHitNum+i, "," , minHitNum+j, ")")

            newArray[i][j] = array[minHitNum+i][minHitNum+j]
            print(newArray[i][j])

    for i in range(minHitNum, maxHitNumber):
        print(classList[i],"  ", end='')
    print("\n")
    print(newArray)
    return(newArray)















class confusionMatrix(Widget):

    defaultPath = "/home/v4/DeepLearning/AlexeyAB/darknet/data/falseDecs.txt" # default path
    defaultClassListPath = "/home/v4/DeepLearning/AlexeyAB/darknet/cfg/boatcoco.txt"
    path = ""
    classString = ""
    classListPath = ""
    classList = []     ## name file list i.e cat,dog, etc
    detFileList = []   ## detection file list  # format of img loc, true class, detected class, truth box, det box
    totalClasses = 0
    detectionAmount = 0
    confusionMatrix = np.zeros((1, 1)) #default one class confusion matrix of seroes





    ##### ----------------- get file functions --------------- #######
    ## ----------- Get file directory of detections file ------- ##
    def getFileDirectory(self, inputText): # get file save into class member
        confusionMatrix.path = inputText
        if confusionMatrix.path == "":
            print("Default path set  ")
            confusionMatrix.path = confusionMatrix.defaultPath

        print("Detection File is :", inputText )
        file = open(confusionMatrix.path, "r")
        for line in file:
            confusionMatrix.detFileList.append(line)
        #print(confusionMatrix.detFileList)
        confusionMatrix.detectionAmount = len(confusionMatrix.detFileList)
        #print(confusionMatrix.detectionAmount) # PRINT detection amount if needed
        #print("You have set img directory to : ", dataAnalysis.fileDirectory) # print directory if needed

    ## ------------ Get names text file variant of the yolo weights ------ ####
    def getNameFileLoc(self, inputText):
        confusionMatrix.path = inputText
        if inputText == "":
            print("Default path set  ")
            inputText = confusionMatrix.defaultClassListPath
        file = open(inputText, "r")
        for line in file:
            classLabel = line.rstrip()
            confusionMatrix.classList.append(classLabel)
        confusionMatrix.totalClasses = len(confusionMatrix.classList)
        print(confusionMatrix.classList, "of size", confusionMatrix.totalClasses )



    def createConfusionMatrix(self):
        confusionMatrix.confusionMatrix = np.zeros((confusionMatrix.totalClasses, confusionMatrix.totalClasses)) # create 2d matrix of total classes * total classes
        ## now sort text file in to numbers to put in to matrix file
        for i in range(confusionMatrix.detectionAmount):
            detectionSplit = confusionMatrix.detFileList[i].split()
            truthClass = int(detectionSplit[1])
            detectionClass = int(detectionSplit[2])
            confusionMatrix.confusionMatrix[truthClass][detectionClass] = confusionMatrix.confusionMatrix[truthClass][detectionClass] + 1
        print(confusionMatrix.confusionMatrix)
        #confusionMatrix.cMat = confusionMatrix.confusionMatrix.tostring()
        confusionMatrix.classString = '|'.join(confusionMatrix.classList)
        #threading.Thread(target=self.change_text()).start()
        #Clock.schedule_interval(self.change_text(), 0.5)
        print(confusionMatrix.classString)
        pd.DataFrame(confusionMatrix.confusionMatrix).to_csv("cMat.csv")
        scanArrayForPopulatedValues(confusionMatrix.confusionMatrix, confusionMatrix.classList)

    def change_text(self):
        print("I have changed maybe")
        confusionMatrix.classString = "I have changed"








class confusionApp(App):

    def build(self):

        return confusionMatrix()


if __name__ == '__main__':


    confusionApp().run()
