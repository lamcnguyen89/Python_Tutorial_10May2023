emojis = {
    "sadface" : ":(",
    "happyface" : ":)"
}

message = input(">")
words = message.split(' ') # Split returns a list of the split objects
output = ""

for word in words:
    char = emojis.get(word, word)
    output += (char + " ")
    
print(output)

