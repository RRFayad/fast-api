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
