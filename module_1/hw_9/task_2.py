def square_the_param_a_and_divide_it_by_the_param_b(a, b):
    try:
        a = float(a)
    except ValueError:
        return f"Your first number: '{a}', isn't correct. You should enter only digits!"

    try:
        b = float(b)
    except ValueError:
        return f"Your second number: '{b}', isn't correct. You should enter only digits!"

    try:
        return f"Your expression: ({a} ** 2) / {b}, is equal {a ** 2 / b}"
    except ZeroDivisionError:
        return f"Your second number is {b}, so you mustn't divide by zero!"


print(square_the_param_a_and_divide_it_by_the_param_b(input("Please enter the first number: "),
                                                      input("Please enter the second number: ")))
