############################################################################################################################
#
# Program      : Variance Calculation
# Functions    : calculate_variance(), main()
# Input        : Dataset [4,6,8,10,12]
# Output       : Mean, Deviations, Squared Deviations, Variance
# Description  : Calculates variance step by step
# Author       : Samruddh Shivkumar Birajdar
#
############################################################################################################################

def calculate_variance():
    data = [4,6,8,10,12]
    mean_val = sum(data)/len(data)
    print("Mean:", mean_val)

    deviations = [x - mean_val for x in data]
    print("Deviations:", deviations)

    squared_dev = [d**2 for d in deviations]
    print("Squared Deviations:", squared_dev)

    variance = sum(squared_dev)/len(data)
    print("Variance:", variance)

def main():
    calculate_variance()

if __name__ == "__main__":
    main()
