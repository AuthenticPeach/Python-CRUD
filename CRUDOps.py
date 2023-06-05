import sqlite3
"""
## CREATE 
# Connect to the database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Create the 'users' table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  email TEXT)''')

# Insert a new record into the 'users' table
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("John Doe", "john@example.com"))

# Commit the transaction and close the connection
connection.commit()
connection.close()
"""
## READ
# Connect to the database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Fetch all records from a table
cursor.execute("SELECT * FROM users")
records = cursor.fetchall()

# Print the retrieved data
for record in records:
    print(record)

# Close the connection
connection.close()
"""
# UPDATE

# Connect to the database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Update the email of a specific record in a table
cursor.execute("UPDATE users SET email = ? WHERE id = ?", ("newemail@example.com", 1))

# Commit the transaction and close the connection
connection.commit()
connection.close()

# DELETE

# Connect to the database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Delete a specific record from a table
cursor.execute("DELETE FROM users WHERE id = ?", (1,))

# Commit the transaction and close the connection
connection.commit()
connection.close()
"""