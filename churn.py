# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 08:23:03 2018

@author: KERKOURI Mohamed Amine
"""


################################## Part 1 Pre-Processing#########################"
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values


# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
X=X[:,1:]


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


################################## Part 2  ANN Making ##########################

#importing keras 
import keras 
from  keras.models import Sequential
from  keras.layers import Dense 

#Initialising ANN 
classifier =Sequential()

#Adding Input layer and Hidden layer 1 
classifier.add(Dense(output_dim=6,init='uniform',activation ='relu',input_dim=11))

#Adding Hidden layer 2
classifier.add(Dense(output_dim=6,init='uniform',activation ='relu'))

#Adding Output layer 
classifier.add(Dense(output_dim=6,init='uniform',activation ='relu'))

classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)


# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)    
