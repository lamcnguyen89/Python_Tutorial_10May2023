customer = {"Name": "Lam Nguyen",
            "Age" : 30,
            "Is_verified" : True
            }

# For a dictionary each key should be unique, but the value can be anything.

# To access Dictionary:
print(customer["Name"]) # Case Sensitive
print(customer.get("birthdate", "Jan1989")) # The get function is good because it won't crash if no key is found
customer["name"] = "Jack Smith" # For updating a value for a key
customer["birthyear"] = 1989

print(customer)

# Write a program where you enter numbers and it outputs the word for a number:

numberDictionary = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

phoneInput = input("Enter your phone number:")
output = ""

for digit in phoneInput:
    output += ((numberDictionary.get(digit,"Character Not Found") + " "))

print(output)