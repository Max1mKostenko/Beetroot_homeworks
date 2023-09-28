import multiprocessing
import time


def calculate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib


def calculate_factorial(n):
    if n < 0:
        return []
    elif n == 0:
        return [1]

    factorial = 1
    factorial_list = []
    for i in range(1, n + 1):
        factorial *= i
        factorial_list.append(factorial)
    return factorial_list


def calculate_squares(n):
    return [i ** 2 for i in range(1, n + 1)]


def calculate_cubes(n):
    return [i ** 3 for i in range(1, n + 1)]


def main():
    start_time = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(lambda func: func(10),
                           [calculate_fibonacci, calculate_factorial, calculate_squares, calculate_cubes])

    fibonacci_result, factorial_result, squares_result, cubes_result = results

    print("Fibonacci:", fibonacci_result)
    print("Factorial:", factorial_result)
    print("Squares:", squares_result)
    print("Cubes:", cubes_result)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution Time: {execution_time} seconds")


if __name__ == "__main__":
    main()
