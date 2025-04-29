# Vulnerability 2: Directory Traversal
import os

# Define the base directory (ensure raw string to handle backslashes on Windows)
base_dir = r'C:\Users\kanjeng\Downloads'

try:
    file_name = input("Enter file name: ").strip()
except EOFError:
    print("Error: No input provided for file name.")
    file_name = "default_file.txt"  # Set a default value

# Construct the full file path
full_path = os.path.abspath(os.path.join(base_dir, file_name))

# Normalize base_dir to absolute path
base_dir_abs = os.path.abspath(base_dir)

# Check if the full_path starts with the base_dir to prevent traversal
if not full_path.startswith(base_dir_abs + os.path.sep):
    print("Invalid path: Access denied.")
else:
    try:
        with open(full_path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Now, the file path is restricted to the base_dir, preventing directory traversal.
