############################################################################################################################
#
# Program      : Student Marks DataFrame
# Functions    : sort_by_total(), main()
# Input        : Hardcoded dictionary data
# Output       : DataFrame sorted by 'Total' marks in descending order
# Description  : Sorts DataFrame by total marks
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def sort_by_total():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    df['Total'] = df[['Math','Science','English']].sum(axis=1)
    df = df.sort_values(by='Total', ascending=False)
    print(df)
    return df

def main():
    df = sort_by_total()

if __name__ == "__main__":
    main()
