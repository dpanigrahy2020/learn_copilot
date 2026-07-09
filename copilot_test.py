#!/usr/bin/env python3
"""
Script to display system uptime in a human-readable format.
Works on Linux, macOS, and Windows.
"""

import platform
import subprocess
import re
from datetime import timedelta


def get_uptime_linux():
    """Get uptime on Linux systems."""
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            return uptime_seconds
    except FileNotFoundError:
        return None


def get_uptime_macos():
    """Get uptime on macOS systems."""
    try:
        result = subprocess.run(['uptime'], capture_output=True, text=True)
        # uptime output: "10:30  up 5 days, 3:45, 2 users, load average: 1.23, 0.98, 0.87"
        uptime_output = result.stdout.strip()
        return uptime_output
    except Exception:
        return None


def get_uptime_windows():
    """Get uptime on Windows systems."""
    try:
        result = subprocess.run(
            ['wmic', 'os', 'get', 'lastbootuptime'],
            capture_output=True,
            text=True
        )
        # Parse the output to calculate uptime
        boot_time = result.stdout.split('\n')[1].split('.')[0]
        from datetime import datetime
        boot_dt = datetime.strptime(boot_time, '%Y%m%d%H%M%S')
        uptime = datetime.now() - boot_dt
        return str(uptime)
    except Exception:
        return None


def format_uptime(seconds):
    """Convert seconds to a human-readable uptime format."""
    td = timedelta(seconds=seconds)
    days = td.days
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    parts = []
    if days > 0:
        parts.append(f"{days} day{'s' if days > 1 else ''}")
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours > 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
    if seconds > 0 or not parts:
        parts.append(f"{seconds} second{'s' if seconds > 1 else ''}")
    
    return ", ".join(parts)


def print_system_uptime():
    """Print the system uptime in a human-readable format."""
    system = platform.system()
    
    print("=" * 50)
    print("System Uptime Information")
    print("=" * 50)
    print(f"Operating System: {system}")
    print()
    
    uptime = None
    
    if system == "Linux":
        uptime = get_uptime_linux()
        if uptime:
            formatted_uptime = format_uptime(uptime)
            print(f"Uptime: {formatted_uptime}")
        else:
            print("Could not retrieve uptime information.")
    
    elif system == "Darwin":  # macOS
        uptime = get_uptime_macos()
        if uptime:
            print(f"Uptime: {uptime}")
        else:
            print("Could not retrieve uptime information.")
    
    elif system == "Windows":
        uptime = get_uptime_windows()
        if uptime:
            print(f"Uptime: {uptime}")
        else:
            print("Could not retrieve uptime information.")
    
    else:
        print(f"Unsupported operating system: {system}")
    
    print("=" * 50)


if __name__ == "__main__":
    print_system_uptime()
