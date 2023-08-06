class Calculator:
    def __init__(self, num_1: int or float, num_2: int or float):
        self.num_1 = num_1
        self.num_2 = num_2

    def addition(self):
        return f"Your answer is: {self.num_1 + self.num_2}"

    def subtraction(self):
        return f"Your answer is: {self.num_1 - self.num_2}"

    def multiplication(self):
        return f"Your answer is: {self.num_1 * self.num_2}"

    def exponentiation(self):
        return f"Your answer is: {self.num_1 ** self.num_2}"

    def division(self):
        try:
            return f"Your answer is: {self.num_1 / self.num_2}"
        except ZeroDivisionError:
            return "You can't divide by zero!"

    def floor_division(self):
        try:
            return f"Your answer is: {self.num_1 // self.num_2}"
        except ZeroDivisionError:
            return "You can't divide by zero!"

    def modulus(self):
        try:
            return f"Your answer is: {self.num_1 % self.num_2}"
        except ZeroDivisionError:
            return "You can't divide by zero!"


calculator = Calculator(50, 2)

print(calculator.addition())

print(calculator.subtraction())

print(calculator.multiplication())

print(calculator.exponentiation())

print(calculator.division())

print(calculator.floor_division())

print(calculator.modulus())
