from kivy.app import App
from kivy.uix.widget import Widget
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

    #variables needed
    currentImg = 0 #position in list
    imgList = []
    totalImgs = 0
    currentJpgFileLocation = ""
    currentTxtFileLocation = ""
    path = ""
    ImgDimensions = []


    #simple butotn press check
    def on_enter(instance, value):
        print('User pressed enter in', instance)

    #gets list of images and paths in the directory
    def pressme(self):
        path = "/home/v4/Datasets/boats/NewProposedDataSet/boat_images[val]/"
        PongGame.imgList = getImgList(path)
        PongGame.totalImgs = len(PongGame.imgList)
        print(PongGame.imgList)

    #opens next img in the list
    def getNextImg(imgList):
        #PongGame.openImg(PongGame.imgList[PongGame.currentImg])
        PongGame.currentTxtfileLocation = jpgToTxt(PongGame.imgList[PongGame.currentImg])
        currentImgLoc = PongGame.imgList[PongGame.currentImg]
        try:
            textfile = open(PongGame.currentTxtfileLocation, "r")
            PongGame.nextLabel(textfile, currentImgLoc)
        except:
            print("Can't open text file : ", textfile)
        #PongGame.nextLabel(PongGame.imgList[PongGame.currentImg])
        print("img : ", PongGame.currentImg, "/" , PongGame.totalImgs)
        PongGame.currentImg = PongGame.currentImg + 1

    def openImg(imgLoc):
        img = cv2.imread(imgLoc)  # open image

        cv2.imshow('img', img)  # show img
        PongGame.ImgDimensions = img.shape  # get image size
        print("Dimensions of img are : ", PongGame.ImgDimensions)
        cv2.waitKey(10)

    def nextLabel(file, curImg):
        #open text file:

        img = cv2.imread(curImg)  # open image
        try:
            txtFile = open(file, "r")
        except:
            print("failed to open textfile")
        cv2.imshow('img', img)  # show img
        PongGame.ImgDimensions = img.shape  # get image size
        print("Dimensions of img are : ", PongGame.ImgDimensions)
        cv2.waitKey(10)
        dimensions = PongGame.ImgDimensions
        for object in file:
            splitTextFileLine = object.split()
            coords = convertCoords(splitTextFileLine, dimensions)
            tlx = int(int(coords[1]) - (int(coords[3]) / 2))
            tly = int(int(coords[2]) - (int(coords[4]) / 2))
            brx = int(int(coords[1]) + (int(coords[3]) / 2))
            bry = int(int(coords[2]) + (int(coords[4]) / 2))
            vertex1 = (tlx, tly)
            vertex2 = (brx, bry)
            print("vertex1 : ", vertex1, "Vertex2 :", vertex2)
            cv2.rectangle(img, vertex1, vertex2, (0, 255, 0), 2)
            cv2.imshow('img', img)  # show img
            cv2.waitKey(100)  # if 'a' is pressed - move on to next image
            #newClassNumber = input("Enter New Class")
            #splitTextFileLine[0] = newClassNumber
            splitTextFileLine = " ".join(splitTextFileLine)
            print(splitTextFileLine)
            splitTextFileLine = splitTextFileLine + "\n"
            #newLabelFile.write(splitTextFileLine)
            PongGame.enterNewLabel()
            # replace class with the new type you've chosen = i.e coco = boat = we wnt sail bo
            c = cv2.waitKey(0) % 256  # if 'a' is pressed - move on to next image

            if c == ord('a'):  # press a to move on to next object in file
                print("Next Object Selected")

    def enterNewLabel(self):
        print("New Label is : ")

#def callback(instance):
    #print("Button is being pressed")



class PongApp(App):

    def build(self):

        return PongGame()


if __name__ == '__main__':


    PongApp().run()
