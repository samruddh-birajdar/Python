############################################################################################################################
#
# Program      : Advertising Sales Prediction
# Functions    : load_data(), main()
# Input        : MarvellousAdvertising.csv file
# Output       : Loaded DataFrame
# Description  : Loads dataset into Python application
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def load_data():
    df = pd.read_csv("MarvellousAdvertising.csv")
    print(df.head())
    return df

def main():
    df = load_data()

if __name__ == "__main__":
    main()
