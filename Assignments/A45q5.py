############################################################################################################################
#
# Program      : Student Marks ML
# Functions    : add_status_column(), main()
# Input        : Hardcoded dictionary data
# Output       : DataFrame with 'Status' column
# Description  : Adds Status column based on total marks
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def add_status_column():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    df['Total'] = df[['Math','Science','English']].sum(axis=1)
    df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')
    print(df)
    return df

def main():
    df = add_status_column()

if __name__ == "__main__":
    main()
