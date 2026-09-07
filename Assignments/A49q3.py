############################################################################################################################
#
# Program      : Feature Scaling using StandardScaler
# Functions    : perform_scaling(), main()
# Input        : Dataset [[25,20000],[30,40000],[35,80000]]
# Output       : Scaled dataset
# Description  : Performs feature scaling using StandardScaler
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

import pandas as pd
from sklearn.preprocessing import StandardScaler

def perform_scaling():
    data = [[25,20000],[30,40000],[35,80000]]
    df = pd.DataFrame(data, columns=['Age','Income'])
    scaler = StandardScaler()
    scaled = scaler.fit_transform(df)
    print("Scaled Dataset:\n", scaled)

def main():
    perform_scaling()

if __name__ == "__main__":
    main()
