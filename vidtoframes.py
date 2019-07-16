# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import argparse
import cv2


def save_vid_to_images(filename):
    print("Starting Video")
    vidcap = cv2.VideoCapture(filename)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1
    print("Video frame capturing Complete")


# command line arguement
parser = argparse.ArgumentParser(description='Plot histograms of labelled data')
parser.add_argument('--File', action='store', dest = 'filename',
                    help='Video to be split location (will be saved to the same folder as this script)')                  

args = parser.parse_args()
print("File name is : ", args.filename)
filename = args.filename
save_vid_to_images(filename)
