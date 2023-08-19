import pandas as pd
from pymongo import MongoClient

# Read the CSV file into a DataFrame
df = pd.read_csv("adult.csv")

# Convert DataFrame to JSON
json_data = df.to_dict(orient="records")

# MongoDB URI
uri = "mongodb+srv://dev:dev@cluster0.qg3gmlv.mongodb.net/test?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)
db = client["census"]  # Replace with your database name
collection = db["dev"]

# Insert JSON data into the collection
collection.insert_many(json_data)

print("JSON data deployed to MongoDB successfully.")
