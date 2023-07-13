from random import choice


def choose_func(nums: list, func1, func2):
    positive_nums = [num for num in nums if num > 0]
    if len(positive_nums) == len(nums):
        return func1(nums)
    else:
        return func2(nums)


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


c = choice([[1, 2, 4], [0, 1, -3, 2, 4]])
print(f"random list: {c}")
print(choose_func(c, square_nums, remove_negatives))

