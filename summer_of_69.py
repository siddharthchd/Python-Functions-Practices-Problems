def summer_of_69(arr):
    """
    This function returns the sum of the numbers in the array, except ignoring the sections of numbers starting
    with a 6 and extending to the next 9 (every 6 followed by at least one 9).
    """
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
                break
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_of_69([2, 1, 6, 9, 11]))