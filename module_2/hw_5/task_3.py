class Fraction:
    def __init__(self, num_1, num_2):
        self.num_1, self.num_2 = num_1, num_2

    def __add__(self, other):
        return f"{self.num_1} + {other.num_2} = {int(self.num_1) + int(other.num_2)}"

    def __sub__(self, other):
        return f"{self.num_1} - {other.num_2} = {int(self.num_1) - int(other.num_2)}"

    def __mul__(self, other):
        return f"{self.num_1} * {other.num_2} = {int(self.num_1) * int(other.num_2)}"

    def __truediv__(self, other):
        if other.num_2 == 0:
            raise ValueError("Division by zero isn't allowed.")
        return f"{self.num_1} / {other.num_2} = {int(self.num_1) / int(other.num_2)}"


if __name__ == "__main__":
    fraction = Fraction(50, 2)
    print(fraction + fraction)
    print(fraction - fraction)
    print(fraction * fraction)
    print(fraction / fraction)
