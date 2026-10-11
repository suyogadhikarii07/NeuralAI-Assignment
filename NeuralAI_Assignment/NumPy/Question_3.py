import numpy as np

X = np.array([
    [25, 50000],
    [17, 30000],
    [35, 80000],
    [42, 90000],
    [19, 25000],
    [31, 70000]
])

age = X[:, 0]
salary = X[:, 1]

print("People aged 25 or above:")
print(X[age >= 25])

print("\nPeople earning more than 60000:")
print(X[salary > 60000])

condition = (age >= 25) & (salary > 60000)
print("\nPeople aged >= 25 and earning > 60000:")
print(X[condition])

X[X[:, 1] < 30000, 1] = 30000
print("\nDataset after salary replacement:")
print(X)

print("\nAverage salary:", np.mean(X[:, 1]))

eligible_salary = X[X[:, 0] >= 25, 1]
print("Average salary for people aged >= 25:",np.mean(eligible_salary))
