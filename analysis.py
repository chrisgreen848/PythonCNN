from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
import glob
import shutil
import os
import cv2
import v4_training as v4


def totalValueOfTally(tally):
    total = 0
    for i in range(len(tally)):
        total = tally[i] + total

    return total






class dataAnalysis(Widget):
    bob = 0
    fileDirectory = ""
    textFileTotal = 0
    jpgfileTotal = 0
    jpgFileList = []
    txtFileList = []
    classNumbers = []
    classNumbersTally = [None]
    labelCount = 0
    nameFileLoc = "" #so we can match classes
    classList = []

    ###------get file directoy entered on the user interface ------
    def getFileDirectory(self, inputText):
        dataAnalysis.fileDirectory = inputText
        #print("You have set img directory to : ", dataAnalysis.fileDirectory)
        dataAnalysis.checkFiles(self)


        ## get name file and added to a list
    def getNameFileLoc(self, inputText):
        file = open(inputText, "r")
        for line in file:
            classLabel = line.rstrip()
            dataAnalysis.classList.append(classLabel)
        print(dataAnalysis.classList)


    ##check how many jpg and txt files there are and if there's an even match
    def checkFiles(self):
        ##reset totals
        dataAnalysis.jpgfileTotal = 0
        dataAnalysis.textFileTotal = 0
        print("file is: ", dataAnalysis.fileDirectory)
        for file in os.listdir(dataAnalysis.fileDirectory):
            if file.endswith(".txt"):
                dataAnalysis.txtFileList.append(file)
                dataAnalysis.textFileTotal = dataAnalysis.textFileTotal + 1
            elif file.endswith((".jpg")):
                dataAnalysis.jpgFileList.append(file)
                dataAnalysis.jpgfileTotal = dataAnalysis.jpgfileTotal + 1


        print("Total jpg files are :", dataAnalysis.jpgfileTotal)
        print("Total text files are :", dataAnalysis.textFileTotal)
        if dataAnalysis.jpgfileTotal != dataAnalysis.textFileTotal:
            print("Uneven file amount. Missing a text or jpgfile")
        elif dataAnalysis.jpgfileTotal == 0 and dataAnalysis.textFileTotal > 0:
            print("No Jpg Files available")
        elif dataAnalysis.textFileTotal == 0 and dataAnalysis.jpgfileTotal > 0:
            print("No Text files available")
        elif dataAnalysis.textFileTotal == 0 and dataAnalysis.jpgfileTotal == 0:
            print("No Jpg files or text files, consider trying new directory")

    def getClassSplit(self):
        try:
            for file in os.listdir(dataAnalysis.fileDirectory):
                if file.endswith(".txt"):
                    fileLoc = dataAnalysis.fileDirectory + file
                    labelFile = open(fileLoc, "r")
                    for line in labelFile:
                        print(line)
                        lineSplit = line.split()
                        currentLabel = lineSplit[0]
                        #print("Current label is : ", currentLabel)
                        print("appending list")
                        dataAnalysis.appendClassListAndTally(self, currentLabel)
                        print("appended labeled")
                        dataAnalysis.labelCount = dataAnalysis.labelCount + 1


        except:
            print("Error, try again")

        print("class number list is :", dataAnalysis.classNumbers)
        #dataAnalysis.classNumbers.sort()
        #print("Sorted list is : ", dataAnalysis.classNumbers)
        #dataAnalysis.classNumbersTally = [None] * len(dataAnalysis.classNumbers)
        print("Tally is : " , dataAnalysis.classNumbersTally)
        print("Total labels are :", dataAnalysis.labelCount)
        print("Total Value of Tally is : ", totalValueOfTally(dataAnalysis.classNumbersTally))
        if dataAnalysis.labelCount == totalValueOfTally(dataAnalysis.classNumbersTally):
            print("tally and list match")
            dataAnalysis.matchClasses(self)

        else:
            print("Tally and list don't match, something has gone wrong")








    ## ---- check if list has number already, if not append -----
    def appendClassListAndTally(self, label):
        seenFlag = 0
        if len(dataAnalysis.classNumbers) == 0:
            dataAnalysis.classNumbers.append(label)
            dataAnalysis.classNumbersTally[0] = 1
            print("Appended first element")
            ## search array
        else:
            #print("List not empty")
            print(dataAnalysis.classNumbers)
            for i in range(len(dataAnalysis.classNumbers)):


                if int(label) == int(dataAnalysis.classNumbers[i]):

                    seenFlag = 1
                    p
                    dataAnalysis.classNumbersTally[i] = dataAnalysis.classNumbersTally[i] + 1



            if seenFlag == 0:

                dataAnalysis.classNumbers.append(label)

                dataAnalysis.classNumbersTally.append(1)


    def matchClasses(self):
        for i in range(len(dataAnalysis.classNumbers)):

            classNum = int(dataAnalysis.classNumbers[i])
            print("CLASS :", dataAnalysis.classList[classNum], " has ", dataAnalysis.classNumbersTally[i], " labels")





##temp name files   /home/v4/DeepLearning/AlexeyAB/darknet/cfg/boatcoco.txt
##temp image file   /home/v4/Datasets/boats/IndividualClassPhotos/cocoreclassedval/




class dataApp(App):

    def build(self):

        return dataAnalysis()


if __name__ == '__main__':


    dataApp().run()
