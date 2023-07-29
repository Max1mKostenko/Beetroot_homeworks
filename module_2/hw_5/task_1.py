class Animal:
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        return "The cat say meow meow"


class Cat(Animal):
    def talk(self):
        return "The dog say woof woof"


def perform_talk(animal):
    print(animal.talk())


dog, cat = Dog(), Cat()

perform_talk(dog)
perform_talk(cat)
