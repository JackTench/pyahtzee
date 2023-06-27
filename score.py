# Jack Tench 2023
# Functions related to score.

# Class for score card.
class ScoreCard():

    def __init__(self):
        
        # Set all scores to 0.
        self.board = []
        for i in range(0, 12):
            self.board.append(0)

    # Method to calculate total score.
    def calculateTotal(self):
        return sum(self.board)
    
    # Method to check if player has scored in category.
    def checkCategory(self, category):

        # Returns False if the corresponding score is 0.
        if self.board[category] == 0:
            return False
        else:
            return True
        
    # Method for scoring in a given category with dice.
    def score(self, category, dice):

        # Horrible if statements inbound.
        # Score in chance.
        if category == 0:
            if self.checkCategory(category) == False:
                self.board[category] = chance(dice)
        
        # Score in ones.
        elif category == 1:
            if self.checkCategory(category) == False:
                self.board[category] = ones(dice)
        
        # Score in twos.
        elif category == 2:
            if self.checkCategory(category) == False:
                self.board[category] = twos(dice)

        # Score in threes.
        elif category == 3:
            if self.checkCategory(category) == False:
                self.board[category] = threes(dice)
        
        # Score in fours.
        elif category == 4:
            if self.checkCategory(category) == False:
                self.board[category] = fours(dice)

        # Score in fives.
        elif category == 5:
            if self.checkCategory(category) == False:
                self.board[category] = fives(dice)

        # Score in sixes.
        elif category == 6:
            if self.checkCategory(category) == False:
                self.board[category] = sixes(dice)

        # Score in three of a kind.
        elif category == 7:
            if self.checkCategory(category) == False:
                self.board[category] = threeOfAKind(dice)
        
        # Score in four of a kind.
        elif category == 8:
            if self.checkCategory(category) == False:
                self.board[category] = fourOfAKind(dice)
        
        # Score in full house.
        elif category == 9:
            if self.checkCategory(category) == False:
                self.board[category] = fullHouse(dice)

        # Score in small straight.
        elif category == 10:
            if self.checkCategory(category) == False:
                self.board[category] = smallStraight(dice)

        # Score in large straight.
        elif category == 11:
            if self.checkCategory(category) == False:
                self.board[category] = largeStraight(dice)

        # Score in yahtzee.
        elif category == 12:
            if self.checkCategory(category) == False:
                self.board[category] = yahtzee(dice)

# Helper functions for calculating scores.
# These functions are based off a gist by markheath on github.
# https://gist.github.com/markheath/1036722/245773ec132815856fd0e60a37dce0520d57b811
def count(dice, number):
    return len([y for y in dice if y == number])

def sumSingle(dice, selected):
    return sum([x for x in dice if x == selected])

def highestRepeated(dice, minRepeats):
    unique = set(dice)
    repeats = [x for x in unique if count(dice, x) >= minRepeats]
    return max(repeats) if repeats else 0

def ofAKind(dice, n):
    return highestRepeated(dice, n) * n

# End of helper functions.

# Functions for Ones, Twos, Threes, Fours, Fives and Sixes.
def ones(dice):
    return sumSingle(dice, 1)
def twos(dice):
    return sumSingle(dice, 2)
def threes(dice):
    return sumSingle(dice, 3)
def fours(dice):
    return sumSingle(dice, 4)
def fives(dice):
    return sumSingle(dice, 5)
def sixes(dice):
    return sumSingle(dice, 6)

# Chance function. Just a sum of the dice.
def chance(dice):
    return sum(dice)

# Functions for three and four of a kind.
def threeOfAKind(dice):
    return ofAKind(dice, 3)

def fourOfAKind(dice):
    return ofAKind(dice, 4)

# Function for full house.
def fullHouse(dice):
    # ChatGPT cleaned up this messy function for me.
    counts = {}

    for die in dice:
        counts[die] = counts.get(die, 0) + 1
    
    if set(counts.values()) == {2, 3}:
        return 25
    else:
        return 0

# Functions for small and large straight.
def smallStraight(dice):
    if tuple(sorted(dice)) == (1,2,3,4,5):
        return 15
    else:
        return 0

def largeStraight(dice):
    if tuple(sorted(dice)) == (2,3,4,5,6):
        return 20
    else:
        return 0
    
# Function for Yahtzee!
def yahtzee(dice):
    if len(dice) == 5 and len(set(dice)) == 1:
        return 50
    else:
        return 0
    
# End of functions for calculating score.

'''
    Score Data Structure
    scores[0] = Chance
    scores[1] = Ones
    scores[2] = Twos
    scores[3] = Threes
    scores[4] = Fours
    scores[5] = Fives
    scores[6] = Sixes
    scores[7] = Three of a kind
    scores[8] = Four of a kind
    scores[9] = Full House
    scores[10] = Small Straight
    scores[11] = Large Straight
    scores[12] = Yahtzee
'''

# Print all valid ways to score a set of dice.
def scoreDice(dice):
    scores = []     # Returns a list of scores that conforms to the data structure.
    scores.append(chance(dice))
    scores.append(ones(dice))
    scores.append(twos(dice))
    scores.append(threes(dice))
    scores.append(fours(dice))
    scores.append(fives(dice))
    scores.append(sixes(dice))
    scores.append(threeOfAKind(dice))
    scores.append(fourOfAKind(dice))
    scores.append(fullHouse(dice))
    scores.append(smallStraight(dice))
    scores.append(largeStraight(dice))
    scores.append(yahtzee(dice))
    return scores

# Print scores in terminal in a way a human can read them.
def printScores(dice):

    # Populate list with all possible scores.
    scores = scoreDice(dice)

    # Print statements.
    print("Chance: " + str(scores[0]))
    print("Ones: " + str(scores[1]))
    print("Twos: " + str(scores[2]))
    print("Threes: " + str(scores[3]))
    print("Fours: " + str(scores[4]))
    print("Fives: " + str(scores[5]))
    print("Sixes: " + str(scores[6]))
    print("3 of a kind: " + str(scores[7]))
    print("4 of a kind: " + str(scores[8]))
    print("Full House: " + str(scores[9]))
    print("Small Straight: " + str(scores[10]))
    print("Large Staight: " + str(scores[11]))
    print("Yahtzee: " + str(scores[12]))