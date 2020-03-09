from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
import glob
import shutil
import os
import cv2


def jpgToTxt(name):
    splitName = name.split(".")
    splitNameNew = splitName[0] + ".txt"
    return splitNameNew


def convertCoords(object, dimensions):
    imgHeight = float(dimensions[0])
    imgWidth = float(dimensions[1])
    centreX = float(object[1])
    centreY = float(object[2])
    W = float(object[3])
    H = float(object[4])
    """print(imgHeight)
    print(imgWidth)
    print(centreX)
    print(centreY)
    print(W)
    print(H)"""
    coords = [0.0] * 5  # class tlX tlY W H
    coords[0] = int(object[0])
    coords[1] = imgWidth * centreX
    coords[2] = imgHeight * centreY
    coords[3] = imgWidth * W
    coords[4] = imgHeight * H
    #print("Converted Coords are : " , coords)
    return coords



def getImgList(path):
    imgList = []
    for root, dir, files in os.walk(path):

        for name in files:
            if name.endswith((".jpg")):
                imageLocation = path + name
                imgList.append(imageLocation)
    return imgList

#def currentImgLoad():





class PongGame(Widget):
    screenMessage = "No Image Selected"
    #variables needed
    currentImg = 0 #position in list
    imgList = []
    txtFileList = []
    totalImgs = 0
    currentJpgFileLocation = ""
    currentTxtFileLocation = ""
    newTextFileLocation = "" #"/home/v4/Datasets/boats/boatValNewLabels/"
    path = ""
    ImgDimensions = []
    newLabel = ""
    imgDirect = ""
    labelList = []
    labelListSize = 0
    labelListPosition = 0
    filenotfound = 0

    #simple butotn press check
    def on_enter(instance, value):
        print('User pressed enter in', instance)

    #gets list of images and paths in the directory
    def getImgList(self):
        path = PongGame.imgDirect
        PongGame.imgList = getImgList(path)
        try:
            PongGame.imgList.insert(0,PongGame.imgList[0]) # seems to be a bug opening first image, so open it twice ? Fix later
            PongGame.screenMessage = "Image List Found"
        except:
            print("No images found, or False Directory. Try again")
            PongGame.screenMessage = "Image List Found not found."
        PongGame.totalImgs = len(PongGame.imgList)
        print("Your list contains : ", PongGame.totalImgs, "Images")
        #PongGame.screenMessage = "Image List Found not found."

    #gets info for next image and stores labels in a list
    def getNextImg(imgList):
        PongGame.screenMessage = "Image List Found not found."
        try:
            PongGame.labelList.clear()
            PongGame.labelListPosition = 0
            # PongGame.openImg(PongGame.imgList[PongGame.currentImg])
            PongGame.currentTxtfileLocation = jpgToTxt(
                PongGame.imgList[PongGame.currentImg])  # stores txt file path for this iteration
            PongGame.currentJpgFileLocation = PongGame.imgList[
                PongGame.currentImg]  # stores jpg location for this iteration

            print("Current txtfile is :", PongGame.currentTxtfileLocation)
            img = cv2.imread(PongGame.currentJpgFileLocation)
            cv2.imshow('img', img)
            cv2.startWindowThread()
            cv2.waitKey(10)
            PongGame.ImgDimensions = img.shape  # get image size
            print("Current Image is :", PongGame.currentJpgFileLocation)
            #### Get label List of Img
            try:
                textfile = open(PongGame.currentTxtfileLocation, "r")
                print("Text file : ", PongGame.currentTxtFileLocation, " is open")
                for line in textfile:
                    PongGame.labelList.append(line) ### save object label to list

                PongGame.labelListSize = len(PongGame.labelList)
                print(PongGame.labelList, "Of SIZE", PongGame.labelListSize)
            except:
                print("cannot open label file for this image")
            PongGame.currentImg = PongGame.currentImg + 1
        except:
            print("Failed on image : ", PongGame.currentJpgFileLocation)


    ## path /home/v4/Datasets/boats/NewProposedDataSet/boat_images[val]/
    def labelImg(self):
        #open Img and Txtfile

        if PongGame.labelListPosition < PongGame.labelListSize:
            try:
                #textfile = open(PongGame.currentTxtfileLocation, "r")
                #print("Text file : " , PongGame.currentTxtFileLocation, " is open")
                img = cv2.imread(PongGame.currentJpgFileLocation)

                cv2.imshow('img', img)  # show img
                PongGame.ImgDimensions = img.shape  # get image size
                #print("Dimensions of img are : ", PongGame.ImgDimensions)
                cv2.waitKey(10)
                dimensions = PongGame.ImgDimensions

                currentLabel = PongGame.labelList[PongGame.labelListPosition]
                print(currentLabel)
                currentLabel= currentLabel.split()


                coords = convertCoords(currentLabel, dimensions)


                tlx = int(int(coords[1]) - (int(coords[3]) / 2))
                tly = int(int(coords[2]) - (int(coords[4]) / 2))
                brx = int(int(coords[1]) + (int(coords[3]) / 2))
                bry = int(int(coords[2]) + (int(coords[4]) / 2))
                vertex1 = (tlx, tly)
                vertex2 = (brx, bry)
                #print("vertex1 : ", vertex1, "Vertex2 :", vertex2)
                cv2.rectangle(img, vertex1, vertex2, (0, 255, 0), 2)
                cv2.imshow('img', img)  # show img
                cv2.waitKey(100)  # if 'a' is pressed - move on to next image"""
                # newClassNumber = input("Enter New Class")

                #splitTextFileLine[0] = PongGame.newLabel"""
                # print("NEW LABEL IS : ", PongGame.newLabel)


                    #splitTextFileLine = " ".join(splitTextFileLine)
                    #print(splitTextFileLine)
                    #splitTextFileLine = splitTextFileLine + "\n"
                PongGame.labelListPosition = PongGame.labelListPosition + 1

            except:
                print("Failure to convert")
        else:
            print("No More Labels. Move to Next Image")
            PongGame.screenMessage = "No More Labels, Move to Next Image"


    def NewLabelValue(self,text):
        try:
            PongGame.newLabel = text
            PongGame.filenotfound = 0
            newTextFileLocation = PongGame.imgList[PongGame.currentImg-1].split("/")
            tempText = newTextFileLocation[-1].split(".")
            #print("Temp text at this point is : ", tempText)
            #print("Position is : ", PongGame.currentImg )
            tempText[-1] = ".txt"
            tempText = "".join((tempText))
            #print("temp text at this poitn is : ", tempText)
            newTextFileLocation = PongGame.newTextFileLocation + tempText
            #print("new file location is " , newTextFileLocation)
            currentLabel = PongGame.labelList[PongGame.labelListPosition-1]
            currentLabel = currentLabel.split()
            print(currentLabel[0])

            currentLabel[0] = text
            newLabel = " ".join(currentLabel)
            newLabel = newLabel + "\n"
            print(newLabel)


            try:
                file = open(newTextFileLocation, "a+")
                #print("File open to be appended")
                #print("Appending file : ", newTextFileLocation)
                #print("Image file is : ", PongGame.imgList[PongGame.currentImg-1] )
                #print("New Label is ", newLabel)
                try:
                    file.write(newLabel)
                except:
                    print("Failed to append")

                file.close()

                PongGame.filenotfound = 0

            except:
                print("file not found, create it")
                PongGame.filenotfound = 1
                if PongGame.filenotfound == 1:
                    file = open(newTextFileLocation, "w+")
                    print("Created File", newTextFileLocation)
                    file.write(newLabel)
                    file.close()

        except:
            print("Error with label file")
        ##now save new label to required directory

    ## path /home/v4/Datasets/boats/NewProposedDataSet/boat_images[val]/
    # new "/home/v4/Datasets/boats/boatValNewLabels/"
    def openImg(imgLoc):
        img = cv2.imread(imgLoc)  # open image

        cv2.imshow('img', img)  # show img
        PongGame.ImgDimensions = img.shape  # get image size
        print("Dimensions of img are : ", PongGame.ImgDimensions)
        cv2.waitKey(10)

    def getImageDirectory(self, inputText):
        PongGame.imgDirect = inputText
        print("You have set img directory to : ", PongGame.imgDirect)

    def getNewImageDirectory(self, inputText):
        PongGame.newTextFileLocation = inputText
        print("You have set New img directory to : ", PongGame.newTextFileLocation)

    #def showImage


    def changeText(self):
        self.screenMessage = "Changinngngngngngngng"


#def callback(instance):
    #print("Button is being pressed")



class PongApp(App):

    def build(self):
        #Clock.schedule_interval(self.changeText(), 1.0 / 2.0)
        return PongGame()


if __name__ == '__main__':


    PongApp().run()
