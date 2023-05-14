numbers = [5,4,2,1,7,5]
numbers.append(20)
print(numbers)
numbers.insert(0,34)
print(numbers)
numbers.pop()
print(numbers)
# print(numbers.index(0))
print(numbers.count(5))
print(numbers.sort())
print(numbers.reverse())
numbers2 = numbers.copy() # Copy items 

# App to remove duplicate elements on a list
List01 = [0,1,1,2,3,4,5,5,6,7,8,8,9,9,10]
SortedList = []

for i in List01:
    if i not in SortedList:
        SortedList.append(i)
    


print(SortedList)