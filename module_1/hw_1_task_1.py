import math

# Hello everyone!
print("Hello everyone!\n")

greeting = "My name is {name} {surname} and I'm {age} y.o.\n"

# My name is Maxim Kostenko and I'm 15 y.o.
print(greeting.format(name="Maxim", surname="Kostenko", age=int(math.sqrt(225))))

info = ["Kherson", "Beetroot Academy", "Python"]

# I'm from Kherson. And I joined to Beetroot Academy to repeat the learned and learn more about Python
print(f"I'm from {info[0]}. And I joined to {info[-2]} to repeat the learned and learn more about {info[2]}", end="\n\n")

# 1-2-3-4-5-6-7-8-9
print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep="-")


info = ["Maxim", "Kostenko", 15]
print(f"My name is {info[0]} {info[1]} and I'm {info[2]} y.o.")

