# print factorial value of a number
number = int(input("Please enter a number to calculate factorial: "))

def factorial_calculation(number_to_use):
    result = 1
    for x in range(number_to_use, 0, -1):
        result = result * x
    return result


print(factorial_calculation(number))
