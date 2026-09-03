############################################################################################################################
#
# Program      : Advertising Sales Prediction
# Functions    : prepare_data(), main()
# Input        : MarvellousAdvertising.csv file
# Output       : Cleaned and prepared DataFrame
# Description  : Prepares dataset for ML algorithms
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd

def prepare_data():
    df = pd.read_csv("Advertising.csv")
    # Check for missing values
    df = df.dropna()
    print(df.info())
    return df

def main():
    df = prepare_data()

if __name__ == "__main__":
    main()
