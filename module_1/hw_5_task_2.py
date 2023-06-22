import random
# исла маленькие, и из-за этого сеты одинаковые
list_1 = random.sample(range(1, 11), 10)
list_2 = random.sample(range(1, 11), 10)
print(set(list_1))
print(set(list_2))

print(list(set(list_1) & set(list_2)))
