# Vulnerability 5: Broken Access Control
# Vulnerable code
users = {
    'admin': 'admin_password',
    'user': 'user_password'
}

try:
    username = input("Enter username: ")
except EOFError:
    print("Error: No input provided for username.")
    username = "default_user"  # Set a default value
if username in users:
    print("Access granted")
else:
    print("Access denied")

# Explanation:
# This code checks if the username exists in the users dictionary but does not enforce proper access controls.
# For example, both 'admin' and 'user' can access the same resources, but 'user' should have limited permissions.

# Fix:
# Implement proper access control, e.g., with roles
roles = {
    'admin': 'admin',
    'user': 'user'
}

try:
    username = input("Enter username: ")
except EOFError:
    print("Error: No input provided for username.")
    username = "default_user"  # Set a default value
if username in roles and roles[username] == 'admin':
    print("Admin access granted")
elif username in roles and roles[username] == 'user':
    print("User access granted")
else:
    print("Access denied")

# Now, different roles have different levels of access, ensuring proper access control.