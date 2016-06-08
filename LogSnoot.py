#Programmed by Zane "ZenOokami" Blalock
# This particular program is for creating a library that allows for communication to crate log files

#Things to do when file is loaded:
#   *Check to see if a "SnoopedLogs" is created, if not create one

# Imports ============================
import time
import os
import math


# Classes ==============================
class Snoop: # A log
    def __init__(self): # Initialization
        self.version = "1.2.0"
        LogDirectory()
        self.log_name = createLogName()
        self.LOG = open('SnoopedLogs/'+ self.log_name, "w") # Create log
        self.LOG.write("Welcome LogSnoot, a Snoot to be booped when it finds some snoops. \nYou are currently using version: " + self.version + "\n")
        self.LOG.write("============================\n")
        self.LOG.write(current_date() + ": Created Log, The Snoot has been Booped!\n")

    def close(self):
        self.LOG.close()

    def write(self, user_input): # Standard Log
        self.LOG.write(current_date() + ": " + user_input + "\n")

    def writeW(self, user_input): # Distinctly states if the log is a warning
        self.LOG.write("[Warning]::" + current_date() + ": " + user_input + "\n")

    def writeE(self, user_input): # Distinctly states if the log is an error
        self.LOG.write("[Error]::" + current_date() + ": " + user_input + "\n")

    def writeI(self, user_input):
        self.LOG.write("[Info]::" + current_date() + ": " + user_input + "\n")


# Functions =======================================
def current_date():
    current_time = time.asctime(time.localtime(time.time()))
    return current_time


def LogDirectory():  # This creates or acknowledges the logs folder
    if os.path.exists("SnoopedLogs"):
        print("The snoot has been booped")
    else:
        os.makedirs("SnoopedLogs")
        print("The snoot is beginning to toot")


def createLogName(): # Creates the proper name for our generated logs
    date = current_date()
    name = ""
    # We ned to remove the ':' and replace them, and spaces, with '-'
    for item in date:
        if item == ":":
            name += "-"
        elif item == " ":
            name += "-"
        else:
            name += item

    name += ".log"
    return name