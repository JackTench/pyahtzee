# Jack Tench 2023

# Imports
from random import randint

# Class for die.
class Die():

    # Constructor method.
    def __init__(self):
        self.sides = 6
        self.currentSideUp = 1      # Always start with the 1 facing upwards.

    # Method to roll die.
    def roll(self):
        self.currentSideUp = randint(1, self.sides)

    # Method to return the current side facing upwards.
    # This decouples querying the object from changing the number on the die with a roll.
    def get(self):
        return self.currentSideUp
    
# Class for player.
class Player():

    # Constructor method.
    def __init__(self, name):

        # Set player defaults.
        if name == "":
            self.name = "Player"
        else:
            self.name = name
        self.score = 0

        # Give player 5 dice.
        self.dice = []
        for i in range(0,5):
            self.dice.append(Die())

        # List of booleans for available score categories per player. All start at false.
        self.usedCats = [False, False, False, False, False, False, False, False, False, False, False, False, False]

    # Method to roll all dice belonging to the player.
    def roll(self):
        self.result = []
        for die in self.dice:
            die.roll()
            self.result.append(die.get())
        return self.result
    
    # Method to return name of the player.
    def getName(self):
        return self.name

    # Method to add score to the player.
    def addScore(self, amount):
        self.score += amount

    # Method to return player's score.
    def getScore(self):
        return self.score
