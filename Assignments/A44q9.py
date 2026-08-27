############################################################################################################################
#
# Program      : Student Marks DataFrame
# Functions    : fill_missing_values(), main()
# Input        : Hardcoded dictionary data with missing values
# Output       : DataFrame with missing values filled by column mean
# Description  : Handles missing values using mean imputation
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
import numpy as np

def fill_missing_values():
    data2 = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [np.nan, 76, 88],
        'Science': [91, np.nan, 85]
    }
    df = pd.DataFrame(data2)
    df['Math'].fillna(df['Math'].mean(), inplace=True)
    df['Science'].fillna(df['Science'].mean(), inplace=True)
    print(df)
    return df

def main():
    df = fill_missing_values()

if __name__ == "__main__":
    main()
