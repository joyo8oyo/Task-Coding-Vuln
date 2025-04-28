# Vulnerability 1: SQL Injection
# Vulnerable code
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
try:
    username = input("Enter username: ")
except EOFError:
    print("Error: No input provided for username.")
    username = "default_user"  # Set a default value
query = f"SELECT * FROM users WHERE username = '{username}'"
cursor.execute(query)
results = cursor.fetchall()
print(results)

# Explanation:
# This code is vulnerable to SQL injection because it directly inserts user input into the SQL query.
# An attacker could input something like ' OR 1=1 -- to retrieve all users or perform other malicious actions.

# Fix:
# Use parameterized queries to safely handle user input
##query = "SELECT * FROM users WHERE username = ?"
##cursor.execute(query, (username,))
##results = cursor.fetchall()
##print(results)

# Now, the input is safely passed as a parameter, preventing SQL injection.