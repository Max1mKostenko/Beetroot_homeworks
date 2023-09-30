def recursive_binary_search(arr, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, end)
    else:
        return recursive_binary_search(arr, target, start, mid - 1)


def fibonacci_search(arr, target):
    def generate_fibonacci_numbers(n):
        fibonacci = [0, 1]
        while fibonacci[-1] < n:
            next_fib = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(next_fib)
        return fibonacci

    n = len(arr)
    fibonacci_numbers = generate_fibonacci_numbers(n)

    offset = 0
    while fibonacci_numbers[-2] > 1:
        i = min(offset + fibonacci_numbers[-2] - 1, n - 1)
        if arr[i] < target:
            offset = i
            fibonacci_numbers = fibonacci_numbers[:-2]
        elif arr[i] > target:
            fibonacci_numbers = fibonacci_numbers[:-1]
        else:
            return i

    if arr[offset] == target:
        return offset
    return -1


print(fibonacci_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 7))
print(recursive_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 7, 1, 11))
