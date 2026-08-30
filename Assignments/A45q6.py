############################################################################################################################
#
# Program      : Student Marks ML
# Functions    : count_passed_students(), main()
# Input        : Hardcoded dictionary data
# Output       : Number of students who passed
# Description  : Counts students with Status = Pass
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def count_passed_students():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    df['Total'] = df[['Math','Science','English']].sum(axis=1)
    df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')
    print("Number of students passed:", (df['Status'] == 'Pass').sum())
    return df

def main():
    df = count_passed_students()

if __name__ == "__main__":
    main()
