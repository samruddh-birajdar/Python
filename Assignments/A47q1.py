############################################################################################################################
#
# Program      : Simple Linear Regression (Manual)
# Functions    : calculate_regression(), main()
# Input        : Dataset X, Y
# Output       : Mean of X, Mean of Y, Slope, Intercept, Regression Equation, Prediction
# Description  : Implements linear regression manually without ML libraries
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def calculate_regression():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    mean_x = sum(X)/len(X)
    mean_y = sum(Y)/len(Y)

    num = sum([(X[i]-mean_x)*(Y[i]-mean_y) for i in range(len(X))])
    den = sum([(X[i]-mean_x)**2 for i in range(len(X))])
    m = num/den
    c = mean_y - m*mean_x

    print("Mean of X =", mean_x)
    print("Mean of Y =", mean_y)
    print("Slope (m) =", m)
    print("Intercept (c) =", c)
    print("Regression Equation: Y =", round(m,2),"X +", round(c,2))
    x_val = 6
    y_pred = m*x_val + c
    print("Predicted Y for X=6:", y_pred)

def main():
    calculate_regression()

if __name__ == "__main__":
    main()
