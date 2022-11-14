"""
#Name Lane Gessler
#Date 10/24/2022

This implements the RoboFriend class.
"""

class RoboFriend:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        print(f"my name is {self.name}")
        print(f"my age is {self.age}")
        return ""

    def stateName(self):
        return print(f"Hello. My name is {self.name}")
        
    def stateAge(self):
        return print(f"I’m {self.age} years old.")
        
        