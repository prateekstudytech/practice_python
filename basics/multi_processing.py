import multiprocessing

def print_even():
    for num in range(1, 100):
        if num % 2 == 0:
            print(f"Even: {num}")

def print_odd():
    for num in range(1, 100):
        if num % 2 != 0:
            print(f"Odd: {num}")

if __name__ == "__main__":
    # Create process objects
    p1 = multiprocessing.Process(target=print_even)
    p2 = multiprocessing.Process(target=print_odd)

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()
