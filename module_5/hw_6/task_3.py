import random
import timeit


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def quicksort(arr, partition_limit=10):
    if len(arr) <= partition_limit:
        insertion_sort(arr)
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        arr = quicksort(left) + middle + quicksort(right)
    return arr


random.seed(42)
data = [random.randint(1, 1000) for _ in range(1000)]

partition_limits = [5, 10, 20, 50, 100]

for limit in partition_limits:
    setup_code = f"from __main__ import quicksort, insertion_sort, data; data_copy = data.copy()"
    sort_code = f"quicksort(data_copy, partition_limit={limit})"
    execution_time = timeit.timeit(sort_code, setup=setup_code, number=1000)
    print(f"Partition Limit: {limit}, Execution Time: {execution_time:.6f} seconds")
