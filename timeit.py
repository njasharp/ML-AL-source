import time

def while_loop(n=100_000_000):
    s = 0
    i = 0
    while i < n:
        s += 1
        i += 1
    return s

def for_loop(n=100_000_000):
    s = 0
    for i in range(n):
        s += 1
    return s

def main():
    n = 100_000_000
    print(f"Summing numbers from 0 to {n-1} using while loop:")
    start_time = time.time()  # Use time.time() instead of timeit.default_timer()
    result = while_loop(n)
    end_time = time.time()
    print(f"Result: {result}")
    print(f"Elapsed time: {end_time - start_time:.6f} seconds")

    print("\nSumming numbers from 0 to {n-1} using for loop:")
    start_time = time.time()
    result = for_loop(n)
    end_time = time.time()
    print(f"Result: {result}")
    print(f"Elapsed time: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()