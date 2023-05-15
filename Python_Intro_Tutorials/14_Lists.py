names = ['John', 'Bob', 'Mosh', 'Sarah', "Melanie"]

# Indexes:
print(names[0]) # Prints John
print(names[-2]) # Prints Sarah
print(names[1:2]) # Prints Bob and leaves out Mosh

# Change Item in List
names[0] = "Lam"

# Write a program to find largest number in a list:

numbers = []
largestNumber = 0

# Generate the List
for x in range(80):
    numbers.append(x)

# Loop through the list to find the largest number:
for i in numbers:
    if i > largestNumber:
        largestNumber = i
print(largestNumber)
