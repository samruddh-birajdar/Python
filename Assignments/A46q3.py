############################################################################################################################
#
# Program      : Advertising Sales Prediction
# Functions    : train_model(), main()
# Input        : MarvellousAdvertising.csv file
# Output       : Trained Linear Regression model
# Description  : Trains model using half of dataset
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def train_model():
    df = pd.read_csv("MarvellousAdvertising.csv")
    X = df[['TV','Radio','Television']]
    y = df['Sales']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("Model trained successfully")
    return model, X_test, y_test

def main():
    model, X_test, y_test = train_model()

if __name__ == "__main__":
    main()
