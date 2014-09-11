

def isPerfectNumber(number):
    sum = 0
    for element in range(1,number):
        if number % element == 0:
            sum += element
    return sum == number


while True:
    number = raw_input("Input number: ")
    if number.isdigit(): 
        print("%s is perfect number ? %s" %(number,isPerfectNumber(int(number))))
        print("-------------------------------------")
    else:
        print("not digital number, break this loop!")
        break 
