# -*- coding: utf-8 -*-
"""Covid19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R9GsNVvine7zoGEClIWSE-lyiQjqUq2e
"""

from google.colab import files
files.upload()

!pip install -q kaggle

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/

!kaggle datasets list

!chmod 600 /root/.kaggle/kaggle.json

!chmod 600 /root/.kaggle/kaggle.json
!kaggle datasets download -d pranavraikokte/covid19-image-dataset

!chmod 600 /root/.kaggle/kaggle.json

from tensorflow import keras
from keras.layers import Input, Dense, Dropout,Conv2D, MaxPooling2D, Flatten
from tensorflow.keras import  datasets
from matplotlib import pyplot as plt

import pandas as pd
from zipfile import ZipFile
with ZipFile('/content/covid19-image-dataset.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()

import os
 
# assign directory
directory = '/content/Covid19-dataset/test/Covid'
test_Covid=[]
# iterate over files in
# that directory
for filename in os.scandir(directory):
    if filename.is_file():
        test_Covid.append(filename.path)

test_Covid

import os
 
# assign directory
directory = '/content/Covid19-dataset/test/Normal'
test_Normal=[]
# iterate over files in
# that directory
for filename in os.scandir(directory):
    if filename.is_file():
        test_Normal.append(filename.path)
test_Normal

import os
 
# assign directory
directory = '/content/Covid19-dataset/test/Viral Pneumonia'
test_pneumonia=[]
# iterate over files in
# that directory
for filename in os.scandir(directory):
    if filename.is_file():
        test_pneumonia.append(filename.path)
test_pneumonia

import os
 
# assign directory
directory = '/content/Covid19-dataset/train/Covid'
train_Covid=[]
# iterate over files in
# that directory
for filename in os.scandir(directory):
    if filename.is_file():
        train_Covid.append(filename.path)
train_Covid

import os
 
# assign directory
directory = '/content/Covid19-dataset/train/Normal'
train_Normal=[]
# iterate over files in
# that directory
for filename in os.scandir(directory):
    if filename.is_file():
        train_Normal.append(filename.path)
train_Normal

import os
 
# assign directory
directory = '/content/Covid19-dataset/train/Viral Pneumonia'
train_Pneumonia=[]
# iterate over files in
# that directory
for filename in os.scandir(directory):
    if filename.is_file():
        train_Pneumonia.append(filename.path)
train_Pneumonia

# Import the necessary libraries
import cv2
from numpy import asarray
import numpy as np
# load the image and convert into 
# numpy array
x_train=[]
for i in train_Covid:
    img =cv2.imread(i,0)
    img=cv2.resize(img, (100, 100)) 
    img=np.array(img)
    x_train.append(np.array(img).astype(np.uint8))

for i in train_Normal:
    img =cv2.imread(i,0)
    img=cv2.resize(img, (100, 100)) 
    img=np.array(img)
    x_train.append(np.array(img).astype(np.uint8))
   


for i in train_Pneumonia:
    img =cv2.imread(i,0)
    img=cv2.resize(img, (100, 100)) 
    img=np.array(img)
    x_train.append(np.array(img).astype(np.uint8))

    
# data
print(x_train)

import numpy as np 
x_train=np.array(x_train)

import numpy as np
#x_train=x_train.reshape((-1,10000))
x_train.shape

y_train=[]

for i in train_Covid:
  y_train.append(0)
for i in train_Normal:
  y_train.append(1)
for i in train_Pneumonia:
  y_train.append(2)

y_train=np.array(y_train)
y_train = np.asarray(y_train).astype('uint8')
y_train.shape

# Import the necessary libraries
  
# importing cv2 
import cv2
from numpy import asarray

# load the image and convert into 
# numpy array
x_test=[]
for i in test_Covid:
    img =cv2.imread(i,0)
    img=cv2.resize(img, (100, 100)) 
    img=np.array(img)
    x_test.append(np.array(img).astype(np.uint8))
for i in test_Normal:
    img =cv2.imread(i,0)
    img=cv2.resize(img, (100, 100)) 
    img=np.array(img)
    x_test.append(np.array(img).astype(np.uint8))

for i in test_pneumonia:
    img =cv2.imread(i,0)
    img=cv2.resize(img, (100, 100)) 
    img=np.array(img)
    x_test.append(np.array(img).astype(np.uint8))
  
    
# data
print(x_test)

import numpy as np 
x_test=np.array(x_test)

#x_test=x_test.reshape((-1,10000))
x_test.shape

x_test[0].shape

x_train[0]

y_test=[]

for i in test_Covid:
  y_test.append(0)
for i in test_Normal:
  y_test.append(1)
for i in test_pneumonia:
  y_test.append(2)

y_test=np.array(y_test).astype(np.uint8)
y_test.shape

import pandas as pd
import keras 
from keras.models import *
from keras.layers import Dense
import matplotlib.pyplot as plt

# normlize the data
x_train = x_train/255
x_test  = x_test/255

#model = keras.Sequential()
#model.add(keras.layers.Dense(6667,input_shape=(10000,), activation="relu"))
#model.add(Dense(2933, activation='relu'))
#model.add(Dense(3, activation='softmax'))

model=keras.Sequential() #Create a network sequence.
model.add(Input(shape=(100,100,1)))
model.add(Conv2D(filters=6,kernel_size = 3,strides = (2,2), padding = 'same',activation = 'relu'))
#model.add(Conv2D(filters=6,kernel_size = 5,strides = (1,1), padding = 'same',activation = 'relu',input_shape = (28,28,1)))
model.add(MaxPooling2D(pool_size=(2,2), strides = (2,2), padding = 'valid'))

model.add(Conv2D(filters=6,kernel_size = 3,strides = (2,2), padding = 'same',activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2), strides = (2,2), padding = 'valid'))

