############################################################################################################################
#
# Program      : Student Marks ML
# Functions    : rename_math_column(), main()
# Input        : Hardcoded dictionary data
# Output       : DataFrame with 'Math' renamed to 'Mathematics'
# Description  : Renames Math column to Mathematics
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def rename_math_column():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    df.rename(columns={'Math':'Mathematics'}, inplace=True)
    print(df)
    return df

def main():
    df = rename_math_column()

if __name__ == "__main__":
    main()
