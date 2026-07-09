import os

# Get the system uptime
uptime = os.popen('uptime -p').read()

# Print the system uptime
print("System Uptime: " + uptime)
