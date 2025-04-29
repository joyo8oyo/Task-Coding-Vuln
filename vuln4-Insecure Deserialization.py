# Vulnerability 4: Insecure Deserialization
# Vulnerable code
import pickle
import os

class Evil:
    def __reduce__(self):
        return (os.system, ("echo HACKED > C:\\Windows\\Temp\\pwned.txt",))

malicious = pickle.dumps(Evil())
print(repr(malicious))
# Explanation:
# Deserializing untrusted data with pickle can execute arbitrary code.
# An attacker could provide a pickled object that, when loaded, executes malicious code via methods like __reduce__.

# Fix:
# Avoid deserializing untrusted data with pickle.
# If you must deserialize, use a safe format like JSON.
import pickle
import ast  # <-- add this line

try:
    data = input("Enter pickled data: ")
except EOFError:
    print("Error: No input provided for pickled data.")
    data = ""  # Set a default value
data = ast.literal_eval(data)  # <-- add this line
untrusted_data = pickle.loads(data)
print(untrusted_data)


# JSON is safer because it doesn't allow arbitrary code execution.
