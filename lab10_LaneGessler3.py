import random

class Die:
    def __init__(self,Sides,Value):
        self.Sides = Sides
        self.Value = Value

    def roll(self):
        self.Value = random.randint(1,self.Sides)
        return self.output

    def getValue(self): 
        return ""

    #def __str__(self):
    #def __add__(self):
    #def __gt__(self):

class Player:
    def __init__(self,Name,Die1,Die2):
        self.Die1 = Die1
        self.Die2 = Die2
        self.Name = Name

    def rollDice(self):
        self.Name = Die(self.Die1,self.Die2)

    #def getDiceValue(self):

class HighTwoGame:
    def __init__(self,Player1,Player2):
        self.Player1 = Player1
        self.Player2 = Player2
        
    def playOneGame(self):
        self.Player1 = Player(self.Player1,6,10)
        self.Player2 = Player(self.Player2,6,10)
        self.Player1.rollDice()
    #def playManyGames(self):
    #def __str__(self):