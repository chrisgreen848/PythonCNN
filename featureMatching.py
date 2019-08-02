# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 10:14:08 2019

@author: ChrisG
"""
import os
import csv
import argparse
import cv2
from matplotlib import pyplot as plt
import numpy as np
#Drone folder


#-----get list of images in relevant directory---------
def getImageList(imageDir, image_path_list):
    valid_img_ext = [".jpg", ".jpeg", ".png"] #look for these files only
    for file in os.listdir(imageDir):
        extension = os.path.splitext(file)[1]
        if extension.lower() not in valid_img_ext:
            continue
        image_path_list.append(os.path.join(imageDir, file))
    
    return image_path_list


#-----get list of labels in relevant directory----- 
def getLabelList(labelDir, label_path_list):
    valid_label_ext = [".txt"]
    for file in os.listdir(labelDir):
        extension = os.path.splitext(file)[1]
        if extension.lower() not in valid_label_ext:
            continue
        label_path_list.append(os.path.join(imageDir, file))
    return label_path_list



    #------turn yolo labels in to coco format --------
def unnormalizeData(xCoordinate, yCoordinate, bboxWidth, bboxHeight, imageWidth, imageHeight):
    label = [0,0,0,0]
    label[0] = int(xCoordinate*imageWidth+0.5)
    label[1] = int(yCoordinate*imageHeight+0.5)
    label[2] = int(bboxWidth*imageWidth+0.5)
    label[3] = int(bboxHeight*imageHeight+0.5)
    return label

def drawBoundingBox(img, label):
    topLeftCorner = [label[0],label[1]]
    bottomRightCorner = [label[0]+label[2],label[1]+label[3]]
    cv2.rectangle(img, (topLeftCorner[0],topLeftCorner[1]),( bottomRightCorner[0],bottomRightCorner[1]), (0,255,0),2)
    bbox = [topLeftCorner[0],topLeftCorner[1],bottomRightCorner[0],bottomRightCorner[1]]
    img = imcrop(img,bbox)
    return img


#convert centre point to top left --- return (x,y)
def centreToTopLeft(label):
    #       --- x ----
    coordXY = [0,0]
    coordXY[0]=int(label[0]-(label[2]/2)+0.5)
    coordXY[1]=int(label[1]-(label[3]/2)+0.5)
    return  coordXY
   
    # i stole imcrop and pad img :D works well
def imcrop(img, bbox): 
    x1,y1,x2,y2 = bbox
    if x1 < 0 or y1 < 0 or x2 > img.shape[1] or y2 > img.shape[0]:
        img, x1, x2, y1, y2 = pad_img_to_fit_bbox(img, x1, x2, y1, y2)
    return img[y1:y2, x1:x2, :]

def pad_img_to_fit_bbox(img, x1, x2, y1, y2):
    img = np.pad(img, ((np.abs(np.minimum(0, y1)), np.maximum(y2 - img.shape[0], 0)),
               (np.abs(np.minimum(0, x1)), np.maximum(x2 - img.shape[1], 0)), (0,0)), mode="constant")
    y1 += np.abs(np.minimum(0, y1))
    y2 += np.abs(np.minimum(0, y1))
    x1 += np.abs(np.minimum(0, x1))
    x2 += np.abs(np.minimum(0, x1))
    return img, x1, x2, y1, y2


def matchFeatures(img1,img2):
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1,None) #compute descriptors and kps img 1
    kp2, des2 = orb.detectAndCompute(img2,None) #compute descriptors and kps img 2
    pts = np.asarray([[p.pt[0], p.pt[1]] for p in kp1])
    pts2 = np.asarray([[p.pt[0], p.pt[1]] for p in kp2])

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True) 

                    # Match descriptors.
    try:               
        matches = bf.match(des1,des2) #match features between img 1 and 2
    
       
                # Sort them in the order of their distance.
        matches = sorted(matches, key = lambda x:x.distance) 
        matchesToDisplay = len(matches)    
        #img5 = cv2.drawMatches(img1,kp1,img2,kp2,matches[0:matchesToDisplay],None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        img3 = img1
        img4 = img2
        for i in range(len(pts)):
            y = int(pts[i][0]+0.5)
            x = int(pts[i][1]+0.5)
            img3[x,y] = (255,0,0)

        for i in range(len(pts2)):
            y = int(pts2[i][0]+0.5)
            x = int(pts2[i][1]+0.5)
            img4[x,y] = (0,255,0)

        print("There has been ", len(matches), "matches. Displaying ", len(matches), "of these matches.")
        plt.imshow(img5),plt.show()
        return len(matches)
    except Exception:
        return 0
    






###### ------------ COMMAND LINE ARGUEMENTS IF NEEDED ############
parser = argparse.ArgumentParser()
parser.add_argument("-f1", "--filename1", help="Image one number for comparison") 
args = parser.parse_args()
testImageNumber = int(args.filename1)
       
print("Program Running")



imageDir = "tv/newdata/3551"   ##add command line arg for this ?
image_path_list= []   #list to store image paths
label_path_list= []   #label paths

image_path_list = getImageList(imageDir, image_path_list)
label_path_list = getLabelList(imageDir, label_path_list)

#--- test image manip #   turn in to function??
testImage = cv2.imread(image_path_list[testImageNumber])
dimensionsTest = testImage.shape
testImageHeight = dimensionsTest[0] 
testImageWidth = dimensionsTest[1]
with open(label_path_list[testImageNumber]) as fp:
            readCSV = csv.reader(fp, delimiter=' ')  #should only be one line
            for row in readCSV:
                x = float(row[1]) #x cordinate
                y = float(row[2]) #y coordinate
                w = float(row[3]) #bounding box width
                h = float(row[4]) #bounding box height

testCocobboxLabel = unnormalizeData(x,y,w,h,testImageWidth, testImageHeight)
        #get bbox top left coord
testTopLeftXY = centreToTopLeft(testCocobboxLabel)
testCocobboxLabel[0] = testTopLeftXY[0]
testCocobboxLabel[1] = testTopLeftXY[1]
testbboximg = drawBoundingBox(testImage,testCocobboxLabel) ## TESTBBOXIMG ----
#plt.imshow(testbboximg),plt.show()
#test image manipulation


matchesList = []

            #show test image
#plt.imshow(testImage),plt.show()
#totalMatchesPerImage = np.array()
for i in range(len(label_path_list)):
    if i != testImageNumber: #don't match with the same image
        currentComparisonImage = cv2.imread(image_path_list[i])
        dimensions = currentComparisonImage.shape
        imageHeight = dimensions[0]
        imageWidth = dimensions[1]
        #read bounding box details # for now just one label 
        with open(label_path_list[i]) as fp:
            readCSV = csv.reader(fp, delimiter=' ')  #should only be one line
            for row in readCSV:
                x = float(row[1]) #x cordinate
                y = float(row[2]) #y coordinate
                w = float(row[3]) #bounding box width
                h = float(row[4]) #bounding box height
        #yolo to coco           
        cocobboxLabel = unnormalizeData(x,y,w,h,imageWidth, imageHeight)
        #get bbox top left coord
        topLeftXY = centreToTopLeft(cocobboxLabel)
        cocobboxLabel[0] = topLeftXY[0]
        cocobboxLabel[1] = topLeftXY[1]
        comparisonbboximg = drawBoundingBox(currentComparisonImage,cocobboxLabel)
        #plt.imshow(comparisonbboximg),plt.show()
               
        matchesList.append(matchFeatures(testbboximg, comparisonbboximg))
        print("Image ", i, "Complete")
        
    else:
        matchesList.append("This is matching image")
        print("This is the test Image")

plt.imshow(testbboximg),plt.show()
