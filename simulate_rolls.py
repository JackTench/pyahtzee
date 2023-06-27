# Jack Tench 2023
# Simulates dice rolls in yahtzee and prints each category's score for the corresponding dice roll.

# Imports
import player
import score
import main

# Create a simulated player.
simulatedPlayer = player.Player("Simulated Player")

# Print statements for top of terminal.
print(main.title + " " + main.version)
print("Dice Roll + Score Simulation")

# Get input from user on how many rolls to simulate.
timesToSimulate = int(input("How many dice rolls? "))

# Seperation line.
print("\n")

# Main Loop.
for i in range(0, timesToSimulate):

    # Simulated player rolls 5 dice.
    diceRoll = simulatedPlayer.roll()

    # Print the outcome of the roll.
    print("Dice: " + str(diceRoll))

    # Scores for that set of dice are printed. Then prints seperation line.
    score.printScores(diceRoll)
    print("\n")