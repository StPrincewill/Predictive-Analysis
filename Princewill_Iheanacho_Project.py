# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 16:48:45 2020

@author: Dell
"""



import os 
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


def load_file(filename):
    return (pd.read_csv(filename))

def clean_data(df_house_data):
    #Let's convert date column to year by extracting the year out of the date
    df_house_data['date'] = df_house_data['date'].str[:4]
    
    #Let's convert the date column to integer so that we can obtain the age of the house from year it was built
    df_house_data['date'] = df_house_data['date'].astype(int)
    
    #creating new column to capture age of building
    df_house_data['house_Age'] = df_house_data['date']- df_house_data['yr_built']
    
    #let's convert zip codes to category in order not to confuse the model we are building
    df_house_data['zipcode']= df_house_data['zipcode'].astype('category')
    
    #We will try to remove the outliers and bridge the gap
    index = df_house_data[(df_house_data['bedrooms'] >= 10)|(df_house_data['bedrooms'] <= 1)].index
    df_house_data.drop(index, inplace=True)
    
    index = df_house_data[(df_house_data['bathrooms'] >= 6)|(df_house_data['bathrooms'] <= 0)].index
    df_house_data.drop(index, inplace=True)
    
    index = df_house_data[(df_house_data['sqft_living'] >= 8000)|(df_house_data['sqft_living'] < 590)].index
    df_house_data.drop(index, inplace=True)
    
    return (df_house_data)


def get_train_test_data(df_house_data):
    #Looking at things from a natuarl perspective, there are some variables that has nothing to do with the price of a house
    #and there are some of them that are not really strong enough to be considered a good predictor of price from the data
    #For example, at a glance, id here has nothing to do with price and will be removed. Then date is between 2014 and 2015
    #so it does not offer much to be a good predictor here
    #waterfront, view,lat,long,year renovated does not seem to offer much and will be removed
    #Finally, year built will be removed because we have already detremined the age of the house
    
    #drop some columns that may not be useful
    df_house = df_house_data.drop(['id','date','waterfront','view','lat','long','yr_built','yr_renovated'],axis=1)
      
    #Let us now seperate our data into features and target
    X = df_house.drop('price',axis=1)
    y= df_house[['price']]
    
    #To add the zipcode, we need to encode to 0 and 1s
    zipcode = pd.get_dummies(X['zipcode'],drop_first = True)
    #Let us drop the zipcode from the feature column as it is now redundant
    X=X.drop('zipcode',axis=1)
    #Add the zipcode features to the main features
    X = pd.concat([X,zipcode],axis=1)
    
    #Let's drop some additional variables that are not showing promise
    X=X.drop(['sqft_lot','sqft_lot15','sqft_living15'],axis=1)
    
    #Let's distribute our data again
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=1)
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.05, random_state=1)
    
    #return (X_train, X_val, y_train, y_val)
    return (X_train, X_val, X_test, y_train, y_val, y_test)

def train_regressor(X_train, y_train):
    #Let's train our model with features including the zipcodes
    regressor = LinearRegression()
    regressor.fit(X_train,y_train)
    return regressor


def predict_regressor(regressor, input_data):
    #let test with our test data
    return regressor.predict(input_data)


filename = "C:\\Users\\Dell\\Desktop\\Data Science\\house_prices_data.csv"
df = load_file(filename)
df_house_data = clean_data(df)
X_train, X_val, X_test, y_train, y_val, y_test = get_train_test_data(df_house_data)
regressor = train_regressor(X_train, y_train)


while True:
    user_input = input("Enter the path of your file: ")
    if os.path.exists(user_input):
        break
    else:
        print ("I did not find the file at, "+str(user_input))
        continue
    
user_df = load_file(user_input)
y_new = predict_regressor(regressor, user_df)
print("The House Price Having those features is Predicted to be: ${}".format(round(y_new[0][0], 2)))    