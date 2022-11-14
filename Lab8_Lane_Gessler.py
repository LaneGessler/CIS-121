# Lane Gessler Lab 8




def dataCleaner(yourData,boolean1=None,boolean2=None):

    f = open(yourData)
    r = f.read().splitlines()
    
    clean = []
    for entry in r:
        if entry.isdigit():
            clean.append(int(entry))
    

    minimum = 0
    maximum = 0
    

    
    #print("I no idea how the fuck its ending up with 102 but 3 is the smallest number and 996 is the biggest")
    if boolean1 and boolean2 == True:
        stop = True
        list1 = []
        list1 = clean.copy()
        while stop == True:
            for number in range(0,len(list1)):
                if len(list1)<=1:
                    stop = False
                    break
                if number+1 >= len(list1):
                    break
            
                if list1[number+1] <= list1[number]:
                #print("length:", len(list1)," ", list1[number+1],"<=",list1[number],"case 1")
                   list1.pop(number)               
                elif list1[number] <= list1[number+1]:
                #print("length:", len(list1)," ", list1[number],"<=",list1[number+1],"case 2") 
                    list1.pop(number+1)
        #print("repeat")
    
    #this should print 3 I dont know why or how 102 appears
        minimum = list1[0]
        stop = True
        list2 = []
        list2 = clean
        while stop == True:
            for number in range(0,len(list2)):
            
                if len(list2)<=1:
                    stop = False
                    break
                if number+1 >= len(list2):
                    break
                if list2[number+1] >= list2[number]:
                #print("length:", len(list2)," ", list2[number+1],">=",list2[number],"case 1")
                    list2.pop(number)               
                elif list2[number] >= list2[number+1]:
                #print("length:", len(list2)," ", list2[number],">=",list2[number+1],"case 2") 
                    list2.pop(number+1)
        #print("repeat")
        maximum = list2[0]
        return [minimum,maximum]

    elif boolean1 == True:
        stop = True
        list1 = []
        list1 = clean.copy()
        while stop == True:
            for number in range(0,len(list1)):
                if len(list1)<=1:
                    stop = False
                    break
                if number+1 >= len(list1):
                    break
            
                if list1[number+1] <= list1[number]:
                #print("length:", len(list1)," ", list1[number+1],"<=",list1[number],"case 1")
                    list1.pop(number)               
                elif list1[number] <= list1[number+1]:
                #print("length:", len(list1)," ", list1[number],"<=",list1[number+1],"case 2") 
                    list1.pop(number+1)
        #print("repeat")
    
    #this should print 3 I dont know why or how 102 appears
        minimum = list1[0]
        return [minimum]

    elif boolean2 == True:
        stop = True
        list2 = []
        list2 = clean
        while stop == True:
            for number in range(0,len(list2)):
            
                if len(list2)<=1:
                    stop = False
                    break
                if number+1 >= len(list2):
                    break
                if list2[number+1] >= list2[number]:
                #print("length:", len(list2)," ", list2[number+1],">=",list2[number],"case 1")
                    list2.pop(number)               
                elif list2[number] >= list2[number+1]:
                #print("length:", len(list2)," ", list2[number],">=",list2[number+1],"case 2") 
                    list2.pop(number+1)
        #print("repeat")
        maximum = list2[0]
        return [maximum]
    

var = "randomValues.txt"
var = input("What file: ")
boolean2 = bool(input("minimum (enter nothing for no) "))
boolean1 = bool(input("maximum (enter nothing for no) "))
print(dataCleaner(var,boolean2,boolean1))