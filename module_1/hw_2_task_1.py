my_name = "Maxim"
my_day = "Thursday"
_dict = {"name": "Maxim", "day": "Thursday"}
_list = ["Maxim", "Thursday"]

print("Good day {name}! {day} is a perfect day to learn some python.".format(name="Maxim", day="Thursday"))
print("Good day {}! {} is a perfect day to learn some python.".format("Maxim", "Thursday"))
print("Good day {}! {} is a perfect day to learn some python.".format(my_name, my_day))
print("Good day {}! {} is a perfect day to learn some python.".format(_list[0], _list[1]))
print("Good day {name}! {day} is a perfect day to learn some python.".format(**_dict))


print("Good day " + my_name + "! " + my_day + " is a perfect day to learn some python.")  # форматирование но не совсем)


print(f"Good day {my_name}! {my_day} is a perfect day to learn some python.")
print(f"Good day {_list[-2]}! {_list[-1]} is a perfect day to learn some python.")
print(f"Good day {_dict['name']}! {_dict['day']} is a perfect day to learn some python.")


print("Good day %s! %s is a perfect day to learn some python." % (my_name, my_day))
print("Good day %(name)s! %(day)s is a perfect day to learn some python." % _dict)







