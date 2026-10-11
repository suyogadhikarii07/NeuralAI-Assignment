import pandas as pd
import numpy as np

data = {
    "Age": [20, 25, 30, 35, 40, 45, 50, 55],
    "Salary": [25000, 30000, 40000, 50000, 60000, 70000, 80000, 90000],
    "Experience": [1, 2, 5, 7, 10, 12, 15, 20],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune",
             "Mumbai", "Delhi", "Pune", "Delhi"],
    "Purchased": [0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df.drop("Purchased", axis=1)
y = df["Purchased"]

X = pd.get_dummies(X, columns=["City"], dtype=int)

X = X.to_numpy(dtype=float)
y = y.to_numpy()

print("Original shapes:")
print("X shape:", X.shape)
print("y shape:", y.shape)

np.random.seed(42)
order = np.random.permutation(len(X))

X = X[order]
y = y[order]

split = int(0.8 * len(X))

X_train = X[:split]
X_test = X[split:]
y_train = y[:split]
y_test = y[split:]

mean = np.mean(X_train, axis=0)
std = np.std(X_train, axis=0)

std[std == 0] = 1

X_train = (X_train - mean) / std

X_test = (X_test - mean) / std

print("\nShapes after splitting:")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

print("\nFinal X_train:")
print(X_train)
print("\nFinal X_test:")
print(X_test)
print("\nFinal y_train:")
print(y_train)
print("\nFinal y_test:")
print(y_test)
