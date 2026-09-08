############################################################################################################################
#
# Program      : Euclidean Distance before and after Scaling
# Functions    : calculate_distance(), main()
# Input        : Two points [25,20000], [35,80000]
# Output       : Euclidean distance before and after scaling
# Description  : Compares Euclidean distance before and after feature scaling
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def calculate_distance():
    point1 = np.array([25,20000])
    point2 = np.array([35,80000])

    # Distance before scaling
    dist_before = np.linalg.norm(point1 - point2)
    print("Distance before scaling:", dist_before)

    # Apply scaling
    data = [[25,20000],[35,80000]]
    df = pd.DataFrame(data, columns=['Age','Income'])
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)

    dist_after = np.linalg.norm(scaled[0] - scaled[1])
    print("Distance after scaling:", dist_after)

    print("\nExplanation:")
    print("Before scaling, the income feature dominates the distance due to large values.")
    print("After scaling, both features contribute equally, giving a balanced distance.")

def main():
    calculate_distance()

if __name__ == "__main__":
    main()
