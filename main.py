# Jack Tench 2023
# This python file just runs a game of yahtzee using this code base.

# Imports
import player
import score

# Global Variables
title = "pyahtzee"
version = "0.1a"

# Print statements for top of terminal.
print(title + " " + version)

# Set amount of player(s).
playersAmount = int(input("Number of players: "))

# Get player names.
playerNames = []
for i in range(0, playersAmount):
    qString = "Player " + str(i + 1) + "'s Name: "
    name = input(qString)
    playerNames.append(name)

# Create player object for each physical player.
players = []
for playerName in playerNames:
    players.append(player.Player(playerName))

