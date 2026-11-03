

import numpy as np
def linear_regression_gradient_descent(X:np.ndarray, y:np.ndarray, alpha = 0.1 , iterations = 1000):
    m,n = X.shape  
    y = y.reshape(-1, 1)
    theta = np.zeros((n, 1))
    for i in range(iterations):
        y_pred = X@theta
        error = y_pred - y
        gradient = (X.T@error)/m
        theta = theta - alpha * gradient
    return theta.flatten()
X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 3])
result =linear_regression_gradient_descent(X, y)
print(np.round(result,4))