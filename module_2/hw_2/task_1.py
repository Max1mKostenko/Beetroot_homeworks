def logger(func):
    def wrapper(num1, num2):
        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            print(f"You should input only digits! But your first and second numbers are: '{num2}', '{num2}'")
        return func(num1, num2)
    return wrapper


@logger
def _sum(num1, num2):
    return f"Sum of the numbers: {num1} + {num2} = {num1 + num2}"


@logger
def square(num1, num2):
    return f"Square of the numbers:\nNumber {num1}: {num1} ** 2 = {num1 ** 2}\nNumber {num2}: {num2} ** 2 = {num2 ** 2}"


first_num = input("Please enter a first number: ")
second_num = input("Please enter a second number: ")
print(_sum(first_num, second_num))
print(square(first_num, second_num))
