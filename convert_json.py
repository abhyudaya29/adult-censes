import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("adult.csv")

# Convert DataFrame to JSON
json_data = df.to_json(orient="records")

# Write JSON data to a file
with open("output.json", "w") as json_file:
    json_file.write(json_data)

print("CSV file converted to JSON successfully.")
