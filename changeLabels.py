import glob
import shutil
import os
import cv2

#path = "/home/v4/Datasets/boats/boat_images[train]copy/"    #change path to your images
#path = "/home/v4/Datasets/boats/IndividualClassPhotos/chrissplit/"
#saveDir = "/home/v4/Datasets/boats/IndividualClassPhotos/cocoreclassed/"  #change path to where you want images stored
path = "/home/v4/Datasets/boats/NewProposedDataSet/boat_images[val]/"
saveDir = "/home/v4/Datasets/boats/IndividualClassPhotos/cocoreclassedval/"
imageNumber = 0

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




for root, dir, files in os.walk(path):

    for name in files:
        if name.endswith((".jpg")):

            imageNumber = imageNumber + 1  #count image numbers4

            imageLocation = path + name    #location of image to open
            #print(imageLocation)           #check image location
            img = cv2.imread(imageLocation)#open image

            cv2.imshow('img', img)         #show img
            dimensions = img.shape          # get image size
            print("Dimensions of img are : ", dimensions)

            #input("Move on to next image?")

            #  ----get text file to get coords ---
            textfilename = jpgToTxt(name)
            textfileDir = path + textfilename
            newTextfileDir = saveDir + textfilename
            try:
                textfile = open(textfileDir, "r")  #read current label file
            except:
                print("Cant open", textfileDir)
            txtfileExist = os.path.exists(newTextfileDir)
            checkImgDir = saveDir + name
            imgfileExist = os.path.exists(checkImgDir)
            if imgfileExist == False:
                shutil.copy(imageLocation, saveDir)
            if txtfileExist == False:
                newLabelFile = open(newTextfileDir, "w")
                print("Opening File: ", newTextfileDir)
                  #copy the jpg image to new folder
                for object in textfile:
                    splitTextFileLine = object.split()
                    coords = convertCoords(splitTextFileLine, dimensions)
                    tlx = int(int(coords[1]) - (int(coords[3])/2))
                    tly = int(int(coords[2]) - (int(coords[4])/2))
                    brx = int(int(coords[1]) + (int(coords[3])/2))
                    bry = int(int(coords[2]) + (int(coords[4])/2))
                    vertex1 = (tlx,tly)
                    vertex2 = (brx, bry)
                    print("vertex1 : ", vertex1, "Vertex2 :", vertex2)
                    cv2.rectangle(img, vertex1, vertex2, (0,255,0), 2 )
                    cv2.imshow('img', img)  # show img
                    cv2.waitKey(100)  # if 'a' is pressed - move on to next image
                    newClassNumber = input("Enter New Class")
                    splitTextFileLine[0] = newClassNumber
                    splitTextFileLine = " ".join(splitTextFileLine)
                    print(splitTextFileLine)
                    splitTextFileLine = splitTextFileLine + "\n"
                    newLabelFile.write(splitTextFileLine)
                    #replace class with the new type you've chosen = i.e coco = boat = we wnt sail bo
                    c = cv2.waitKey(0) % 256  # if 'a' is pressed - move on to next image

                    if c == ord('a'): #press a to move on to next object in file
                        print("Next Object Selected")

                newLabelFile.close()
               #draw rectangle

