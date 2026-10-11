import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, 25, 22, 30, 28],
    "Marks": [85, 72, 90, 65, 88],
    "City": ["Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

print("First 3 rows:")
print(df.head(3))

print("\nLast 2 rows:")
print(df.tail(2))

print("\nShape of DataFrame:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nNames and Marks:")
print(df[["Name", "Marks"]])

print("\nStudents with marks above 80:")
print(df[df["Marks"] > 80])

print("\nStudents sorted by marks high to low:")
print(df.sort_values(by="Marks", ascending=False))
