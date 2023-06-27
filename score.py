# Jack Tench 2023
# Functions related to score.

# Functions to return scores for a given set of dice in ones.
def ones(dice):
    score = 0
    for die in dice:
        #print(die)
        if die == 1:
            score += 1
    return score
