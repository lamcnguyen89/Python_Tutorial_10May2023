# Generate a list of coordinates
#for x in range(4):
 #   for y in range(3):
  #      print(f"({x},{y})")

numbers = [5,2,5,2,2]

# Complication of printing out x using nested loops
for item in numbers:
    placeholderString = ""
    for x in range(item):
        placeholderString += "x"
    print(placeholderString)
    placeholderString = ""
        
