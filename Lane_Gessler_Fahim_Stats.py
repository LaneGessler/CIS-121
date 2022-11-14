#Lane Gessler
#Fahim Uz Zaman

#file = "50DayFruitData.txt"
from unicodedata import name
import statistics

name = "50DayFruitData.txt"
def mean(name):

    f = open(name)
    r=f.read()
    r = r.split()

    list = []
    count = 0

    for number in range(0,len(r)):
        if r[number] == "apple":
            count+=1
            list.append(r[number+1])
    #gets count of days for apples eaten
    #adds value for that day into a list

    total = 0
    for number in list:
        total = total + int(number)
    #adds the values together from the list stated before
    output = total/count

    d = open("Lane_Gessler_Fahim_Output.txt","a")
    d.write("\nThe mean number of apples eaten is ")
    d.write(str(output))
    d.close()

#mean(name)

def median(name):
    f = open(name)
    r=f.read()
    r = r.splitlines()
    r.pop(0)


    apples = []
    temp = []



    for item in r:
       
        temp = (item.split())
        
        if temp[1] == "apple":
            apples.append(int(temp[2]))
    
    output = statistics.median(apples)
    d = open("Lane_Gessler_Fahim_Output.txt","a")
    d.write("\nThe median number of apples eaten is ")
    d.write(str(output))
    d.close()

def mode(name):
    f = open(name)
    r=f.read()
    r = r.splitlines()
    r.pop(0)


    apples = []
    temp = []



    for item in r:
       
        temp = (item.split())
        
        if temp[1] == "apple":
            apples.append(int(temp[2]))
    
    output = statistics.mode(apples)
    d = open("Lane_Gessler_Fahim_Output.txt","a")
    d.write("\nThe mode number of apples eaten is ")
    d.write(str(output))
    d.close()



