#!/usr/bin/env python

# Creating the Dog class
class Dog:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Whoof, whoof!")

# Creating Dog objects
dog1 = Dog("Rex", "German Shepherd")
print(dog1.name, " -> ", dog1.breed)
dog1.bark()

dog2 = Dog("Snoopy", "Beagle")
print(dog2.name, " -> ", dog2.breed)
dog2.bark()


