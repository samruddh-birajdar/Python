############################################################################################################################
#
# Program      : Student Marks ML
# Functions    : one_hot_encode_gender(), main()
# Input        : Hardcoded dictionary data with gender
# Output       : DataFrame with one-hot encoded gender
# Description  : Adds gender column and performs one-hot encoding
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def one_hot_encode_gender():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Gender': ['Male', 'Male', 'Female'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    df = pd.get_dummies(df, columns=['Gender'])
    print(df)
    return df

def main():
    df = one_hot_encode_gender()

if __name__ == "__main__":
    main()
