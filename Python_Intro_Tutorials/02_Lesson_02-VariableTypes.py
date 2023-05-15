birth_year = int(input('Birth Year: '))
age = 2023 - birth_year
print('Current Age: ', str(age))
print(type(birth_year)) # Displays the Class or type
print(type(age))

int() # Converts type to integer
bool() # Converts type to boolean
str() # Converts type to string
float() # Converts type to float

# App to ask the user their weight in lbs and coverts it to kilograms and prints on the terminal:

pounds = float(input('How much do you weigh in pounds? '))
kilograms = pounds/2.21

print('You weigh ' + str(round(kilograms, 2)) + ' Kg')


# Strings:

course = "Python's Course for Beginners"
course02 = 'Python for "Beginners"'

# Multiline strings:
course03 = ''' 
    Hi Tina,
    
    I love you even if you don't love me back
    Bye,
    Lam
'''

# Get a certain letter from a string. A string is stored in an array:
print(course[0]) # Prints P
print(course[-2]) # Prints R

print(course[0:3]) # Prints Pyt but excludes the letter in index 3
print(course[0:]) # Prints to the end from the beginning
print(course[:5]) # Assumes zero as the start index

another = course[:] # Allows you to clone a variable without linking together





