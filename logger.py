# Jack Tench 2023

# Imports
import datetime

# Helper function for logging date and time.
def stamp():
    return str(datetime.datetime.now())

# Function to run when initializing a log.
def initLog():

    # Mark stuff here as global.
    global filename

    # Get current date and time, then set file name for log.
    fileStamp = stamp()
    filename = "log " + stamp + ".txt"

    # Open file for writing.
    # If file does not exist it is created.
    file = open(filename, "w")

# Function for writing a line to the log.
def log(event):

    # Get current time/date stamp
    lineStamp = "[LOGGER] [" + str(stamp()) + "] "

    # Open log.
    file = open(filename, "w")

    # Write line.
    file.write(lineStamp + event + "\n")