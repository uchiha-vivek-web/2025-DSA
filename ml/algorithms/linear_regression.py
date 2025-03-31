""" Implementing linear regression from scratch """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Linear_Regression():
    def __init__(self, learning_rate=0.01, no_of_iterations=1000):
        self.learning_rate = learning_rate
        self.no_of_iterations = no_of_iterations
    
    # X --> years of experience, y --> salary
    def fit(self, X, y):
        # Number of data points (m) and features (n)
        self.m, self.n = X.shape
        # Initialize weights (w) and bias (b)
        self.w = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.y = y
        
        """ Implementing gradient descent """
        for i in range(self.no_of_iterations):
            self.update_weights()

    def update_weights(self):
        # Predictions
        y_pred = self.predict(self.X)
        
        """ Calculate gradients """
        dw = (-2 / self.m) * (self.X.T @ (self.y - y_pred))
        db = (-2 / self.m) * np.sum(self.y - y_pred)
        
        """ Update the weights """
        self.w -= self.learning_rate * dw
        self.b -= self.learning_rate * db

    def predict(self, X):
        return X @ self.w + self.b

# Load dataset
data = pd.read_csv('salary_data.csv')

# Prepare training data
X = data[['YearsExperience']].values  # Feature matrix
y = data['Salary'].values  # Target variable

# Feature scaling (optional but recommended)
X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)
X_scaled = (X - X_mean) / X_std  # Standardization

# Initialize and train model
model = Linear_Regression(learning_rate=0.01, no_of_iterations=1000)
model.fit(X_scaled, y)

# Predict values
y_pred = model.predict(X_scaled)

# Plot results
plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, y_pred, color='red', label='Linear Regression Fit')  # Plot regression line
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()
