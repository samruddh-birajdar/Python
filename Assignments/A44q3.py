############################################################################################################################
#
# Program      : Student Marks DataFrame
# Functions    : add_total_column(), main()
# Input        : Hardcoded dictionary data
# Output       : DataFrame with 'Total' column
# Description  : Adds new column 'Total' as sum of marks
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def add_total_column():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    df['Total'] = df[['Math','Science','English']].sum(axis=1)
    print(df)
    return df

def main():
    df = add_total_column()

if __name__ == "__main__":
    main()
