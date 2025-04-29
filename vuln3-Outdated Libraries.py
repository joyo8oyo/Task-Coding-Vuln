# Vulnerability 3: Outdated Libraries
# Explanation:
# Using outdated libraries can expose your application to known vulnerabilities.
# For example, if you are using an old version of a library like Requests (<2.20.0), it may have security flaws that attackers can exploit.

# Fix:
# Regularly update all libraries and dependencies to their latest versions.
# You can use tools like pip to check for updates:
# pip list --outdated
# Then update them with:
# pip install --upgrade <package_name>
