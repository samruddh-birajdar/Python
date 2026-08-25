############################################################################################################################
#
# Program      : Student Marks DataFrame
# Functions    : replace_name(), main()
# Input        : Hardcoded dictionary data
# Output       : DataFrame with 'Pooja' replaced by 'Puja'
# Description  : Replaces value in 'Name' column
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def replace_name():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    df['Name'] = df['Name'].replace('Pooja','Puja')
    print(df)
    return df

def main():
    df = replace_name()

if __name__ == "__main__":
    main()
