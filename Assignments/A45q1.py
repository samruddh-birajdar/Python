############################################################################################################################
#
# Program      : Student Marks ML
# Functions    : normalize_math(), main()
# Input        : Hardcoded dictionary data
# Output       : DataFrame with normalized Math scores
# Description  : Normalizes Math scores using Min-Max scaling
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def normalize_math():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    df['Math_Normalized'] = (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min())
    print(df)
    return df

def main():
    df = normalize_math()

if __name__ == "__main__":
    main()
