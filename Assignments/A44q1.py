############################################################################################################################
#
# Program      : Student Marks DataFrame 
# Functions    : create_dataframe(), main()
# Input        : Hardcoded dictionary data
# Output       : Shape, Columns, Data types
# Description  : Creates DataFrame and prints basic info.
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def create_dataframe():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("Data Types:\n", df.dtypes)
    return df

def main():
    df = create_dataframe()

if __name__ == "__main__":
    main()
