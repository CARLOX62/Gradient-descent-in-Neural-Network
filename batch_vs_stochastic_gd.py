# -*- coding: utf-8 -*-
"""Batch VS Stochastic GD.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dSwRhDMusg-Zy1VNNbHWyZ66xY-orUSm
"""

import numpy as np
import pandas as pd
import time

df = pd.read_csv('/content/Social_Network_Ads.csv')

df.head()

X = df.iloc[:,0:2]
y = df.iloc[:,-1]

X

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

X_scaled.shape

# from sklearn.model_selection import train_test_split
# X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

# X_train.shape

import tensorflow as tf
from tensorflow import keras
from keras import Sequential
from keras.layers import Dense

model = Sequential()

model.add(Dense(10,activation='relu',input_dim=2))
model.add(Dense(10,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.summary()

# We use batch GD
# batch_size is = n (no. of rows) then it is batch GD

# model.compile(loss='binary_crossentropy',metrics=['accuracy'])
# start = time.time()
# history = model.fit(X_scaled,y,epochs=10,batch_size=1,validation_split=0.2)
# print(time.time() - start)

# we use Stochastic GD
# batch_size = 1 or anything then it is SGD


# model.compile(loss='binary_crossentropy',metrics=['accuracy'])
# start = time.time()
# history = model.fit(X_train,y_train,epochs=10,batch_size=1)
# print(time.time() - start)

model.compile(loss='binary_crossentropy',metrics=['accuracy'])
#start = time.time()
history = model.fit(X_scaled,y,epochs=500,batch_size=1,validation_split=0.2)
#print(time.time() - start)

import matplotlib.pyplot as plt
plt.plot(history.history['loss'])

model = Sequential()

model.add(Dense(10,activation='relu',input_dim=2))
model.add(Dense(10,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',metrics=['accuracy'])
#start = time.time()
history = model.fit(X_scaled,y,epochs=10,batch_size=250,validation_split=0.2)
#print(time.time() - start)

plt.plot(history.history['loss'])

