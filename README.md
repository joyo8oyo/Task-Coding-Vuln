# Vulnerability 2: Directory Traversal
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
