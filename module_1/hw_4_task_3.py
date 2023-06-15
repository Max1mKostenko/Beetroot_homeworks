import random
_list = list(input("Please enter any word: "))
for i in range(5):
    random.shuffle(_list)
    print("".join(_list))
