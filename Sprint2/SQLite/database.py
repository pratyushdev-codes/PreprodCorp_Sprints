import sqlite3

# Create a connection to the database
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
print("Opened Successfully")

# Create a table
command_create = """
CREATE TABLE IF NOT EXISTS status (
    id INTEGER PRIMARY KEY, 
    task TEXT, 
    date TEXT, 
    status TEXT
)
"""
cur.execute(command_create)
print("Table created")

# Inserting into the table
command_insert = """
INSERT INTO status (id, task, date, status) 
VALUES 
    (1, 'Insert Operations for SQLite', '13-09-2024', 'done'),
    (2, 'Create fetch command to fetch data', '14-09-2024', 'done')
"""
cur.execute(command_insert)
print("Inserted into table")
con.commit()

# Fetching data from the table
command_retrieve = "SELECT * FROM status"
cur.execute(command_retrieve)
rows = cur.fetchall()

for row in rows:
    id, task, date, status = row
    print(id, task, date, status)

# Update the status of a task
command_update = "UPDATE status SET status='done' WHERE id=2"
cur.execute(command_update)
con.commit()
print("Updated")

# Delete a row from the table
command_delete = "DELETE FROM status WHERE id=1"
cur.execute(command_delete)
con.commit()
print("Deleted")

# Close the connection
cur.close()
con.close()
