import multiprocessing
import time


def factorize(number):
    return [i for i in range(1, number + 1) if number % i == 0]


def factorize_sync(*numbers):
    return [factorize(num) for num in numbers]


def factorize_parallel(*numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        return pool.map(factorize, numbers)


if __name__ == '__main__':
    # Test the function
    a, b, c, d = 128, 255, 99999, 10651060

    # Assertions
    assert factorize_sync(a, b, c, d) == [
        [1, 2, 4, 8, 16, 32, 64, 128],
        [1, 3, 5, 15, 17, 51, 85, 255],
        [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999],
        [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
         380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    ]

    # Synchronous version
    start_time_sync = time.time()
    result_sync = factorize_sync(a, b, c, d)
    end_time_sync = time.time()
    print(f"Synchronous result: {result_sync}")
    print(f"Synchronous execution time: {end_time_sync - start_time_sync} seconds")

    # Parallel version
    start_time_parallel = time.time()
    result_parallel = factorize_parallel(a, b, c, d)
    end_time_parallel = time.time()
    print(f"Parallel result: {result_parallel}")
    print(f"Parallel execution time: {end_time_parallel - start_time_parallel} seconds")
