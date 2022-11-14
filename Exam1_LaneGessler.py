# Lane Gessler Exam 1
#1a

#name = input("Please enter your name: ")
#age = (int(input ("Please enter your age: ")))
#random_number = 10/(age%23)

# Code does not run
# variables name and age are not a clarified type but do have an output in the terminal.
# line 4 causes an error in line 5 because it is a string.
# I would declare the variable type in lines 3 and 4 as a string and int
# I am unsure of whether the code is trying to use the randomized number code or not 
# if they are then random needs to be imported, if not then it works as a pseudo-random number

#1b
#while number < 100:
#    print(number)

#code does not run
#number is not defined
#there is no exit case
#I do not know what this code is intended for but I would add number += 1 to the code for an exit case
# and I would define number before the while loop

#1c
#number = 5
#if number < 3:
#    print("less")
#elif number> 3:
#    print("greater")
#else:
#    print("SAME")

#code runs, however it is hardcoded with number=5 and does not gather user input
#I would change number = 5 to number = int(input(""))
#you could change else to elif and have is be number == 3 instead of else

#1d
#for i in range(1,10):
#print(i)

#code does not run as intended, unless the intention is to just have a useless for loop
#code does not use the for loop, adding an indentation before print would work
#code does not print 10 when run, to change it increase its maximum range by 1

#1e
#user_number = 0

#while user_number != 5:
#    user_number = input("Please enter a number:")

#code runs
# user_number is defined as 0
#exit case does not seem to work, as entering 5 does not stop the while loop
#to make an exit case of 5, I would change user_number != 5: to True:
#then add an if statement with the case user_number==5: break
#then add an else: user_number=int(input("Please enter a number:"))

#2
#milk = int(input("How much milk? "))
#eggs = int(input("How many eggs? "))
#bacon = int(input("how much bacon? "))

#print(" ")
#print("Amount of milk: ",milk)
#print("Amount of eggs: ",eggs)
#print("Amount of bacon: ",bacon)

#milk = milk*2
#eggs = eggs*1.5
#bacon - bacon*3
#total = bacon + eggs + milk
#print("total cost with tax", total+(total*.11))

#3
#def Number():
#   number = str(input("Please enter a phone number: "))
#   print(number[0:3],"-",number[3:6],"-",number[6:10])
#Number()

#4
import random
count = 0

while count != 10:
    randNumber = random.randint(0,60)
    if randNumber == 0:
        randNumber+1
    if randNumber%2 == 0:
        print(randNumber)
    if randNumber >= 15:
        print("I generated the number",randNumber,", randomly")
    if 48%randNumber == 0:
        count += 1

#if a number passes both >= 15 and %2 == 0 it does with run both statements.
#I need to review how import works and import random.

