############################################################################################################################
#
# Program      : Variance and Standard Deviation
# Functions    : calculate_variance_std(), main()
# Input        : Dataset [6,7,8,9,10,11,12]
# Output       : Variance and Standard Deviation
# Description  : Calculates variance and standard deviation using NumPy
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import numpy as np

def calculate_variance_std():
    data = [6,7,8,9,10,11,12]
    variance = np.var(data)
    std_dev = np.std(data)
    print("Variance:", variance)
    print("Standard Deviation:", std_dev)

def main():
    calculate_variance_std()

if __name__ == "__main__":
    main()
