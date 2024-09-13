from pymongo import MongoClient

# Establish connection with Pymongo with correct URL
client = MongoClient('localhost', 27017)

db = client.mydb

status = db.status

# Creating or inserting documents
status_1 = { "task": "Create fetch command to fetch data", "date": "14-09-2024", "status": "notdone" }

status.insert_one(status_1)

status_1 = status.find_one()

print(status_1)

# Updating a document
status.update_one({"task": "Create fetch command to fetch data"}, {"$set": {"status": "done"}})

# Deleting a document
status.delete_one({"task": "Reupdating in DB"})

print(status_1)
