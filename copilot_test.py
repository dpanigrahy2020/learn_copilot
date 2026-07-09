import psutil
from datetime import timedelta

# Get the system uptime
boot_time = psutil.boot_time()
uptime_seconds = psutil.time.time() - boot_time
uptime = timedelta(seconds=int(uptime_seconds))

# Print the system uptime
print("System Uptime: " + str(uptime))
