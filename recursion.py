
def recursion(count):
    if count <= 0:
        return
    else:
        count =count-1
        print("cool")
        recursion(count)
        
count = int(input("how many recursion you want? "))
recursion(count)
