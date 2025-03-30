import numpy as np
from scipy import stats

# Sample dataset
data = np.array([10, 15, 20, 25, 30, 30, 35, 40, 45, 50, 50, 50])

# Mean
mean_value = np.mean(data)

# Median
median_value = np.median(data)

# Mode
mode_value = stats.mode(data, keepdims=True).mode[0]

# Range
range_value = np.ptp(data)  # ptp: peak-to-peak (max - min)

# Variance
variance_value = np.var(data, ddof=1)  # Sample variance (ddof=1 for unbiased estimate)

# Standard Deviation
std_dev_value = np.std(data, ddof=1)  # Sample standard deviation

# Percentiles
percentile_25 = np.percentile(data, 25)
percentile_50 = np.percentile(data, 50)  # Also the median
percentile_75 = np.percentile(data, 75)

# Quartiles
q1, q2, q3 = np.percentile(data, [25, 50, 75])

# Correlation (Example with another dataset)
data2 = np.array([5, 10, 15, 20, 25, 25, 30, 35, 40, 45, 45, 50])  # Another variable
correlation_matrix = np.corrcoef(data, data2)

# Displaying results
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Range: {range_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {std_dev_value}")
print(f"25th Percentile (Q1): {percentile_25}")
print(f"50th Percentile (Q2 - Median): {percentile_50}")
print(f"75th Percentile (Q3): {percentile_75}")
print(f"Correlation Matrix:\n{correlation_matrix}")

# Causation
# Causation cannot be determined through correlation alone.
# It requires further statistical testing or domain knowledge.
