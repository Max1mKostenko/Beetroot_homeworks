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


print(recursive_binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 7, 1, 11))
