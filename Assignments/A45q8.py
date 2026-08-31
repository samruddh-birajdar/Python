############################################################################################################################
#
# Program      : Student Marks ML
# Functions    : plot_histogram_math(), main()
# Input        : Hardcoded dictionary data
# Output       : Histogram of Math marks
# Description  : Plots histogram of Math marks
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
import matplotlib.pyplot as plt

def plot_histogram_math():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    plt.hist(df['Math'], bins=5, color='skyblue', edgecolor='black')
    plt.xlabel("Math Marks")
    plt.ylabel("Frequency")
    plt.title("Histogram of Math Marks")
    plt.show()

def main():
    plot_histogram_math()

if __name__ == "__main__":
    main()
