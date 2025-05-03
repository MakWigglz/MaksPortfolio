import threading

# Create a Lock object
lock = threading.Lock()
shared_counter = 0

def increment():
    global shared_counter
    # Acquire the lock before entering the critical section
    if lock.acquire():
        try:
            print(f"Lock acquired by {threading.current_thread().name}")
            shared_counter += 1  # Critical section
        finally:
            lock.release()  # Ensure the lock is released
            print(f"Lock released by {threading.current_thread().name}")

# Create and start multiple threads
threads = []
for i in range(5):
    t = threading.Thread(target=increment)
    t.start()
    threads.append(t)

# Wait for all threads to complete
for t in threads:
    t.join()

print(f"Final counter value: {shared_counter}")
