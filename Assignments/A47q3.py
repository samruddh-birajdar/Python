############################################################################################################################
#
# Program      : Salary Prediction using Linear Regression
# Functions    : train_salary_model(), main()
# Input        : Experience vs Salary dataset
# Output       : Predicted Salary for 6 years experience, Regression plot
# Description  : Trains regression model and plots regression line
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def train_salary_model():
    data = {
        'Experience': [1,2,3,4,5],
        'Salary': [20000,25000,30000,35000,40000]
    }
    df = pd.DataFrame(data)

    X = df[['Experience']]
    y = df['Salary']

    model = LinearRegression()
    model.fit(X,y)

    prediction = model.predict([[6]])
    print("Predicted Salary for 6 Years Experience: ₹", int(prediction[0]))

    plt.scatter(X,y,color='blue',label='Data Points')
    plt.plot(X,model.predict(X),color='red',label='Regression Line')
    plt.xlabel("Experience (Years)")
    plt.ylabel("Salary")
    plt.title("Experience vs Salary Regression")
    plt.legend()
    plt.show()

def main():
    train_salary_model()

if __name__ == "__main__":
    main()
