i = 1

while i <= 5:
    print('*' * i)
    i+=1
print("done")


# Secret Number Game:

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess a number"))
    guess_count += 1
    if guess == secret_number:
        print(f"You've guessed the correct number {secret_number}!")
        break
else:
    print("You've Failed....")
