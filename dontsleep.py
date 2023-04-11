import sys
import time
import ctypes
import argparse
import pystray
import pygetwindow as gw
from PIL import Image

# Define Windows constants
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

def prevent_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)

def restore_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

def exit_action(icon, item):
    icon.stop()
    restore_sleep()
    sys.exit()

def create_tray_icon():
    # Load an icon image
    image = Image.open("icon.png")
    # Create the tray icon
    icon = pystray.Icon("prevent_sleep", image, "Prevent Sleep", menu=pystray.Menu(pystray.MenuItem("Exit", exit_action)))
    icon.run()

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Prevent system sleep.")
    parser.add_argument('-v', '--verbose', action='store_true', help="Show CMD output window")
    args = parser.parse_args()

    # Hide the CMD output window if -v flag is not passed
    if not args.verbose:
        cmd_window = gw.getWindowsWithTitle('prevent_sleep.py')[0]
        if cmd_window:
            cmd_window.hide()

    prevent_sleep()
    create_tray_icon()

if __name__ == "__main__":
    main()
