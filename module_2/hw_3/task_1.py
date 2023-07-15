class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def talk(self):
        return f"Hello, my name's {self.name} {self.surname} and I’m {self.age} years old"


person = Person("Maxim", "Kostenko", 15)
print(person.talk())
