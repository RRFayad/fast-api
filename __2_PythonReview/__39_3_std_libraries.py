import math
import random

types_of_drinks = ["soda", "coffee", "water", "tea"]
print(random.choice(types_of_drinks))

print("Random int from 1 to 10:", random.randint(1, 10))

square_root = math.sqrt(64)  # 8


class Person():
    def __init__(self, age=20, name="John"):
        self.age = age
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}, {self.age} years old")


p1 = Person(30, "Alice")
p1.talk()


class Man(Person):
    def __init__(self, age=20, name="John", beard_length=0):
        super().__init__(age, name)
        self.beard_length = beard_length

    def shout(self):
        print("I am a man!")

    def grow_beard(self):
        self.beard_length += 1


renan = Man(25, "Renan", 5)
print(renan.name)  # Renan
renan.shout()

# Composition


class Engine():
    def start(self):
        print("Engine started")


class Motorcycle():
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Motorcycle started")


harley = Motorcycle()
harley.start()
