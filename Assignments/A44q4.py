############################################################################################################################
#
# Program      : Student Marks DataFrame
# Functions    : filter_science_marks(), main()
# Input        : Hardcoded dictionary data
# Output       : Students scoring more than 85 in Science
# Description  : Filters DataFrame based on Science marks
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def filter_science_marks():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    print(df[df['Science'] > 85])
    return df

def main():
    df = filter_science_marks()

if __name__ == "__main__":
    main()
