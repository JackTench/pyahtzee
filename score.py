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