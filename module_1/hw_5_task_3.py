num_list = [i for i in range(1, 101)]
print(num_list)
new_list = [i for i in num_list if i % 7 == 0 and i % 5 != 0]
print(new_list)
