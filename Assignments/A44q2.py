############################################################################################################################
#
# Program      : Student Marks DataFrame
# Functions    : describe_dataframe(), main()
# Input        : Hardcoded dictionary data
# Output       : Descriptive statistics
# Description  : Prints descriptive statistics using .describe()
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def describe_dataframe():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    print(df.describe())
    return df

def main():
    df = describe_dataframe()

if __name__ == "__main__":
    main()
