#!/usr/bin/env python

# Creating Owner class
class Owner:
    def __init__(self, name: str, address: str, contact_number: str, hasDog: bool = False):
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.hasDog = hasDog

    #isDogOwner = self.hasDog

# Creating Owner objects
kommissar = Owner("Richie", "Vienna, Austria", "+43 123-456-7890", True)
cartoon = Owner("Charlie", "Minnesota, U. S.", "+1 123-456-7890", True)

print(f"Does {kommissar.name} have a dog?", kommissar.hasDog)
print(f"Does {cartoon.name} have a dog?", cartoon.hasDog)

# Creating the Dog class
class Dog:
    def __init__(self, name: str, breed: str, owner: Owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof, whoof!")

# Creating Dog objects
dog1 = Dog("Rex", "German Shepherd", kommissar)
print(dog1.name, " -> ", dog1.breed)
print(f"{dog1.name}'s owner: {dog1.owner.name}")
dog1.bark()

dog2 = Dog("Snoopy", "Beagle", cartoon)
print(dog2.name, " -> ", dog2.breed)
print(f"{dog2.name}'s owner: {dog2.owner.name}")
dog2.bark()


