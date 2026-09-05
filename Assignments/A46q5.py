############################################################################################################################
#
# Program      : Advertising Sales Prediction
# Functions    : display_results(), main()
# Input        : MarvellousAdvertising.csv file
# Output       : Predicted vs Expected values
# Description  : Displays predicted and expected values side by side
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def display_results():
    df = pd.read_csv("MarvellousAdvertising.csv")
    X = df[['TV','Radio','Television']]
    y = df['Sales']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    results = pd.DataFrame({'Expected': y_test.values, 'Predicted': y_pred})
    print(results)
    return results

def main():
    results = display_results()

if __name__ == "__main__":
    main()
