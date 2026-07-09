import os
import platform
from datetime import datetime

# Get the system uptime (cross-platform)
if platform.system() == "Windows":
    # Use Windows WMI command to get last boot time
    try:
        import subprocess
        result = subprocess.run(
            'wmic os get lastbootuptime',
            capture_output=True,
            text=True,
            shell=True
        )
        lines = result.stdout.strip().split('\n')
        if len(lines) > 1:
            boot_time_str = lines[1][:14]
            boot_time = datetime.strptime(boot_time_str, "%Y%m%d%H%M%S")
            uptime = datetime.now() - boot_time
            print("System Uptime: " + str(uptime))
        else:
            print("Error: Could not parse uptime from wmic output")
    except Exception as e:
        print(f"Error getting uptime: {e}")
else:
    # Use Unix/Linux command
    try:
        uptime = os.popen('uptime -p').read().strip()
        if uptime:
            print("System Uptime: " + uptime)
        else:
            print("Error: uptime command returned empty result")
    except Exception as e:
        print(f"Error getting uptime: {e}")
