# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 15:39:30 2019

@author: Christopher Green
"""

#LOADING OWN DATA TO NETWORKS

import sys
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import tensorflow as tf

DATADIR = "D:\Images"
CATEGORIES = ["Drones", "Birds", "Sky"]
TEST= ["Other"]
for category in CATEGORIES:
    path = os.path.join(DATADIR, category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)  
        plt.imshow(img_array, cmap = "gray")
        plt.show()
        break
    break
print("There are ", len(CATEGORIES), "Categories")       
print(img_array.shape)        

IMG_SIZE = 50
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
plt.imshow(new_array, cmap = 'gray')
plt.show

training_data = []
test_data = []
def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)  
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass
def create_test_data():
    for tests in TEST:
        path = os.path.join(DATADIR, tests)
        class_num = TEST.index(tests)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)  
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                test_data.append([new_array, class_num])
            except Exception as e:
                pass
print("Creating training data")
create_training_data()
print("Training Data Successful. Training Data length is:",len(training_data))
print("Creating test data")
create_test_data()
print("Test Data Successful. Test Data length is:", len(test_data))


user_input = input("Would you like to continue?")
if(user_input == "No" or user_input == "no" or user_input == "NO" ):
    sys.exit()
import random

random.shuffle(training_data)  #shuffling data 


    
x = []  # labels
y = []  # labels
x_test = []
y_test = []
for features, label in training_data:
    x.append(features)
    y.append(label)
for features, label in test_data:
    x_test.append(features)
    y_test.append(label)
                  
                  
x = np.array(x).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
x_test = np.array(x_test).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
# Saving so you can use these again without training 
"""import pickle

pickle_out = open("x.pickle", "wb")
pickle.dump(x, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()

pickle_in = open("x.pickle", "rb")
x= pickle.load(pickle_in)"""


#Train Test Data
x = tf.keras.utils.normalize(x, axis=1)  # scales data between 0 and 1
x_test = tf.keras.utils.normalize(x_test, axis=1)

print("Training Successful")

#---------------------model--------------------

model = tf.keras.models.Sequential()  # a basic feed-forward model

model.add(tf.keras.layers.Flatten())  # takes our 28x28 and makes it 1x784
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  # a simple fully-connected layer, 128 units, relu activation
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam',  # Good default optimizer to start with
              loss='sparse_categorical_crossentropy',  # how will we calculate our "error." Neural network aims to minimize loss.
              metrics=['accuracy'])  # what to track
print("Training Successful YAAAAAAAAADA")

model.fit(x, y, epochs=3)  # train the model
print("Model Successful")

val_loss, val_acc = model.evaluate(x_test, y_test)  # evaluate the out of sample data with model




print("PROGRAM SUCCESSFUL")
