import matplotlib.pyplot as plt

def plot_results(X, y, y_pred):
    """Plot actual vs predicted values."""
    plt.scatter(X, y, color='blue', label='Actual Data')
    plt.plot(X, y_pred, color='red', label='Linear Regression Fit')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.legend()
    plt.show()
