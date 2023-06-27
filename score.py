# Jack Tench 2023
# Functions related to score.

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
