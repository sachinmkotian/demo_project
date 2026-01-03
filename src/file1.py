import pandas as pd

# Sample data: A dictionary of lists
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 32, 28, 22, 30],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Miami"],
    "Salary": [70000, 85000, 75000, 60000, 90000],
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
