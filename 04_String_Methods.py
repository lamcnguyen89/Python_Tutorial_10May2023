course = 'Python for Beginners'
print(len(course)) # Prints Length of String

# This inbuilt function len() allows you to limit the size of a string. It is a general purpose function

# String Method example. Methods are specific to a certain thing.
print(course.upper())
print(course.capitalize())
print(course.lower())

print(course.find('P')) # Lets you find the index of the first occurence of the character specified
print(course.find('O')) # Returns -1 for not found
print(course.replace('Beginners', 'Absolute Beginners')) # Replace

# Checks to see if something is in a variable. Returns a boolean. It's case sensitive
print('Python' in course)