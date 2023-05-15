def find_max(numberArr=[]):
    largest_number = 0
    for i in numberArr:
        if i > largest_number:
            largest_number = i
    return largest_number