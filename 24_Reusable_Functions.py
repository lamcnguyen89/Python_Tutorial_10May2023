def emoji_greeting(message):
    emojis = {
    "sadface" : ":(",
    "happyface" : ":)"
}
    words = message.split(' ') # Spl
    output = ""

    for word in words:
        char = emojis.get(word, word)
        output += (char + " ")

    return output


message = emoji_greeting(message="I am happy! happyface")
print(message)