import asyncio


async def calculate_fibonacci(n):
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


async def calculate_factorial(n):
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


async def calculate_squares(n):
    return [i ** 2 for i in range(1, n + 1)]


async def calculate_cubes(n):
    return [i ** 3 for i in range(1, n + 1)]


async def main():
    tasks = [calculate_fibonacci(10), calculate_factorial(10), calculate_squares(10), calculate_cubes(10)]
    results = await asyncio.gather(*tasks)

    fibonacci_result, factorial_result, squares_result, cubes_result = results

    print("Fibonacci:", fibonacci_result)
    print("Factorial:", factorial_result)
    print("Squares:", squares_result)
    print("Cubes:", cubes_result)


if __name__ == "__main__":
    asyncio.run(main())
