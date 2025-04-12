🌦️ Weather Data Analysis and Temperature Prediction
This project focuses on analyzing a weather dataset and building a simple regression model to predict Temperature based on various weather-related features.

📁 Dataset
The dataset (Dataset11-Weather-Data.csv) contains real-world weather observations including attributes such as:

Temperature

Weather condition descriptions

Wind speed

Visibility

Dew Point, etc.

🧠 Project Overview
The script performs the following tasks:

Loads and explores the dataset using pandas and Seaborn

Checks for missing values and handles them

Explores and processes categorical weather data

Prepares features for machine learning (including one-hot encoding for categorical data)

Builds a Linear Regression model to predict temperature

Evaluates the model using metrics like Mean Squared Error (MSE) and R² Score

📊 ML Workflow Steps:
Data Loading & Cleaning

Exploratory Data Analysis (EDA)

Weather Condition Normalization (e.g., splitting compound weather labels like "Fog Rain")

Feature Engineering (including one-hot encoding)

Train/Test Split

Model Training using LinearRegression from sklearn

Performance Evaluation

🧪 Technologies Used
Python

Pandas, NumPy

Matplotlib, Seaborn

Scikit-learn

📈 Sample Output
The model outputs performance metrics such as:

Mean Squared Error: 5.03

R² Score: 0.89

✅ How to Run
Upload the dataset to /content/Dataset11-Weather-Data.csv (if running in Google Colab)

Run weather_detection_dataset.py to see the analysis and model results
