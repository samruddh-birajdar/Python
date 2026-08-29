############################################################################################################################
#
# Program      : Student Marks ML
# Functions    : group_by_gender(), main()
# Input        : Hardcoded dictionary data with gender
# Output       : Average marks grouped by gender
# Description  : Groups students by gender and calculates average marks
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def group_by_gender():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Gender': ['Male', 'Male', 'Female'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    print(df.groupby('Gender')[['Math','Science','English']].mean())
    return df

def main():
    df = group_by_gender()

if __name__ == "__main__":
    main()
