# Jack Tench 2023
# Functions related to score.

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

# Function for full house. From ChatGPT, might suck.
def fullHouse(dice):
    if set(dice) and (dice.count(x) == 2 or dice.count(x) == 3 for x in dice):
        return 25
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