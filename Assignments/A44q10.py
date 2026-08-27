############################################################################################################################
#
# Program      : Student Marks DataFrame
# Functions    : drop_english_column(), main()
# Input        : Hardcoded dictionary data
# Output       : DataFrame without 'English' column
# Description  : Drops English column from DataFrame
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def drop_english_column():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    df = df.drop(columns=['English'])
    print(df)
    return df

def main():
    df = drop_english_column()

if __name__ == "__main__":
    main()
