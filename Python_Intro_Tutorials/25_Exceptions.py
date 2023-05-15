try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except(ValueError):
    print("Invalid Value. Type Float or Integer")
except(ZeroDivisionError):
    print("Invalid Value. Age cannot be zero. Try Again")

# Progress 2:55:51