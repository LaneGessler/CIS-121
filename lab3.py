earnedIncome = float(input("Enter the amount of income you earned in 2021: "))
print("Are you married or single? ")
status = str(input("Type m for married and s for single: "))

taxOwed = 0
taxrate = 0.0
# two variables income and status

exit = 0
while (exit==0) :
    if (status != "m") and (status != "s") :
         status = str(input("bruh m or s "))
    elif (status == "m") or (status == "s") :    exit = 1
# while loop to guarrantee an "m" or "s" answer


brokeOrnot = 0
#married filter
if(status == "m"):
    if(earnedIncome <= 0): 
        print("go to a financial advisor")
        brokeOrnot = 1

    elif(earnedIncome <= 19900):
        taxrate=.10
        taxOwed = taxrate*earnedIncome

    elif(earnedIncome >= 19901) and (earnedIncome <= 81050):
        taxrate=.12
        taxOwed = ((earnedIncome-19900)*taxrate) + (.10 * 19900)

    elif(earnedIncome >= 81051) and (earnedIncome <= 172750):
        taxrate=.22
        taxOwed = ((earnedIncome-81050)*taxrate) + ((81050-19900)*.12) + (.10 * 19900)

    else :
        print("damn you rich") 
        brokeOrnot = 1

#single filter
elif(status == "s"):
    if(earnedIncome <= 0):
         print("go to a financial advisor")
         brokeOrnot = 1

    elif (earnedIncome <= 9950):
        taxrate=.10
        taxOwed = taxrate*earnedIncome
        
    elif (earnedIncome>=9951) and (earnedIncome<=40525) :
        taxrate = .12
        taxOwed = ((earnedIncome-9950)*taxrate) + (.10 * 9950)

    elif (earnedIncome >=40526) and (earnedIncome <=86375):
        taxrate = .22
        taxOwed = ((earnedIncome-40526)*taxrate) + (.12 * (40526-9950)) + (.10 * 9950)

    else:
        print("You made too much for this calculator. Hurray!") 
        brokeOrnot = 1


if (brokeOrnot == 0): print("This year you owe ", taxOwed," in taxes")
