class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age

    def human_age(self):
        return f"The dog's age {self.age} in human equivalent is equal around: {Dog.age_factor * self.age}"


dog = Dog(5)
print(dog.human_age())
