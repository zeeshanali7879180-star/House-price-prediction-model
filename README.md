# House-price-prediction-model
# House Price Prediction using Linear Regression

## Project Overview

This project predicts house prices using a Linear Regression machine learning model.

The model uses house features such as square footage, distance from the city,
and number of rooms to predict the house price.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Linear Regression

## Dataset

The dataset contains information about houses and their prices.

The following features are used for prediction:

- `square_feet` - Size of the house in square feet
- `distance_to_city(km)` - Distance from the city in kilometers
- `num_rooms` - Number of rooms

The target variable is:

- `price` - House price

## Machine Learning Model

I used **Linear Regression** from Scikit-learn to train the model.

The model learns the relationship between the house features and the house price.

## Prediction Example

The model was used to predict the price of a house with:

- Square feet: 2248
- Distance to city: 22 km
- Number of rooms: 3

The trained model then generates the predicted house price.

## Project Workflow

1. Load the dataset using Pandas
2. Explore the dataset
3. Select the input features
4. Select the target variable
5. Train the Linear Regression model
6. Provide new house information
7. Predict the house price

## Code

The complete Python code is available in the project files.

## Future Improvements

- Split the dataset into training and testing sets
- Evaluate the model using MAE, MSE, and R² score
- Try other machine learning algorithms
- Perform feature engineering
- Improve model performance
