import numpy as np
import matplotlib.pyplot as plt
import cv2
print("Running Successfully \n")
img = cv2.imread("Drones\Drone1.jpg")

surf = cv2.xfeatures2d.SURF_create(400)
kp, des = surf.detectAndCompute(img,None)
print(len(kp))

kp, des = surf.detectAndCompute(img,None)
img2 = cv2.drawKeypoints(img,kp,None,(255,0,0),4)
plt.imshow(img2),plt.show()
