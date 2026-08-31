############################################################################################################################
#
# Program      : Student Marks ML
# Functions    : export_to_csv(), main()
# Input        : Hardcoded dictionary data
# Output       : CSV file exported
# Description  : Exports DataFrame to CSV file
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def export_to_csv():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    df.to_csv("student_marks.csv", index=False)
    print("Data exported to student_marks.csv")
    return df

def main():
    df = export_to_csv()

if __name__ == "__main__":
    main()
