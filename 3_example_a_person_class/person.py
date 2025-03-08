#!/usr/bin/env python

# Create Person class
class Person:
    def __init__(self, name: str, age: int, profession: str):
        self.name = name
        self.age = age
        self.profession = profession

    def greet(self):
        return f"Hi, my name is {self.name}.\n" \
               f"I'm {self.age} years old.\n" \
               f"I'm a{'n' if self.profession[0].lower() in 'aeiou' else ''} {self.profession}.\n"

# Create Person objects
poet1 = Person("Rubén Darío", 49, "Poet")
print(poet1.greet())

actor1 = Person("Pedro Infante", 40, "Actor")
print(actor1.greet())


