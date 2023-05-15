# Google "Python Module Index" to see a list of all the different types of modules that python offers
import random

for i in range(3):
    print(random.random())
    print(random.randint(10,20))


# Choose an object from a list randomly:
members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(f'Team Leader: {leader}')


# Write a program to roll 2 sets of dice and display them
# Create a class called Dice which has a method called Roll that outputs a tuple

class Dice:
    def __init__(self, number_of_dice, sides_on_dice):
        self.number_of_dice = number_of_dice
        self.sides_on_dice = sides_on_dice

    def roll(self):
        # Create a Dice
        dice = []
        for i in range(1,(1+self.sides_on_dice)):
            dice.append(i)

        # Roll the Dice:
        dice_roll_outcome = []
        for num_of_rolls in range(self.number_of_dice):
            roll= random.choice(dice)
            dice_roll_outcome.append(roll)
        
        return tuple(dice_roll_outcome)
    
Dice_Set = Dice(number_of_dice= 2, sides_on_dice= 6)

print(Dice_Set.roll())





        