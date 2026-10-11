import numpy as np
X = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [100, 110, 120]
])

print("Shape:", X.shape)
print("Dimensions:", X.ndim)
print("Data type:", X.dtype)

print("\nSecond column:")
print(X[:, 1])

print("\nFirst two rows:")
print(X[:2, :])

print("\nLast two columns:")
print(X[:, -2:])

X[X > 80] = 0
print("\nArray after replacing values greater than 80:")
print(X)

print("\nColumn wise minimum:", np.min(X, axis=0))
print("Column wise maximum:", np.max(X, axis=0))
print("Column wise mean:", np.mean(X, axis=0))
print("Column wise standard deviation:", np.std(X, axis=0))
