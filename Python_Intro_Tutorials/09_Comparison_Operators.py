temp = 35

if temp > 30:
    print("It's a hot day")
else:
    print("It's nice outside")


# Logical Operators:
    # ==
    # >=
    # <=
    # >
    # <
    # !=

# Name Application:

def enterName():
    name = input("Enter a name: ")

    if len(name) < 3:
        print("Name must be at least 3 characters long")
        enterName()
    elif len(name) > 50:
        print("Name must be less then 50 characters long")
        enterName()
    else:
        print("Name looks good!") 

enterName()

# Weight Conversion Application:

def WeightConversion():

    try:
        weight = float(input("What is your weight? "))
    except ValueError:
        print("That is not a valid number. Try Again")
        WeightConversion()

    def enterUnits():
        unit = input("Enter L for lbs unit or K for Kilograms for the units you are inputting into converter: ").capitalize()

        if unit == "L":
            weightInKilograms = float(weight) / 2.21
            print(f"You weigh {round(weightInKilograms,2)} Kg")
        elif unit == "K":
            weightInPounds = float(weight) * 2.21
            print(f"You weight {round(weightInPounds,2)} lbs")
        else:
            print("Invalid Input")
            enterUnits()

WeightConversion()





        
  