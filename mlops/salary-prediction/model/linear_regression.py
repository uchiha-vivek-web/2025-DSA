import numpy as np

class LinearRegression:
    def __init__(self, learning_rate=0.01, no_of_iterations=1000):
        self.learning_rate = learning_rate
        self.no_of_iterations = no_of_iterations
    
    def fit(self, X, y):
        self.m, self.n = X.shape
        self.w = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.y = y
        
        for _ in range(self.no_of_iterations):
            self.update_weights()

    def update_weights(self):
        y_pred = self.predict(self.X)
        dw = (-2 / self.m) * (self.X.T @ (self.y - y_pred))
        db = (-2 / self.m) * np.sum(self.y - y_pred)
        self.w -= self.learning_rate * dw
        self.b -= self.learning_rate * db

    def predict(self, X):
        return X @ self.w + self.b
