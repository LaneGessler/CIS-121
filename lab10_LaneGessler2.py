class HighTwoGame:
    def __init__(self,Player1,Player2):
        self.Player1 = Player1
        self.Player2 = Player2
    
    def playOneGame(self):
        self.game1 = Player(self.Player1,6,10)
        self.game2 = Player(self.Player2,6,10)

    #def playManyGames(self):

    def __str__(self):
        print(f"{self.Player1} rolled {self.Player1.getDiceValue()}")
        return ""

class Player:
    def __init__(self,Name,Die1,Die2):
        self.Name = Name
        self.Die1 = Die1
        self.Die2 = Die2

    def rollDice(self):
        self.Die1 = Dice(self.Die1,1)
        return self.Die1
    
    def getDiceValue(self):
        return self.Die1

import random

class Dice:
    def __init__(self,Sides,Value):
        self.Sides = Sides
        self.Value = Value

    def roll(self):
        self.Sides = random.randint(self.Value,self.Sides)
        return self.Sides

    #def getValue(self):