import pandas as pd

data = {
    "Employee": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Department": ["CS", "CS", "IT", "IT", "CS", "IT", "HR", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 70000, 75000, 40000, 45000],
    "Experience": [2, 4, 3, 5, 6, 7, 1, 2]
}

df = pd.DataFrame(data)

group = df.groupby("Department")

print("Average Salary:")
print(group["Salary"].mean())

print("\nMaximum Salary:")
print(group["Salary"].max())

print("\nMinimum Salary:")
print(group["Salary"].min())

print("\nAverage Experience:")
print(group["Experience"].mean())

average_salary = group["Salary"].mean()
print("\nDepartment with highest average salary:")
print(average_salary.idxmax())

print("\nNumber of Employees:")
print(group["Employee"].count())

print("\nDepartments sorted by average salary:")
print(average_salary.sort_values(ascending=False))
