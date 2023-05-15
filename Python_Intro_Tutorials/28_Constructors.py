# Constructors are like predetermined templates that require a class to have certain parameters
class Point_with_Constructors:
    def __init__(self, x, y): # Self is a reference to the current object in memory
        self.x = x
        self.y = y
        

    def move(self):
        print("move")
    
    def draw(self):
        print("draw")



point = Point_with_Constructors(x=10,y=20)
print(f'{point.x}, {point.y}')

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
    def talk (self):
        print(f'Hello. My name is {self.name}, a {self.gender}. I like you.')

Person1 = Person(name="Lam Nguyen", gender="male")
Person1.talk()

