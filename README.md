# Vulnerability 1: SQL Injection
Description: SQL injection occurs when user input is directly incorporated into an SQL query, allowing attackers to manipulate the query. For example, an attacker could input ' OR 1=1 -- to bypass authentication or extract all data from a database.

Risk: This can lead to unauthorized data access, data modification, or even complete database compromise.

Example in Script:

Vulnerable Code: The script uses an f-string to build an SQL query: query = f"SELECT * FROM users WHERE username = '{username}'". This allows malicious input to alter the query’s logic.
Fix: The fixed version uses a parameterized query: query = "SELECT * FROM users WHERE username = ?", with the input passed as a parameter: cursor.execute(query, (username,)). This ensures the input is treated as data, not executable code.
Mitigation: Always use parameterized queries or prepared statements when interacting with databases. Libraries like sqlite3 and ORM frameworks (e.g., SQLAlchemy) provide built-in support for this.


# Vulnerability 2: Directory Traversal
Vulnerability 2: Directory Traversal
Description: Directory traversal vulnerabilities arise when an application allows user input to specify file paths without proper validation. Attackers can use inputs like ../secret.txt to access files outside the intended directory.

Risk: This can expose sensitive files, such as configuration files or user data, and in some cases, enable remote code execution.

Example in Script:

Vulnerable Code: The script opens a file based on user input: with open(file_path, 'r') as file. This allows access to any readable file on the system.
Fix: The fixed version restricts file access to a specific directory: full_path = os.path.join(base_dir, file_path), and checks if the resolved path stays within the base directory: if not os.path.abspath(full_path).startswith(base_dir).
Mitigation: Validate and sanitize file paths using os.path functions like os.path.join and os.path.abspath. Ensure the resolved path is within a designated safe directory.

Explanation:
This code allows the user to specify any file path, which could be outside the intended directory.
An attacker could input '../secret.txt' to access files outside the web root, potentially exposing sensitive data.

Fix:
Restrict the file path to a specific directory

```base_dir = r'C:\Users\kanjeng\Downloads'

try:
    file_path = input("Enter file name: ")
except EOFError:
    print("Error: No input provided for file name.")
    file_path = "default_file.txt"  # Set a default value
full_path = os.path.join(base_dir, file_path)
if not os.path.abspath(full_path).startswith(base_dir):
    print("Invalid path")
else:
    with open(full_path, 'r') as file:
        print(file.read())`
```
Now, the file path is restricted to the base_dir, preventing directory traversal.

# Vulnerability 3: Outdated Libraries
Description: Using outdated libraries can expose applications to known vulnerabilities. For instance, the requests library before version 2.20.0 had a flaw where HTTP Authorization headers were sent to HTTP URIs upon redirects, risking credential exposure (CVE-2018-18074).

Risk: Attackers can exploit known vulnerabilities in outdated libraries to gain unauthorized access or execute malicious code.

Example in Script:

Vulnerable Code: The script doesn’t include code for this, as it’s an environmental issue, but it explains the risk of using outdated libraries.
Fix: The script recommends checking for outdated packages with pip list --outdated and updating them with pip install --upgrade <package_name>.
Mitigation: Regularly update dependencies using tools like pip. Consider using dependency management tools like poetry or pipenv, and monitor vulnerability databases like PyUp.io.

# Vulnerability 4: Insecure Deserialization
Description: Deserializing untrusted data with Python’s pickle module can execute arbitrary code. Attackers can craft malicious pickled objects that invoke harmful methods via __reduce__.

Risk: This can lead to remote code execution, allowing attackers to run arbitrary commands on the system.

Example in Script:

Vulnerable Code: The script deserializes user input with pickle.loads(data), which could execute malicious code.
Fix: The fixed version uses json.loads(data) for deserialization, as JSON does not support executable code.
Mitigation: Avoid deserializing untrusted data with pickle. Use safe formats like JSON or YAML with yaml.safe_load. If pickle is necessary, ensure the data source is trusted.

# Vulnerability 5: Broken Access Control
Description: Broken access control occurs when an application fails to enforce proper permissions, allowing users to access resources they shouldn’t. For example, a user might access admin features by simply providing a valid username.

Risk: This can lead to unauthorized access to sensitive data or functionality, compromising the application’s security.

Example in Script:

Vulnerable Code: The script grants access if the username exists in a dictionary: if username in users, without checking roles.
Fix: The fixed version uses a role-based system: if username in roles and roles[username] == 'admin', ensuring only authorized users access specific features.
Mitigation: Implement role-based access control (RBAC) or object-level permissions. Use frameworks like Flask-Login or Django’s authentication system for robust access control.
