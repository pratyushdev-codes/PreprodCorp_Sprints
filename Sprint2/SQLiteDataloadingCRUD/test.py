import sqlite3
import pandas as pd

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

df_csv = pd.read_csv('MOCK_DATA.csv')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS mock_data_csv (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        gender TEXT,
        ip_address TEXT
    )
''')
conn.commit()

df_csv.to_sql('mock_data_csv', conn, if_exists='replace', index=False)

print("Initial Data:")
cursor.execute('SELECT * FROM mock_data_csv LIMIT 8')
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
    INSERT INTO mock_data_csv (first_name, last_name, email, gender, ip_address)
    VALUES ('Aleta', 'Wyne', 'awyne0@4shared.com', 'Female', '125.59.65.232')
''')
conn.commit()

print("\nAfter Insert:")
cursor.execute('SELECT * FROM mock_data_csv WHERE email = "edupoy5@businessweek.com"')
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
    UPDATE mock_data_csv
    SET first_name = 'Jane', email = 'jane.doe@example.com'
    WHERE email = 'wferbrachec@cisco.com'
''')
conn.commit()

print("\nAfter Update:")
cursor.execute('SELECT * FROM mock_data_csv WHERE email = "rowelr@jalbum.net"')
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
    DELETE FROM mock_data_csv
    WHERE email = 'jane.doe@example.com'
''')
conn.commit()

print("\nAfter Delete:")
cursor.execute('SELECT * FROM mock_data_csv WHERE email = "mouth1z@wikipedia.org"')
rows = cursor.fetchall()
if not rows:
    print("No records found")

conn.close()
