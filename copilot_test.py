import os
import platform

# Get the system uptime (cross-platform)
if platform.system() == "Windows":
    # Use Windows command
    uptime = os.popen('wmic os get lastbootuptime').read()
    print("System Uptime (raw): " + uptime)
else:
    # Use Unix/Linux command
    uptime = os.popen('uptime -p').read()
    print("System Uptime: " + uptime)
