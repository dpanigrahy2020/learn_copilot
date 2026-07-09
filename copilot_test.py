import os
import platform
from datetime import datetime, timedelta

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
        boot_time_str = result.stdout.strip().split('\n')[1][:14]
        boot_time = datetime.strptime(boot_time_str, "%Y%m%d%H%M%S")
        uptime = datetime.now() - boot_time
        print("System Uptime: " + str(uptime))
    except Exception as e:
        print(f"Error getting uptime: {e}")
else:
    # Use Unix/Linux command
    uptime = os.popen('uptime -p').read().strip()
    print("System Uptime: " + uptime)