model.add(Conv2D(filters=16,kernel_size = 3,strides = (2,2),padding = 'same',activation = 'relu'))
model.add(MaxPooling2D(pool_size=(2,2), strides = (2,2), padding = 'valid'))


model.add(Flatten())
model.add(Dense(84,activation = 'relu'))
model.add(Dense(10,activation = 'relu'))
model.add(Dense(3,activation="softmax"))

model.summary()
'''
model=keras.Sequential() #Create a network sequence.
model.add(Conv2D(filters=96,kernel_size =(11,11) ,strides = (4,4), padding = 'same',activation = 'relu',input_shape=(100,100,1)))
model.add(MaxPooling2D(pool_size=(3,3), strides = (2,2)))

model.add(Conv2D(filters=256,kernel_size = (5,5),strides = (1,1), padding = 'same',activation = 'relu'))
model.add(MaxPooling2D(pool_size=(3,3), strides = (2,2)))

model.add(Conv2D(filters=384,kernel_size = (3,3),strides = (1,1),padding = 'same',activation = 'relu'))
model.add(Conv2D(filters=384,kernel_size = (3,3),strides = (1,1),padding = 'same',activation = 'relu'))
model.add(Conv2D(filters=384,kernel_size = (3,3),strides = (1,1),padding = 'same',activation = 'relu'))
model.add(MaxPooling2D(pool_size=(3,3), strides = (2,2), padding = 'same'))


model.add(Flatten())
model.add(Dense(4096,activation = 'relu'))
model.add(Dense(4096,activation = 'relu'))
model.add(Dense(3,activation = 'softmax'))

model.summary()
'''

model.compile(optimizer='adam',loss="sparse_categorical_crossentropy",metrics=['accuracy']) 
results= model.fit(x_train,y_train,epochs=50,batch_size=128,validation_data=(x_test, y_test))

#results=model.fit( x=x_train,y=y_train, shuffle=True,  epochs=100,   validation_data=(x_test,y_test))

score = model.evaluate(x_test, y_test)

y_pred=model.predict(x_test)
y_pred[0:3]

import numpy as np
from numpy import argmax
y_pred1=argmax(y_pred,axis=1)
y_pred1[0:3]

from sklearn.metrics import accuracy_score,confusion_matrix
print(confusion_matrix(y_pred1,y_test))
print(accuracy_score(y_pred1,y_test))

import matplotlib.pyplot as plt
plt.plot(results.history['loss'])
plt.plot(results.history['val_loss'])
plt.legend(['Training','Vaildation'])
plt.title('Training and Validation Losses')
plt.xlabel('epoches')
plt.ylabel('losses')

import matplotlib.pyplot as plt
plt.plot(results.history['accuracy'])
plt.plot(results.history['val_accuracy'])
plt.legend(['Training','Vaildation'])
plt.title('Training and Validation Accuracy')
plt.xlabel('epoches')
plt.ylabel('accuracy')

print(results.history['accuracy'])
print(results.history['val_accuracy'])

print(model.evaluate(x_test,y_test))

model.save("Covid19_CNN.h5")
from google.colab import drive
drive.mount('/content/drive')
from keras.models import load_model
!cp "/content/Covid19_CNN.h5" "/content/drive/MyDrive/H5_Folders"