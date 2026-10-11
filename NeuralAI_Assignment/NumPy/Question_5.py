import numpy as np

X = np.array([
    [1, 10],
    [2, 20],
    [3, 30],
    [4, 40],
    [5, 50],
    [6, 60],
    [7, 70],
    [8, 80],
    [9, 90],
    [10, 100]
])

y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

np.random.seed(42)

indices = np.random.permutation(len(X))

X_shuffled = X[indices]
y_shuffled = y[indices]

split_index = int(0.8 * len(X_shuffled))

X_train = X_shuffled[:split_index]
X_test = X_shuffled[split_index:]

y_train = y_shuffled[:split_index]
y_test = y_shuffled[split_index:]

train_mean = np.mean(X_train, axis=0)
train_std = np.std(X_train, axis=0)

X_train_scaled = (X_train - train_mean) / train_std
X_test_scaled = (X_test - train_mean) / train_std

print("Shapes:")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

print("\nFirst 3 Training Samples Before Scaling:")
print(X_train[:3])

print("\nFirst 3 Training Samples After Scaling:")
print(X_train_scaled[:3])

print("\nTraining Mean After Scaling:")
print(np.mean(X_train_scaled, axis=0))

print("\nTraining Standard Deviation After Scaling:")
print(np.std(X_train_scaled, axis=0))