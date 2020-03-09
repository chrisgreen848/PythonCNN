
### ---- Information on how to use -------------

"""
Enter the file directory in to the 'Enter File Directory text box' and press button
If you want to add a name file to output names instead of class numbers, do the same for the enter .name File Loc (It will have to be as a text file though'
Use the class split button to generate class distributions

For test training file option -- This simply checks if there are any missing/corrupt images/ text files in your train file.
"""









from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
import glob
import shutil
import os
import cv2
import v4_training as v4
from os import path


def totalValueOfTally(tally):
    total = 0
    for i in range(len(tally)):
        total = tally[i] + total

    return total






class dataAnalysis(Widget):
    defaultPath = "/home/v4/DeepLearning/AlexeyAB/darknet/trainingImages/"
    defaultClassList = "/home/v4/DeepLearning/AlexeyAB/darknet/cfg/boatcoco.txt"
    defaultTrainingFile = ""
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
    test = "TestTestTestTestTest"

    ###------get file directoy entered on the user interface ------
    def getFileDirectory(self, inputText):
        if inputText != "":
            dataAnalysis.fileDirectory = inputText
        else:
            dataAnalysis.fileDirectory = dataAnalysis.defaultPath
        #print("You have set img directory to : ", dataAnalysis.fileDirectory)
        dataAnalysis.checkFiles(self)


        ## get name file and added to a list
    def getNameFileLoc(self, inputText):
        try:
            file = open(inputText, "r")
            for line in file:
                classLabel = line.rstrip()
                dataAnalysis.classList.append(classLabel)
            print(dataAnalysis.classList)
        except:
            print("Opening Textfile failed. Enter new Textfile")



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



    def checkFalseDetections(self, path):
        try:
            file = open(path, "r")
            for line in file:
                splitLine = line.split()
                classTruth = splitLine[1]
                classDetection = splitLine[2]
                imgLocation = splitLine[0]
                if classTruth != classDetection:
                    # print("falseDetection Class : ", classTruth, " with ", classDetection)
                    print("falseDetection Class : ", dataAnalysis.classList[int(classTruth)], " with ",
                          dataAnalysis.classList[int(classDetection)])
        except:
            print("File opening error. Please enter new file")



    #/ home / v4 / DeepLearning / AlexeyAB / darknet / data / falseDecs.txt
    #/ home / v4 / DeepLearning / AlexeyAB / darknet / cfg / boatcoco.txt


    ## ---- check if list has number already, if not append -----
    def appendClassListAndTally(self, label):
        seenFlag = 0
        if len(dataAnalysis.classNumbers) == 0:
            dataAnalysis.classNumbers.append(label)
            dataAnalysis.classNumbersTally[0] = 1
            ## search array
        else:
            #print("List not empty")
            print(dataAnalysis.classNumbers)
            for i in range(len(dataAnalysis.classNumbers)):


                if int(label) == int(dataAnalysis.classNumbers[i]):

                    seenFlag = 1

                    dataAnalysis.classNumbersTally[i] = dataAnalysis.classNumbersTally[i] + 1



            if seenFlag == 0:

                dataAnalysis.classNumbers.append(label)

                dataAnalysis.classNumbersTally.append(1)


    def matchClasses(self):
        for i in range(len(dataAnalysis.classNumbers)):

            classNum = int(dataAnalysis.classNumbers[i])

            if dataAnalysis.classList != []:
                print("CLASS :", dataAnalysis.classList[classNum], " has ", dataAnalysis.classNumbersTally[i], " labels")
            else:
                print("No Class List has been entered. Displaying NUmbers!")
                print("CLASS NUMBER : ", dataAnalysis.classNumbers[i], " has ", dataAnalysis.classNumbersTally[i], "Objects present")


    def checkTrainingFile(self, txt):
        it = 0
        try:
            file = open(txt, "r")
            for line in file:

                jpgLocation = line
                jpgLocation = jpgLocation.rstrip()
                txtLocation = v4.jpgToTxt(jpgLocation)

                check = path.exists(jpgLocation)
                if check == False:
                    print(jpgLocation, "failed")

                check = path.exists(txtLocation)
                if check == False:
                    print(txtLocation, "failed")

                ##OPEN TEXT file and check labels

                txtF = open(txtLocation, "r")
                for label in txtF:
                    lblSplit = label.split()
                    if float(lblSplit[1]) > 1.0 or float(lblSplit[2]) > 1.0 or float(lblSplit[3]) > 1.0 or float(
                            lblSplit[4]) > 1.0:
                        print("textfile :", txtLocation, "Corrupt")

                # print(path.exists(jpgLocation))
                # print(path.exists(txtLocation))

                it = it + 1
        except:
            print("Failed opening file, try better location")

##temp name files   /home/v4/DeepLearning/AlexeyAB/darknet/cfg/boatcoco.txt
##temp image file   /home/v4/Datasets/boats/IndividualClassPhotos/cocoreclassedrelabeled/




class dataApp(App):

    def build(self):

        return dataAnalysis()


if __name__ == '__main__':


    dataApp().run()
