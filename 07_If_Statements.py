
is_hot = False
is_cold = True

warning = 'Drink some water bitch'
encourage = 'Have some fun!'
warning2 = 'Wear a jacket'

if is_hot:
    print(warning)
elif is_cold:
    print(warning2)
else:
    print(encourage)

print("Enjoy your day")


# Write a program where the price of a house is 1 million. If a buyer has good credit, he puts down 10%. If bad credit, he puts down 20%
#Then print how much money the buyer has to put down

housePrice = 1000000.00
goodCredit = False

if goodCredit:
    downpayment = housePrice * .1
    print(f"Downpayment: ${downpayment}")
else:
    downpayment = housePrice *.2
    print(f"Downpayment: ${downpayment}")

