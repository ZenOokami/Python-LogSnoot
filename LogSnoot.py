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
        LogDirectory()
        self.log_name = createLogName()
        self.LOG = open('SnoopedLogs/'+ self.log_name, "w") # Create log
        self.LOG.write(current_date() + ": Created Log")

    def close(self):
        self.LOG.close()

    def write(self, user_input):
        self.LOG.write(current_date() + ": " + user_input)



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


def createLogName():
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