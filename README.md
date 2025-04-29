# Vulnerability 1: SQL Injection
 
This code is vulnerable to SQL injection because it directly inserts user input into the SQL query.
An attacker could input something like ' OR 1=1 -- to retrieve all users or perform other malicious actions.
 
## Fix:
Use parameterized queries to safely handle user input
```query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (username,))
results = cursor.fetchall()
print(results)
```

Before :

![image](https://github.com/user-attachments/assets/42602f73-c9ce-4f2b-85b3-3f5abb954765)
![image](https://github.com/user-attachments/assets/76e7b7ee-56b2-4e26-b146-9c3922cdfa53)


After :
![image](https://github.com/user-attachments/assets/358b6d2f-72dd-4315-b750-c6819db3a118)


Now, the input is safely passed as a parameter, preventing SQL injection.
 
# Vulnerability 2: Directory Traversal

 ```
import os

try:
    file_path = input("Enter file path: ")
except EOFError:
    print("Error: No input provided for file path.")
    file_path = "default_path.txt"  # Set a default value

with open(file_path, 'r') as file:
    print(file.read())
```
 This code allows the user to specify any file path, which could be outside the intended directory.
 An attacker could input '../secret.txt' to access files outside the web root, potentially exposing sensitive data.
 
## Fix:
Restrict the file path to a specific directory
```base_dir = '/path/to/safe/directory'
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
        print(file.read())
```

Before :

![image](https://github.com/user-attachments/assets/cae4a123-2bfb-4d45-bfa1-e0422b4d29ab)

After :

![image](https://github.com/user-attachments/assets/b53091d8-2e9c-4caa-8ec9-a534a924abcf)

Now, the file path is restricted to the base_dir, preventing directory traversal.
 
# Vulnerability 3: Outdated Libraries
Using outdated libraries can expose your application to known vulnerabilities.
For example, if you are using an old version of a library like Requests (<2.20.0), it may have security flaws that attackers can exploit.
 
## Fix:
Regularly update all libraries and dependencies to their latest versions.
You can use tools like pip to check for updates:
```pip list --outdated```
Then update them with:
```pip install --upgrade <package_name>```

Result:

![image](https://github.com/user-attachments/assets/52450e3c-5911-4ebc-88d5-1f219271bc3e)

 
# Vulnerability 4: Insecure Deserialization
Deserializing untrusted data with pickle can execute arbitrary code.
An attacker could provide a pickled object that, when loaded, executes malicious code via methods like _reduce_.
 
## Fix:
Avoid deserializing untrusted data with `pickle`.
If you must deserialize, use a safe format like JSON.
```import json
 
try:
    data = input("Enter JSON data: ")
except EOFError:
    print("Error: No input provided for JSON data.")
    data = "{}"  # Set a default value
untrusted_data = json.loads(data)
print(untrusted_data)
```
JSON is safer because it doesn't allow arbitrary code execution.
 
# Vulnerability 5: Broken Access Control
 
This code checks if the username exists in the users dictionary but does not enforce proper access controls.
For example, both 'admin' and 'user' can access the same resources, but 'user' should have limited permissions.
 
## Fix:
 
Implement proper access control, e.g., with roles
 
```roles = {
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
```
 Before :
 ![image](https://github.com/user-attachments/assets/8f290aef-967d-407e-9299-6a1600c2a220)

 After :
 ![image](https://github.com/user-attachments/assets/1cd2b74e-fd52-47aa-bbb8-597f83360f2e)


Now, different roles have different levels of access, ensuring proper access control.
