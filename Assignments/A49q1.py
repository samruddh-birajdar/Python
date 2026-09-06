############################################################################################################################
#
# Program      : Mean Calculation using NumPy
# Functions    : calculate_mean(), main()
# Input        : Dataset [6,7,8,9,10,11,12]
# Output       : Mean of dataset
# Description  : Calculates mean using NumPy
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import numpy as np

def calculate_mean():
    data = [6,7,8,9,10,11,12]
    mean_val = np.mean(data)
    print("Mean of dataset:", mean_val)

def main():
    calculate_mean()

if __name__ == "__main__":
    main()
