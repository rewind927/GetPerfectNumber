import sys

def isPerfectNumber(number):
    sum = 0
    for element in range(1, number/2+1):
        if number % element == 0:
            sum += element
    return sum == number

number = sys.argv[1]
print("%s is perfect number ? %s" %(number,isPerfectNumber(int(number))))
print("-------------------------------------")
