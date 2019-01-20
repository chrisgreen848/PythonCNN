# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os, os.path


print("Program Running")

imageDir = "images/drones"
image_path_list= []
imageDirBird = "images/birds"
image_path_list_bird = []
valid_img_ext = [".jpg", ".jpeg", ".png"]

#Drone folder
for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_img_ext:
        continue
    image_path_list.append(os.path.join(imageDir, file))
#Bird Folder
for file in os.listdir(imageDirBird):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_img_ext:
        continue
    image_path_list_bird.append(os.path.join(imageDirBird, file))
    
for x in range(len(image_path_list)):
    img1 = cv2.imread(image_path_list[x])
    for y in range(len(image_path_list_bird)):
        
        img2= cv2.imread(image_path_list_bird[y])

        orb = cv2.ORB_create()

        kp1, des1 = orb.detectAndCompute(img1,None)
        kp2, des2 = orb.detectAndCompute(img2,None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1,des2)
        matches = sorted(matches, key = lambda x:x.distance)
        img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
        plt.figure(figsize=(16,9))
        plt.imshow(img3)
        plt.show()

print("Program End")

