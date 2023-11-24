import numpy as np


class LinearRegression:

        def __init__(self, lr=0.001, n_iters=500):
                self.lr = lr
                self.n_iters = n_iters
                self.weights = None
                self.bias = None
        def fit(self, X, y):
                n_samples, n_features = X.shape
                self.weights = np.zeros(n_features)
                self.bias = 0

                for _ in range(self.n_iters):
                        # Prediction
                        yhat = self.bias + np.dot(X, self.weights)
                        # Derivatives
                        dw = (1/n_samples) * np.dot(X.T, (yhat-y))
                        db = (1/n_samples) * np.sum(yhat - y)
                        # GD
                        self.weights = self.weights - self.lr * dw
                        self.bias = self.bias - self.lr * db
        def predict(self, X):
                yhat = self.bias + np.dot(X, self.weights)
                return yhat

