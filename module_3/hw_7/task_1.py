import asyncio


def fibonacci(num):
    if num < 1:
        return 0
    elif num == 1:
        return 1

    fib_prev = 0
    fib_curr = 1
    for _ in range(2, num + 1):
        fib_prev, fib_curr = fib_curr, fib_prev + fib_curr

    return fib_curr


def factorial(var):
    factorial_ = 1
    for i in range(1, var + 1):
        factorial_ *= i
    return factorial_


def squares(sqr_num):
    return sqr_num ** 2


def cubic(cubic_num):
    return cubic_num ** 3

