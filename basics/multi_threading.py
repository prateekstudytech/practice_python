import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        # lock.acquire()
        counter += 1
        # lock.release()
        print(counter)
        

# Create threads
first_thread = threading.Thread(target=increment)
second_thread = threading.Thread(target=increment)

first_thread.start()
second_thread.start()

first_thread.join()
second_thread.join()
