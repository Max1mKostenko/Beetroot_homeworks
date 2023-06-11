_str = "#" * 9
string_with_space = "#" + " " * 7 + "#"

"""
#########
#       #
#       #
#       #
#########
"""
print(f"{_str}\n" + f"{string_with_space}\n" * 3 + _str, end="\n" * 2)


"""
#       #
#       #
#########
#       #
#       #
"""
print(f"{string_with_space}\n" * 2 + f"{_str}\n" + f"{string_with_space}\n" * 2)

print("sfsdf")