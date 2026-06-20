import pandas as pd

# Load the dataset
df = pd.read_csv('hospital_readmission_dataset.csv')

# Display first few rows
print("="*60)
print("FIRST 5 ROWS OF DATA:")
print("="*60)
print(df.head())

# Display dataset info
print("\n" + "="*60)
print("DATASET INFORMATION:")
print("="*60)
print(df.info())

# Display basic statistics
print("\n" + "="*60)
print("BASIC STATISTICS:")
print("="*60)
print(df.describe())

# Display shape (rows and columns)
print("\n" + "="*60)
print(f"DATASET SIZE: {df.shape[0]} rows, {df.shape[1]} columns")
print("="*60)

# Show column names
print("\nCOLUMN NAMES:")
print(df.columns.tolist())

# Check for missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())