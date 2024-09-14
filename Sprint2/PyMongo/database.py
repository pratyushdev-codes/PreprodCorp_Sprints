import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.mydb
collection = db.mock_data_csv

# Load CSV file
df_csv = pd.read_csv('MOCK_DATA.csv')

# Convert DataFrame to dictionary and insert into MongoDB
data_dict = df_csv.to_dict('records')
collection.insert_many(data_dict)

# Verify data insertion
print("Initial Data:")
for doc in collection.find().limit(8):
    print(doc)

# Create: Insert a new document
new_user = {
    "first_name": "Aleta",
    "last_name": "Wyne",
    "email": "awyne0@4shared.com",
    "gender": "Female",
    "ip_address": "125.59.65.232"
}
collection.insert_one(new_user)

print("\nAfter Insert:")
for doc in collection.find({"email": "awyne0@4shared.com"}):
    print(doc)

# Update: Modify a document
collection.update_one(
    {"email": "wferbrachec@cisco.com"},
    {"$set": {"first_name": "Jane", "email": "jane.doe@example.com"}}
)

print("\nAfter Update:")
for doc in collection.find({"email": "jane.doe@example.com"}):
    print(doc)

# Delete: Remove a document
collection.delete_one({"email": "jane.doe@example.com"})

print("\nAfter Delete:")
if collection.find_one({"email": "jane.doe@example.com"}) is None:
    print("No records found")

# Close the connection
client.close()
