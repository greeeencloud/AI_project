# -*- coding: utf-8 -*-
"""face_recognition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vt8-p1CNdoWiRSSRY-q4x6mtMamKww6y
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

from subprocess import check_output
print(check_output(["ls", "../"]).decode("utf8"))

# Any results you write to the current directory are saved as output.

#Load all necessary libraries
import numpy as np
import cv2 # opencv
import os # control and access the directory structure in local machine
img = cv2.imread('train/ben_afflek/httpwwwhillsindcomstorebenjpg.jpg',12)

from matplotlib import pyplot as plt
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

#load training dataset of the faces data
for imgfolder in os.listdir('train/'): #iterate thru each of the 5 celeb folders
    for filename in os.listdir('train/' + imgfolder):# iterate thru each image in a celeb folder
        filename = 'train/' + imgfolder + '/' + filename # build the path to the image file
        print(filename) # print the filename read. For debugging purpose only
        img = cv2.imread(filename,0) # read the image using OpenCV
        plt.imshow(img, cmap = 'gray', interpolation = 'bicubic') # display all images read
        plt.xticks([]), plt.yticks([])
        plt.show()

# reading the dimensions of individual images. We need to scale it to a same size before we can use
# this dataset
for imgfolder in os.listdir('train/'):
    for filename in os.listdir('train/' + imgfolder):
        filename = 'train/'+ imgfolder + '/' + filename
        img = cv2.imread(filename,0)
        print (img.shape)

# scaling all images to 47 * 62 using OpenCV resize function
for imgfolder in os.listdir('train/'):
    for filename in os.listdir('train/' + imgfolder):
        filename = 'train/' + imgfolder+ '/'+ filename
        img=cv2.imread(filename,0)
        img = cv2.resize(img, (47,62), interpolation = cv2.INTER_AREA)  
        #print(type(img))
        print(img.shape)

# building an array of images and finding its shape.
X_images = []
for imgfolder in os.listdir('train/'):
    for filename in os.listdir('train/' + imgfolder):
        filename = 'train/' + imgfolder + '/' + filename
        #print(filename)
        img = cv2.imread(filename,0)
        img = cv2.resize(img, (47,62), interpolation = cv2.INTER_AREA)
        X_images.append(img)
X_images = np.asarray(X_images)
X_images.shape

#trying display a single image just to check
plt.imshow(X_images[20], cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

# building an 1D array of labels for the training dataset
y_train = []
for imgfolder in os.listdir('train/'):
    for filename in os.listdir('train/' + imgfolder):
        y_train.append(imgfolder)
y_train = np.asarray(y_train)
y_train.shape

#Build array of images for Test/Validation dataset
X_test = []
for imgfolder in os.listdir('val/'):
    for filename in os.listdir('val/' + imgfolder):
         if(filename.endswith('.jpg')):
                filename = 'val/' + imgfolder + '/' + filename
                #print(filename)
                img = cv2.imread(filename,0)
                img = cv2.resize(img, (47,62), interpolation = cv2.INTER_AREA)
                X_test.append(img)
X_test = np.asarray(X_test)

#Building a 1D array of test labels
y_test = []
for imgfolder in os.listdir('val/'):
    for filename in os.listdir('val/' + imgfolder):
        y_test.append(imgfolder)
y_test = np.asarray(y_test)

# Commented out IPython magic to ensure Python compatibility.
#display training images and labels to make sure they lineup correctly
# %matplotlib inline
import seaborn as sns; sns.set()

fig,ax = plt.subplots(3,6)
for i, axis in enumerate(ax.flat):
    axis.imshow(X_images[i], cmap= 'gray')
    axis.set(xticks = [], yticks=[], xlabel=y_train[i])

#display test images and labels to make sure they lineup correctly
fig, ax = plt.subplots(3, 5)
for i, axi in enumerate(ax.flat):
    axi.imshow(X_test[i], cmap='gray')
    axi.set(xticks=[], yticks=[],
            xlabel=y_test[i])