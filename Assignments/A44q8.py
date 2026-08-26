############################################################################################################################
#
# Program      : Student Marks DataFrame
# Functions    : plot_line(), main()
# Input        : Hardcoded dictionary data
# Output       : Line chart of Amit's marks across subjects
# Description  : Plots line chart for Amit's marks
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
import matplotlib.pyplot as plt

def plot_line():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    amit_marks = df[df['Name'] == 'Amit'][['Math','Science','English']].values.flatten()
    subjects = ['Math','Science','English']
    plt.plot(subjects, amit_marks, marker='o')
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Amit's Marks Across Subjects")
    plt.show()

def main():
    plot_line()

if __name__ == "__main__":
    main()
