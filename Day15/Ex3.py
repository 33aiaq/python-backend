import pandas as pd

data = {
    "Name": ["Ahmed", "Layla", "Khaled", "Sara", "Mahmoud", "Noor", "Omar", "Huda"],
    "Age": [25, 30, 45, 35, 28, 40, 50, 38],
    "Department": ["HR", "IT", "IT", "Finance", "HR", "Finance", "IT", "HR"],
    "Salary": [4000, 5000, 7000, 6500, 4200, 7200, 8000, 4800]
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

df["Bonus"] = df["Salary"] * 0.10
print("\nData with Bonus:\n", df)

grouped = df.groupby("Department")[["Salary", "Bonus"]].mean()
print("\nAverage Salary and Bonus by Department:\n", grouped)

highest_salary = df.loc[df.groupby("Department")["Salary"].idxmax()]
print("\nEmployee with Highest Salary in Each Department:\n", highest_salary)

df["AgeGroup"] = pd.cut(df["Age"], bins=[20,30,40,50,60], labels=["20-30","31-40","41-50","51-60"])
pivot = pd.pivot_table(df, values="Salary", index="Department", columns="AgeGroup", aggfunc="mean")
print("\nPivot Table - Average Salary by Department and Age Group:\n", pivot)
