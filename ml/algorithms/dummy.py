import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data = {
    "YearsExperience": [1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.2, 3.7, 3.9, 4.0, 4.0, 4.1, 4.5, 4.9, 5.1, 5.3, 5.9, 6.0, 6.8, 7.1, 7.9, 8.2, 8.7, 9.0, 9.5, 9.6, 10.3, 10.5],
    "Salary": [39343, 46205, 37731, 43525, 39891, 56642, 60150, 54445, 64445, 57189, 63218, 55794, 56957, 57081, 61111, 67938, 66029, 83088, 81363, 93940, 91738, 98273, 101302, 113812, 109431, 105582, 116969, 112635, 122391, 121872]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Plot
plt.figure(figsize=(8, 5))
plt.scatter(df["YearsExperience"], df["Salary"], color='blue', label="Salary Data")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Years of Experience vs. Salary")
plt.legend()
plt.grid(True)
plt.show()
