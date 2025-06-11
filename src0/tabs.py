from tabulate import tabulate

# Sample data
data = [
    {"name": "Alice", "age": 25, "score": 95.5, "subject": "Math"},
    {"name": "Bob", "age": 22, "score": 87.0, "subject": "Science"},
    {"name": "Charlie", "age": 23, "score": 92.5, "subject": "History"},
]

# Define table headers
headers = ["Name", "Age", "Score", "Subject"]

# Extract data in list format for tabulate
table_data = [[row["name"], row["age"], row["score"], row["subject"]] for row in data]

# Display table
print(tabulate(table_data, headers=headers, tablefmt="grid"))