############################################################################################################################
#
# Program      : Confusion Matrix Values
# Functions    : calculate_confusion_values(), main()
# Input        : Actual and Predicted arrays
# Output       : TP, TN, FP, FN
# Description  : Calculates confusion matrix values manually
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def calculate_confusion_values():
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    TP = sum([1 for i in range(len(actual)) if actual[i]==1 and predicted[i]==1])
    TN = sum([1 for i in range(len(actual)) if actual[i]==0 and predicted[i]==0])
    FP = sum([1 for i in range(len(actual)) if actual[i]==0 and predicted[i]==1])
    FN = sum([1 for i in range(len(actual)) if actual[i]==1 and predicted[i]==0])

    print("True Positive (TP):", TP)
    print("True Negative (TN):", TN)
    print("False Positive (FP):", FP)
    print("False Negative (FN):", FN)

def main():
    calculate_confusion_values()

if __name__ == "__main__":
    main()
