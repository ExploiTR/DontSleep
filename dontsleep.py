import sys
import time
import ctypes
import pystray
import win32gui
import argparse
import pyautogui
import pygetwindow as gw
from PIL import Image, ImageDraw, ImageFont

# Define Windows constants
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002

def prevent_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | ES_SYSTEM_REQUIRED | ES_DISPLAY_REQUIRED)

def restore_sleep():
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

def simulate_mouse():
    print("simulating mouse input")
    while True:
        pyautogui.move(100, 0, duration=0.25)  
        pyautogui.move(0, 100, duration=0.25) 
        pyautogui.move(-100, 0, duration=0.25) 
        pyautogui.move(0, -100, duration=0.25) 
        time.sleep(10) # do this 4s every minute

def exit_action(icon, item):
    print("exit")
    icon.stop()
    restore_sleep()
    sys.exit()

def create_image():
    print("Create tray image")
    # Create a new image with RGB mode, size 64x64 and blue color
    img = Image.new('RGB', (64, 64), color = 'blue')

    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('arial.ttf', 30) # You may need to specify the full path of the font file

    # Draw text in the center
    d.text((10,10), "DS", font=fnt, fill=(255, 255, 255))

    return img

def create_tray_icon():
    # Create an icon image
    image = create_image()
    print("Create tray icon")
    # Create the tray icon
    icon = pystray.Icon("prevent_sleep", image, "Prevent Sleep", menu=pystray.Menu(pystray.MenuItem("Exit", exit_action)))
    icon.run()

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Prevent system sleep.")
    parser.add_argument('-m', '--mouse', action='store_true', help="Use mouse movement to prevent sleep")
    args = parser.parse_args()

    if args.mouse:
        simulate_mouse()
    else:
        prevent_sleep()

    create_tray_icon()

if __name__ == "__main__":
    main()
