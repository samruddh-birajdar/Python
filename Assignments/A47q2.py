############################################################################################################################
#
# Program      : Linear Regression Performance
# Functions    : calculate_performance(), main()
# Input        : Dataset X, Y
# Output       : Predicted Y values, MSE, R2 Score
# Description  : Calculates performance metrics manually
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def calculate_performance():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    mean_x = sum(X)/len(X)
    mean_y = sum(Y)/len(Y)

    num = sum([(X[i]-mean_x)*(Y[i]-mean_y) for i in range(len(X))])
    den = sum([(X[i]-mean_x)**2 for i in range(len(X))])
    m = num/den
    c = mean_y - m*mean_x

    Y_pred = [m*x + c for x in X]
    print("Predicted Y values:", Y_pred)

    mse = sum([(Y[i]-Y_pred[i])**2 for i in range(len(Y))])/len(Y)
    ss_total = sum([(Y[i]-mean_y)**2 for i in range(len(Y))])
    ss_res = sum([(Y[i]-Y_pred[i])**2 for i in range(len(Y))])
    r2 = 1 - (ss_res/ss_total)

    print("Mean Squared Error (MSE):", mse)
    print("R2 Score:", r2)

def main():
    calculate_performance()

if __name__ == "__main__":
    main()
