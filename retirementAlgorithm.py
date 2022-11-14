age = int(input("Enter starting age: "))
total = 0
maximumAmount = 20500
catchUp = 6500
inflationLoss=0
number1 = 0
number2 = 0
for number in range(1,60-age):
    if number > 49:
        total = total + maximumAmount+catchUp+(number*500)+(number*500)
    else:
        total = total + maximumAmount+(number*500)
    total = (total*1.08)
    inflationLoss = total*.025
number1=total
print("\n401k total sum, inflation adjusted+IRS contribution adjustment: ",int(round(total-inflationLoss,ndigits=0)))

inflationLoss=0
total = 0
for number in range(1,60-age):
    if number > 49:
        total = total + maximumAmount+catchUp
    else:
        total = total + maximumAmount
    total = (total*1.08)
    inflationLoss = total*.025
print("401k total sum, inflation adjusted: ",int(round(total-inflationLoss,ndigits=0)))

total = 0
for number in range(1,60-age):
    if number > 49:
        total = total + maximumAmount+catchUp
    else:
        total = total + maximumAmount
    total = (total*1.08)
print("401k total sum: ",int(round(total,ndigits=0)))

total = 0
for number in range(1,60-age):
    if number > 49:
        total = total + maximumAmount+catchUp
    else:
        total = total + maximumAmount
print("\nTotal amount contributed to plan: ",int(round(total,ndigits=0)))

total = 0
for number in range(1,60-age):
    if number > 49:
        total = total + maximumAmount+catchUp+(number*500)+(number*500)
    else:
        total = total + maximumAmount+(number*500)
print("Total amount contributed to plan, with IRS contribution adjustment: ",int(round(total,ndigits=0)),"\n")



maximumAmount = 20500*2

inflationLoss=0
total=0
for number in range(1,60-age):
    if number > 49:
        total = total + maximumAmount+catchUp+(number*500)+(number*500)
    else:
        total = total + maximumAmount+(number*500)
    total = (total*1.08)
    inflationLoss = total*.025
number2=total
print("\nEmployer contributions+401k total sum, inflation adjusted+IRS contribution adjustment: ",int(round(total-inflationLoss,ndigits=0)))

inflationLoss=0
total = 0
for number in range(1,60-age):
    if number > 49:
        total = total + maximumAmount+catchUp
    else:
        total = total + maximumAmount
    total = (total*1.08)
    inflationLoss = total*.025
print("Employer contributions+401k total sum, inflation adjusted: ",int(round(total-inflationLoss,ndigits=0)))

inflationLoss=0
total = 0
for number in range(1,60-age):
    if number > 49:
        total = total + maximumAmount+catchUp
    else:
        total = total + maximumAmount
    total = (total*1.08)
print("Employer contributions+401k total sum: ",int(round(total,ndigits=0)))

total = 0
for number in range(1,60-age):
    if number > 49:
        total = total + maximumAmount+catchUp
    else:
        total = total + maximumAmount
print("\nEmployer contributions+Total amount contributed to plan: ",int(round(total,ndigits=0)))

total = 0
for number in range(1,60-age):
    if number > 49:
        total = total + maximumAmount+catchUp+(number*500)+(number*500)
    else:
        total = total + maximumAmount+(number*500)
print("Employer contributions+Total amount contributed to plan, with IRS contribution adjustment: ",int(round(total,ndigits=0)),"\n")

print("with employer double: ",int(number2),"\nno employer double: ",int(number1),"\n")