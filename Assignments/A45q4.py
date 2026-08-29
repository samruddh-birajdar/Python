############################################################################################################################
#
# Program      : Student Marks ML
# Functions    : plot_pie_sagar(), main()
# Input        : Hardcoded dictionary data
# Output       : Pie chart of Sagar's subject marks
# Description  : Plots pie chart of subject marks for Sagar
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
import matplotlib.pyplot as plt

def plot_pie_sagar():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    sagar_marks = df[df['Name'] == 'Sagar'][['Math','Science','English']].values.flatten()
    subjects = ['Math','Science','English']
    plt.pie(sagar_marks, labels=subjects, autopct='%1.1f%%')
    plt.title("Sagar's Subject Marks")
    plt.show()

def main():
    plot_pie_sagar()

if __name__ == "__main__":
    main()
