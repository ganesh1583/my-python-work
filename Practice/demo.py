import time
import pyautogui

# Give some time to switch to the messaging app
time.sleep(5)

# Message to send
message = "U+1F595"

# Number of times to send the message
num_messages = 5

# Loop to send the message multiple times
for _ in range(num_messages):
    # Type the message and press Enter
    pyautogui.typewrite(message)
    pyautogui.press('enter')

    # Add a delay between messages (adjust as needed)
    time.sleep(1)
