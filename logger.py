# Jack Tench 2023

# Imports
from datetime import datetime

class Logger():

    # Constructor method.
    def __init__(self, name):

        # Get current date and time as string when a logger is created.
        self.dt = datetime.now().strftime("%d.%m.%Y %H:%M")

        # Set logger name.
        self.name = "Log - " + name + " " + self.dt + ".txt"

        # Create log file.
        with open(self.name, "w") as self.logfile:
            self.logfile.write("Logfile created. \n")
            self.logfile.write(self.name + "\n")

test = Logger("test")