# Inheritance is where you can create similar classes without having to duplicate code.

class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark():
        print("The Dog barks")


class Cat(Mammal):
    def meow():
        print("The cat meows")


