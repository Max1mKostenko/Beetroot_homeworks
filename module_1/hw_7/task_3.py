def make_operation(operator, *args):
    if operator == '+':
        result = sum(args)
    elif operator == '-':
        result = args[0] - sum(args[1:])
    elif operator == '*':
        result = 1
        for num in args:
            result *= num
    elif operator == '/':
        result = args[0]
        for num in args[1:]:
            result /= num
    else:
        return f"Operator in function should be (-, +, *, /), but your is: {operator}"

    return result


print(make_operation(input("Please enter the operator(+, -, *, /) to solve the numbers: "), 50, 5, 15, -10))
