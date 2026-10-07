import pandas as pd
import numpy as np

# Create sample dataset
data = {
    "Name": ["shubham", "kartik", "nayra", "saurabh", "pinki", "ujwal"],
    "Age": [23, 23, np.nan, 22, 25, np.nan],
    "Gender": ["Male", "male", "Female", "Male", "FEMALE", "Male"],
    "Marks": [95, 90, 78, 85, np.nan, 88]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Fill missing numerical values with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Handle inconsistent categorical values
df["Gender"] = df["Gender"].str.lower()

# Remove duplicate records
df = df.drop_duplicates()

print("\nCleaned Dataset:")
print(df)

print("\nMissing values after cleaning:")
print(df.isnull().sum())
