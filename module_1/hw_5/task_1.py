import random
"""
First variant
"""
num = random.randint(10, 100)
_list = random.sample(range(0, num), 10)
print(_list)
print(max(_list))

# one str
print(max(random.sample(range(0, random.randint(10, 100)), 10)))

"""
Second variant
"""
# _list_2 = [random.randint(0, random.randint(10, 100)) for i in range(10)]
# print(_list_2)
# print(max(_list_2))
