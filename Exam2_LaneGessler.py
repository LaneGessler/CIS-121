#Lane Gessler Exam 2

#part 1
def evenOdd(list):
    dictionary = {}
    list1 = []
    list2 = []

    for entry in list:
        if entry%2 == 0:
            list1.append(entry)
        else:
            list2.append(entry)
    # makes list for both evens and odds

    dictionary['Even']=list1
    dictionary['Odd']=list2
    #slaps the lists into the 2 entrys
    #print(dictionary)

    f= open("results1.txt","w")
    string1 = "Even: "
    string2 = "\nOdd: "
    for entry in list1:
        string1 = string1 + str(entry)+" "
    for entry in list2:
        string2 = string2 + str(entry)+" "

    f.write(str(string1))
    f.write(str(string2))

#list = [2,4,5,4,6,7,8,2,1,9,7,8,85,34,65] 
#evenOdd(list)

#end part 1
#part 2

import random
def randomLists():
    list1 = []
    list2 = []
    for cool in range(200):
        var = random.randint(1,100)
        list1.append(var)
        var = random.randint(1,100)
        list2.append(var)
    #creates the lists of random numbers

    dictionary = {}
    cool1 = 0
    for entry in list1:
        var1 = list1.index(entry)
        list1.pop(var1)
        
        dictionary[entry] = cool1+1

        cool1 = dictionary[entry]
        #needs to find out how to get the values from the keys
    cool2 = 0
    for entry in list2:
        var2 = list2.index(entry)
        list2.pop(var2)
        dictionary[entry] = cool2+1

        cool2 = dictionary[entry]
        #needs to find out how to get the values from the keys
        #if it could get the values stored in the entry it would probably work
    #tries to find and adds the value index gets

    #f=open("RESULTS4.txt","w")
    #f.write(dictionary)
    #doesnt have writing to a file out of time
    print(dictionary)
#randomLists()

#end of part 2
#part 3

def stepTracker():
    f=open("steps.txt","r")
    r = f.read()
    r.splitlines()
    sum = 0
    average = 0
    day = 0
    for cool in range(12):
        if cool == 0:
            for number in range(31):
                sum = sum+ r[day]
                day =+1
        average = sum/31
        f.write(str(average))
        average = 0
        sum = 0  

        #every one of these loops should look like this one with the ranges changed  
        
        if cool == 1:
            for number in range(28):
                
        if cool == 2:
            for number in range(31):
        if cool == 3:
            for number in range(30):
        if cool == 4:
            for number in range(31):
        if cool == 5:
            for number in range(30):
        if cool == 6:
            for number in range(31):
        if cool == 7:
            for number in range(31):
        if cool == 8:
            for number in range(30):
        if cool == 9:
            for number in range(31):
        if cool == 10:
            for number in range(30):
        if cool == 11:
            for number in range(31):

        #needs to write the values obtained in each for loop to the file
