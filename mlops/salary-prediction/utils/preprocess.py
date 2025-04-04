import pandas as pd
import numpy as np

def load_data(file_path):
    """Load dataset from CSV file."""
    return pd.read_csv(file_path)

def feature_scaling(X):
    """Apply standardization to the feature matrix."""
    X_mean = np.mean(X, axis=0)
    X_std = np.std(X, axis=0)
    return (X - X_mean) / X_std, X_mean, X_std
