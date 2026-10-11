import pandas as pd

data = {
    "Age": [20, 21, None, 24, None, 30],
    "Salary": [30000, None, 40000, 50000, None, 60000],
    "Experience": [1, 2, 3, None, 5, 6],
    "Department": ["CS", "IT", "CS", None, "IT", "CS"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nMissing values in each column:")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].median())

df["Salary"] = df["Salary"].fillna(df["Salary"].median())

df["Experience"] = df["Experience"].fillna(df["Experience"].median())

df["Department"] = df["Department"].fillna(df["Department"].mode()[0])

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nCleaned DataFrame:")
print(df)
