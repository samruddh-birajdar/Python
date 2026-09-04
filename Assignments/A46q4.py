############################################################################################################################
#
# Program      : Advertising Sales Prediction
# Functions    : test_model(), main()
# Input        : MarvellousAdvertising.csv file
# Output       : Predictions on test data
# Description  : Tests model using remaining half of dataset
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def test_model():
    df = pd.read_csv("MarvellousAdvertising.csv")
    X = df[['TV','Radio','Television']]
    y = df['Sales']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Predicted values:", y_pred)
    print("Expected values:", y_test.values)
    return y_pred, y_test

def main():
    y_pred, y_test = test_model()

if __name__ == "__main__":
    main()
