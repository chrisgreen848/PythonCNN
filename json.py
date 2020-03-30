# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:30:52 2020

@author: chris
"""

import json

mypath = "C:/Users/chris/"
file = mypath+ "instances_train2017.json"
badList = "C:/Users/chris/bad.txt"

bad = []
it = 0
badFile = open(badList, "r")
for line in badFile:
    it += 1
    linesplit = line.split("/")
    temp = ""
    for i in range(len(linesplit)):
        temp= linesplit[i]
    temp = temp.split(".")
    bad.append(temp[0])
    
   
#print(bad)    
    #print("Bad Item Number ", it , ":" , linesplit)
    #bad.append(linesplit)
    
    
itfound = 0  
f = open(file) 
data = json.load(f)

for a in data['images']:
    imgId = a['id']
    imgId = imgId + 000000000000
    if str(imgId) in bad:
        w = a['width']
        h = a['height']
        print("Opening ", imgId)
        outFile = open('D:/textfiles/' + str(imgId) + ".txt", 'w') 
        for k in data['annotations']:
            
            imageid = k['image_id']
            
            if imgId == imageid:
                #imageid = k['image_id']
                
                cat = k['category_id']
                bbox = k['bbox']
                bboxx=(bbox[0]+bbox[2])/w
                bboxy=(bbox[1]+bbox[3])/h
                bboxw=(bbox[2]/w)
                bboxh=(bbox[3]/h)           
                label = str(cat) + " " + str(bboxx) + " " + str(bboxy) + " " + str(bboxw) + " " + str(bboxh) + "\n"
                outFile.write(label)
        
        outFile.close()
        print("Closing ", imgId)
    
    

	 
print(it, itfound)
f.close()
print("Finished")
