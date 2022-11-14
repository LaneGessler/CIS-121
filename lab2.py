# the dog years is the only one thoroughly noted, the rest are not; But they are the same code minus changes to the multiplier and final print statements.

humanyears = float(input("Enter your age: "))
# source value
variableyears = humanyears*7
# year multiplier

totaldays = variableyears*360
# the value used for the math block

# big math block below
years = variableyears
years = years-(years%1)
# the mod is added to all of the math values to trim decimals

months = ((totaldays%360)/30)
months = months-(months%1)

# weeks = (totaldays%30)/7 
# disabled because weeks are not required

days = (totaldays%30)
days = days-(days%1)
# change the 30 to a 7 to account for undisabling weeks

# values assigned in the math block go on to the print statement

print ("Your age in dog years is ", years,"years", months,"months", days,"days")
# prints the years, months, weeks, days
# weeks,"weeks" (copy paste to add in weeks)


# cat years are below

variableyears = humanyears/9

totaldays = (variableyears*360)-1
# For some reason I had to add that -1 and I don't know why

years = variableyears
years = years-(years%1)
months = ((totaldays%360)/30)
months = months-(months%1)
# weeks = (totaldays%30)/7 
days = (totaldays%30)# change the 30 to a 7 to account for undisabling weeks
days = days-(days%1)
print ("Your age in cat years is ", years,"years", months,"months", days,"days")
# weeks,"weeks" (copy paste to add in weeks)


# horse years are below

variableyears = (((((humanyears*humanyears)-47)/7)+12)*3)
# *(6.46428+(1/300000)) (the copy paste for trying to cheese it)

totaldays = (variableyears*360)
# For some reason I had to add that -1 and I don't know why

years = variableyears
years = years-(years%1)
months = ((totaldays%360)/30)
months = months-(months%1)
# weeks = (totaldays%30)/7 
days = (totaldays%30)
days = days-(days%1)
# change the 30 to a 7 to account for undisabling weeks
print ("Your age in horse years is ", years,"years", months,"months", days,"days")
# weeks,"weeks" (copy paste to add in weeks)