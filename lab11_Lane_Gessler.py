#lab 11
#Lane Gessler
#11/10/2022

import random

class Company:
    def __init__(self,name,year):
        self.name = name
        self.year = year
    
class Car():
    def __init__(self,wheels,company,color,miles,status,speed):
        self.wheels = wheels
        self.company = company
        self.color = color
        self.miles = miles
        self.status = status
        self.speed = speed

    def __str__(self):
        print("=====Car Info=====")
        print(f"Wheels:{self.wheels}")
        print(f"Company:{self.company}")
        print(f"Color:{self.color}")
        print(f"Miles:{self.miles}")
        print(f"Status:{self.status}")
        print(f"Speed:{self.speed}")
        return ""

    def changeSpeed(self,quantity):
        self.speed = quantity

    def mileTracker(self,mile):
        self.miles = self.miles + mile

    def howFast(self):
        return self.speed

    def accelerate(self,amount):
        self.speed = self.speed + amount
        if self.speed > 60:
            self.speed = 60
        self.status = "Moving"
        

    def stop(self):
        self.speed = 0
        self.status = "Stopped"
        

    def decrease(self):
        self.speed = self.speed - 20
        if self.speed < 0:
            self.speed = 0
        self.status = "Slowing down"

car = Car(4,"Chevy","Red",0,"Moving",0)

def sixtyToZero():
    car.changeSpeed(60)
    seconds = 0
    while car.howFast() != 0:
        car.decrease()
        seconds += 1
    print(seconds,"seconds 60 to 0")
    car.mileTracker(seconds)


def zeroToSixty():
    car.changeSpeed(0)
    seconds = 0
    while car.howFast() != 60:
        car.accelerate(random.randint(1,15))
        seconds += 1
    print(seconds,"seconds 0 to 60")
    car.mileTracker(seconds)


print(car)
sixtyToZero()
zeroToSixty()