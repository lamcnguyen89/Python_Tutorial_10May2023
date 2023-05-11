#for item in 'Python':
    #print(item) # Prints each character on an individual line

#for item in ["Art", "Heart", "Gun", "Knife"]:
    #print(item) # Prints each item in the array on an individual line

#for x in range(30):
#    print(x) # Prints numbers all the way to 29

#for x in range(5,10,2): # 5 is the beginning of the range, 10 is the end of the range and 2 is the steps 
#    print(x)

prices = [10,20,30]
total = 0
for x in prices:
    total += x
print(f"Total Price: ${total}")
