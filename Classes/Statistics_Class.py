import numpy as np
from scipy import stats

class Statistics:
    def __init__(self):  # Class Constructor
        pass

    def Mean(self, data):  # Method {Mean()} to calculate the value of Mean for the data set in the parameter.
        return np.mean(data)  # Calculating the value of the Mean using {mean()} function from {numpy} module.

    def Median(self, data):  # Method {Median()} to calculate the value of Median for the data set in the parameter.
        return np.median(data)  # Calculating the value of the Median using {median()} function from {numpy} module.

    def Mod(self, data):  # Method {Mod()} to calculate the value of Mod for the data set in the parameter.
        return stats.mode(data)  # Calculating the value of the Mod using {mod()} function from {stats} module.

    def Variance(self, data):  # Method {Variance()} to calculate the value of Variance for the data set in the parameter.
        return np.var(data)  # Calculating the value of the Variance using {var()} function from {numpy} module.

    def Standard_Deviation(self, data):  # Method {Standard_Deviation()} to calculate the value of Standard Deviation for the data set in the parameter.
        return np.std(data)  # Calculating the value of the Standard Deviation using {std()} function from {numpy} module.