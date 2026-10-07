import pandas as pd
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add target/label
df["label"] = iris.target

print("First 5 observations:")
print(df.head())

print("\nShape of dataset:")
print(df.shape)

print("\nFeatures:")
print(iris.feature_names)

print("\nLabels:")
print(iris.target_names)

print("\nData types:")
print(df.dtypes)

print("\nBasic statistical characteristics:")
print(df.describe())

print("\nNumber of observations:", df.shape[0])
print("Number of features:", len(iris.feature_names))

