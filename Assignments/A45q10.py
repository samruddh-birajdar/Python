############################################################################################################################
#
# Program      : Student Marks ML
# Functions    : plot_boxplot_english(), main()
# Input        : Hardcoded dictionary data
# Output       : Boxplot of English marks
# Description  : Plots boxplot for English marks to check distribution and outliers
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
import matplotlib.pyplot as plt

def plot_boxplot_english():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    plt.boxplot(df['English'])
    plt.title("Boxplot of English Marks")
    plt.ylabel("Marks")
    plt.show()

def main():
    plot_boxplot_english()

if __name__ == "__main__":
    main()

