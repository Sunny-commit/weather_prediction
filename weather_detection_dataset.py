# -*- coding: utf-8 -*-
"""weather_detection_dataset

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S_gfVtWCF-nd41DJiy4vx9XWP9ZWgB3C
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('/content/Dataset11-Weather-Data.csv')
data.head()

data.shape

data.info()

data.describe()

data.isnull().sum()

data['Weather'].value_counts()

data['Weather'].nunique()

"""## converting the weather categorical into standard categorical"""

x='Thunderstorms,Moderate Rain Showers,Fog'

#split the above x

list_of_lists=[w.split() for w in x.split(',')]
list_of_lists

#combining the before splited data to a combined form as

from itertools import chain
flat_list=list(chain(*list_of_lists))
flat_list

def create_list(x):
  list_of_lists=[w.split() for w in x.split(',')]
  flat_list=list(chain(*list_of_lists))
  return flat_list




def Get_weather(list1):
  if 'Fog' in list1 and 'Rain' in list1:
    return 'RaIN+FOG'

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv('/content/Dataset11-Weather-Data.csv')

# Show the first few rows
print("Dataset Preview:\n", df.head())

# Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# Drop rows with missing values (or handle them as needed)
df = df.dropna()

# Choose feature columns (X) and target column (y)
# You can change these based on your dataset
# Let's assume we are predicting "Temperature" using the other numeric features

# Print all column names to choose features
print("\nColumns:", df.columns)

# Example: predicting 'Temperature' from all other numeric columns
target_column = 'Temperature'  # change this if needed
X = df.drop(columns=[target_column])
y = df[target_column]

# If there are non-numeric columns, convert or drop them
X = pd.get_dummies(X, drop_first=True)

# Split the dataset into training and testing sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("Mean Squared Error:", mse)
print("R² Score:", r2)