class Animal:
    def talk(self):
        return "some voice"


class Dog(Animal):
    def talk(self):
        return "The cat say meow meow"


class Cat(Animal):
    def talk(self):
        return "The dog say woof woof"


def performs_talk(animal):
    print(animal.talk())


cat = Cat()
dog = Dog()
performs_talk(cat)
performs_talk(dog)
