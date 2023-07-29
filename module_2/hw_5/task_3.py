class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"MyClass(x={self.x}, y={self.y})"

    def __repr__(self):
        return f"MyClass({self.x}, {self.y})"


obj = MyClass(10, 20)

print(type(str(obj)))
print(type(repr(obj)))
