# Jack Tench 2023
# Functions related to score.

# Imports
from itertools import combinations

# Function to return score for a given set of dice in ones.
def ones(dice):
    score = 0
    for die in dice:
        if die == 1:
            score += 1
    return score

# Function to return score for a given set of dice in twos.
def twos(dice):
    score = 0
    for die in dice:
        if die == 2:
            score += 1
    return score

# Function to return score for a given set of dice in threes.
def threes(dice):
    score = 0
    for die in dice:
        if die == 3:
            score += 1
    return score

# Function to return score for a given set of dice in fours.
def fours(dice):
    score = 0
    for die in dice:
        if die == 4:
            score += 1
    return score

# Function to return score for a given set of dice in fives.
def fives(dice):
    score = 0
    for die in dice:
        if die == 5:
            score += 1
    return score

# Function to return score for a given set of dice in sixes.
def sixes(dice):
    score = 0
    for die in dice:
        if die == 6:
            score += 1
    return score

# Function to return score for a given set of dice in three of a kind.
def threeOfAKind(dice):
    score = 0

    # Check if any 3 items in the list are the same.
    for combination in combinations(dice, 3):
        if len(set(combination)) == 1:
            
            # If 3 items in list are identical. Return sum of the identical ones.
            score = sum(combination)
            return score

        else:
            return 0
