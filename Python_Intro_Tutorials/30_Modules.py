# Break up code into different files for better reusability and organization.
#import converters
#from converters import kg_to_lbs

class math_functions:
    def __init__(self, numberArray = []):
        self.numberArr = numberArray

    def find_max(self):
        largest_number = 0
        for i in self.numberArr:
            if i > largest_number:
                largest_number = i
        print(f'Max Number: {largest_number}')


numArray = [1,2,3,4,5,6,7,8,234253]

from utils import find_max

max = find_max(numberArr=numArray)
print(f'Max number: {max}')


