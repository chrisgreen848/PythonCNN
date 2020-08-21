# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 08:53:43 2020
### would be nice to turn this in to a UI so we can individual click rotations we want and so forth

@author: ChrisGreen
"""
import os
import glob
import albumentations as a
import cv2
import os.path
from os import path


### Load image directory - save to list so we don't have to keep searching
## arguement : empty image list, directory of images
def getImageList(imgList, imgDir):
    os.chdir(imgDir)
    #### Get jpeg images ####
    for file in glob.glob("*.jpg"):
       fullImageLocation = imgDir + file
       imgList.append(fullImageLocation)
    #### Get bitmap images #### 
    for file in glob.glob("*.bmp"):
       fullImageLocation = imgDir + file
       imgList.append(fullImageLocation)
    #### Get png images ####
    for file in glob.glob("*.png"):
       fullImageLocation = imgDir + file
       imgList.append(fullImageLocation)
    
    return imgList



def getBboxList(imgList):
    bboxData = []
    for i in range(len(imgList)):
        textFile = imgList[i].split(".")
        newTextFile = textFile[0] + ".txt"
        ##check the textfile exists
        if path.exists(newTextFile):
            bboxData.append(newTextFile)
    return bboxData 



def getLabels(bboxList):
    bboxLabels = []
    bboxCurrentLabel = []
    for i in range(len(bboxList)):
        curLabelFile = open(bboxList[i], "r")
        bboxLabels.append([])
        for line in curLabelFile:
            bboxLabels[i].append(line)
            
        bboxCurrentLabel.clear()
    return bboxLabels
    
    
    
def getImageName(name):
    splitName = name.split("/")
    oldImgName = splitName[5]
    oldImgName = oldImgName.split(".")
    oldImgName = oldImgName[0]
    return oldImgName

    
def saveLabelsAsTextFile(bboxObjects, file, classList):
    txtFile = open(file, "w+")
    for i in range(len(bboxObjects)):
        
            newline ="0 " + str(bboxObjects[i][0]) + " " + str(bboxObjects[i][1]) + " " + str(bboxObjects[i][2]) + " " + str(bboxObjects[i][3]) + "\n"
            print(newline)
            txtFile.write(newline)
            
    else:
        newline = "0 " + str(bboxObjects[i][0]) + " " + str(bboxObjects[i][1]) + " " + str(bboxObjects[i][2]) + " " + str(bboxObjects[i][3])
        print(newline)
        txtFile.write(newline)
    
    


imgDir = "Y:/2020-VesselDetection/Annotations/training/trainingset/"
saveDir = "Y:/2020-VesselDetection/Annotations/training/augmentations/"
textFileName = saveDir 
imgList = []
bboxList = [] ##list of bbox files
bboxData = [] ##list of bbox labels 
classes = ['boat']

###Image list ready to be augmented
imgList = getImageList(imgList, imgDir)
bboxList = getBboxList(imgList)


##---- Check size of img and bbox list to see if they match -----###
if len(bboxList) == len(imgList):
    print("Total label files and total img files match!")
else:
    print("Total label files and total img files do NOT match. Check!")
    print("Label files size: ", len(bboxList), "Img files size: ", len(imgList))

bboxData = getLabels(bboxList)
class_labels = ['boat']
##create instance of 'compose' class


#transform = a.Compose([a.OpticalDistortion(distort_limit=0.05, shift_limit=0.05, interpolation=1, 
        #border_mode=4, value=None, mask_value=None, always_apply=True)
         #, a.Rotate(limit=(90,90),always_apply=True)], bbox_params=a.BboxParams(format='yolo'))
    
    
transform = a.Compose([ a.Rotate(limit=(180,180),always_apply=True)], bbox_params=a.BboxParams(format='yolo'))   
##import image
print("Started Transform for each image in directory")

for i in range(len(imgList)):
    image = cv2.imread(imgList[i])
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    oldImgName = getImageName(imgList[i])
   
    bboxes = []
    
    for i in range(len(bboxData[j])):
    bboxData[j][i]=bboxData[j][i].strip('\n')
    currentLabel = bboxData[j][i].split(" ")
    bboxes.append([])
    bboxes[i].append(float(currentLabel[1]))
    bboxes[i].append(float(currentLabel[2]))
    bboxes[i].append(float(currentLabel[3]))
    bboxes[i].append(float(currentLabel[4]))
    bboxes[i].append('boat')
    
    
    """
    transformed = transform(image=image)
    transformed_image = transformed["image"]
    newImageName = saveDir + oldImgName + "_augmented.jpg"
    cv2.imwrite(newImageName,transformed_image )
    print("Image ", i, "complete!")"""
    


#-----INDIVIDUAL IMAGES ----- # 
"""
j = 1
image = cv2.imread(imgList[j])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
oldImgName = getImageName(imgList[j])
    #h, w = image.shape[:2]
bboxes = []
for i in range(len(bboxData[j])):
    bboxData[j][i]=bboxData[j][i].strip('\n')
    currentLabel = bboxData[j][i].split(" ")
    bboxes.append([])
    bboxes[i].append(float(currentLabel[1]))
    bboxes[i].append(float(currentLabel[2]))
    bboxes[i].append(float(currentLabel[3]))
    bboxes[i].append(float(currentLabel[4]))
    bboxes[i].append('boat')
    print(bboxes[i])  
 """  
    

## save text file


newImageName = saveDir + oldImgName + "_augmented"
jpgName = newImageName + ".jpg"
textFileName = newImageName + ".txt"
saveLabelsAsTextFile(transformed_bbox, textFileName)
cv2.imwrite(jpgName,transformed_image )
print("Image ", i, "complete!")






  
"""

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #cv2.imshow("img", image)
    #cv2.waitKey(1)
oldImgName = getImageName(imgList[i])
#transformed = transform(image=image, bboxes=bboxes, class_labels=class_labels)
transformed = transform(image=image)
transformed_image = transformed["image"]
print("Image transfer done")
##---bboxes are failing - find out why --- ###
#transformed_bboxes = transformed['bboxes'] 
#print("Bbox transfer done")
#transformed_class_labels = transformed['class_labels']
newImageName = saveDir + oldImgName + "_augmented.jpg"
    
cv2.imwrite(newImageName,transformed_image )
"""
