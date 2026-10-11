import numpy as np

X = np.array([
    [10, 100, 1000],
    [20, 200, 2000],
    [30, 300, 3000],
    [40, 400, 4000],
    [50, 500, 5000]
], dtype=float)

mean = np.mean(X, axis=0)
print("Column means:", mean)

std = np.std(X, axis=0)
print("Column standard deviations:", std)

X_scaled = (X - mean) / std

print("\nStandardized matrix:")
print(X_scaled)

print("\nScaled column means:", np.mean(X_scaled, axis=0))
print("Scaled column standard deviations:", np.std(X_scaled, axis=0))

print("\nStandardization completed without loops.")
