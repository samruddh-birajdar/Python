############################################################################################################################
#
# Program      : Student Marks DataFrame
# Functions    : plot_bar(), main()
# Input        : Hardcoded dictionary data
# Output       : Bar plot of student names vs total marks
# Description  : Creates bar plot using matplotlib
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
import matplotlib.pyplot as plt

def plot_bar():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    df['Total'] = df[['Math','Science','English']].sum(axis=1)
    plt.bar(df['Name'], df['Total'])
    plt.xlabel("Students")
    plt.ylabel("Total Marks")
    plt.title("Student Names vs Total Marks")
    plt.show()

def main():
    plot_bar()

if __name__ == "__main__":
    main()
