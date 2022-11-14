maximum = int(input("Enter an upper bound for a check: "))
print("Between 1 and", maximum, "there are")

number = 1
proper = 1
propersum = 0
# will be modified and used to determine the numbers

deficient = 0
perfect = 0
abundant = 0

while number <= maximum :
    while proper < number:
        if number % proper == 0:
            propersum += proper 
        # finds a proper divisor and adds to a sum
        proper += 1
        # system for getting the sum of proper divisors

    if propersum == number :
        perfect += 1
# tests if the number is perfect

    elif propersum < number :
        deficient += 1
# tests if the number is deficient

    elif propersum > number :
        abundant += 1
# tests if the number is abundant
    proper = 1
    propersum = 0
    number += 1
# resets proper and propersum for the next numbers, and goes up one number

print(deficient,"deficient numbers")
print(perfect,"perfect numbers")
print(abundant,"abundant numbers")