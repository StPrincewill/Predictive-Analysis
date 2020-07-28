# Predictive-Analysis
Predicting house prices based on input parameters

House prices have always been an important topic and indicator to the state of the economy overall. The real estate markets provide opportunities for data scientists and analysts to see where prices of houses are heading to and what the future holds in terms of house pricing for prospective home buyers. Therefore, predicting house prices is always very important as it is an indicator of the general housing market as well as the economy.

The aim is to predict the house prices in King County, Washington State, USA using Multiple Linear Regression (MLR) model. The dataset consisted of historic data of houses sold between May 2014 to May 2015.

At the end, the prediction is built into an application where users can pass several input parameters and get an instant price prediction of their favorite home.

The dataset is obtained from Kaggle. The dataset consists of 21 variables and 21613 observations.
https://www.kaggle.com/swathiachath/kc-housesales-data#kc_house_data.csv

Users are expected to enter a csv file template with the following house information: No of bedrooms, bathrooms, sqft_living, floors, condition, grade, sqft_above, sqft_basement, house_Age and zipcode. All zipcodes in the file are set to 0 by default. The user is required to find their zipcode and change it to 1. This file path is then passed to the program as an input. Program validates the file to run

The output is a prediction of the house price of the features entered above. The house price is displayed on the application. For example, a house with the following features;
3 bedrooms, 2.25 bathroom, 2230 sqft_living, 1 floor, 4 condition, grade of 8, 1510 sqft_above, 720 sqft_basement, 40 years of age and located in the 98006 area is predicted to cost $702,721.76. I have included an input_data file to test the program
