import threading
import time
import queue

# Shared variables
lines_to_type = [
    "This is the first line.",
    "Try to type this one correctly.",
    "The quick brown fox jumps over the lazy dog."
]

user_input_queue = queue.Queue()
correct_typing_count = 0
total_typing_count = 0
start_time = None

# Function for the thread providing the next line
def provide_next_line():
    global correct_typing_count, total_typing_count, start_time

    for line in lines_to_type:
        start_time = time.time()
        print(f"\nType the following line:\n{line}\n")

        # Sleep for a fixed duration (adjust as needed)
        time.sleep(10)

        # Check user input from the queue
        user_input = user_input_queue.get()
        total_typing_count += len(line.split())
        if line.strip() == user_input.strip():
            correct_typing_count += len(line.split())

    # Signal the end of the test
    user_input_queue.put(None)

# Function for the thread getting input from the user
def get_user_input():
    while True:
        user_input = input()
        if user_input is None:
            break

        # Put user input in the queue
        user_input_queue.put(user_input)

# Create threads
provide_line_thread = threading.Thread(target=provide_next_line)
get_input_thread = threading.Thread(target=get_user_input)

# Start threads
provide_line_thread.start()
get_input_thread.start()

# Wait for the provide_line_thread to finish
provide_line_thread.join()

# Signal the end to the get_input_thread
user_input_queue.put(None)
get_input_thread.join()

# Calculate typing speed and accuracy
end_time = time.time()
elapsed_time = end_time - start_time
typing_speed = total_typing_count / elapsed_time * 60  # words per minute
accuracy = (correct_typing_count / total_typing_count) * 100

print(f"\nTyping Speed: {typing_speed:.2f} words per minute")
print(f"Typing Accuracy: {accuracy:.2f}%")
