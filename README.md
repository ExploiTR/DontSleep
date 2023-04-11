# Prevent System Sleep

This Python script prevents your Windows system from going to sleep while it's running. It's useful when you want to keep your computer awake during long tasks or other activities that don't involve user input.

## Features

- Prevents system sleep while the script is active
- Hides the command prompt window by default, but can be shown with the `-v` flag
- Includes a system tray icon to exit the program

## Requirements

- Python 3.6 or higher
- `pystray` library
- `pygetwindow` library

## Installation

1. Install Python 3.6 or higher from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone this repository or download the `prevent_sleep.py` script and the `icon.png` image.

3. Install the required libraries:

## Installation

1. Install Python 3.6 or higher from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone this repository or download the `prevent_sleep.py` script and the `icon.png` image.

3. Install the required libraries:

    ```bash
    pip install pystray pygetwindow
    ```

## Usage

Run the script using Python:

```bash
python prevent_sleep.py
```
By default, the command prompt window will be hidden. If you want to show the command prompt window, run the script with the -v flag:

```bash
python prevent_sleep.py -v
```

A system tray icon will appear while the script is running. To exit the program and restore the original sleep settings, right-click on the system tray icon and select "Exit".

## License : The Unlicense
