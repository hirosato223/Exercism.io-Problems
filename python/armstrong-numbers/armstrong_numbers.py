import math

def is_armstrong_number(number):
    stringInput = str(number)
    numDigits = len(stringInput)
    currTotal = 0
    for digit in stringInput:
        currTotal+= math.pow(int(digit), numDigits)
    return True if currTotal == number else False