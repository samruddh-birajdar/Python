############################################################################################################################
#
# Program      : Classification Report
# Functions    : generate_report(), main()
# Input        : Actual and Predicted arrays
# Output       : Classification report (precision, recall, F1-score, support)
# Description  : Generates classification report using scikit-learn
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

from sklearn.metrics import classification_report

def generate_report():
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    report = classification_report(actual, predicted)
    print("Classification Report:\n", report)

def main():
    generate_report()

if __name__ == "__main__":
    main()
