from model.linear_regression import LinearRegression
from utils.preprocess import load_data, feature_scaling
from utils.plot import plot_results

# Load dataset
data = load_data('data/salary_data.csv')

# Prepare training data
X = data[['YearsExperience']].values  # Feature matrix
y = data['Salary'].values  # Target variable

# Feature scaling
X_scaled, X_mean, X_std = feature_scaling(X)

# Train model
model = LinearRegression(learning_rate=0.01, no_of_iterations=1000)
model.fit(X_scaled, y)

# Predictions
y_pred = model.predict(X_scaled)

# Plot results
plot_results(X, y, y_pred)
