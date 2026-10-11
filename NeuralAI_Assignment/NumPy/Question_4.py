import numpy as np

X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6]
])

y = np.array([3, 5, 7, 9, 11])

X_bias = np.column_stack((np.ones(X.shape[0]), X))
print("X with bias column:")
print(X_bias)

XTX = X_bias.T @ X_bias
print("\nX.T @ X:")
print(XTX)

XTy = X_bias.T @ y
print("\nX.T @ y:")
print(XTy)

w = np.linalg.pinv(XTX) @ XTy
print("\nWeights:")
print(w)

y_pred = X_bias @ w
print("\nPredicted y:")
print(y_pred)

# errors = y - y_pred
# squared_errors = errors ** 2
# mse = np.sum(squared_errors) / len(y)
mse = np.mean((y - y_pred) ** 2)
print("MSE:", mse)
