def mean(r):
    #file = str(input("Enter the file name: "))
    #f = open(file)
    #r=f.read()
    #r=r.split()
    #opens "500DayFruitData.txt and splits the text file into entrys for a list after every space

    total = []
    apples=0
    #initializes total and apples for the for loop

    for number in range(0,len(r)):
        if r[number]=="apple":
            apples+=1
            if r[number+1].isdigit():
                total.append(r[number+1])
    #finds "apple" in r then adds 1 do apples, next if goes to next entry and passes if its a number
    #then it adds the entry to another list

    x = 0
    for number in total:
        x = x + int(number)
    # creates a sum of all the numbers from total

    mean = x/apples

    return mean

def median(r):
    #file = str(input("Enter the file name: "))
    #f = open(file)
    #r=f.read()
    #r=r.split()
    #opens "500DayFruitData.txt and splits the text file into entrys for a list after every space

    total = []
    apples=0
    #initializes total and apples for the for loop

    for number in range(0,len(r)):
        if r[number]=="apple":
            apples+=1
            if r[number+1].isdigit():
                total.append(r[number+1])
    #finds "apple" in r then adds 1 do apples, next if goes to next entry and passes if its a number
    #then it adds the entry to another list

    x = 0
    for number in total:
        x = x + int(number)
    # creates a sum of all the numbers from total

    median = x/2

    return median








