#Programmed by Zane "ZenOokami" Blalock
#      Http://EssenceOfZen.org/
# This particular program is for creating a library that allows for communication to crate log files
# You can find an example file that shows the use of LogSnoot
# You can also find our videos on the project over at your channel, http://YouTube.com/EssenceOfZen

#Things to do when file is loaded:
#   *Check to see if a "SnoopedLogs" is created, if not create one
#   * We're going to want to have the system keep track of the logged files - if said files are dated beyond the timespan of the user's setting
#     we can do this by running a check on the file names in the Log folder and comparing them to the date.

#Mascot: Snooter? The Python

# Imports ============================
import time
import os
import math

# Classes ==============================
class Snoop: # A log
    def __init__(self): # Initialization
        self.version = "2.0.0"
        LogDirectory() # Check for the directory
        self.log_name = createLogName()
        self.LOG = open('SnoopedLogs/'+ self.log_name, "w") # Create Log file
        self.LOG.write("Welcome LogSnoot, a Snoot to be booped when it finds some snoops. \nYou are currently using version: " + self.version + "\n")
        self.LOG.write("============================\n")
        self.LOG.write(current_date() + ": Created Log, The Snoot has been Booped!\n")

        # Adding for v2.0
        # Do we have a settings file?
        LogSettings()  # check for settings

    def close(self):
        self.LOG.close()

    # These are our write functions with levels -- you can have normal logged statements
    # or you can utilize levels that act as a message for specific functions in your project.
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
        print("The snoot has been booped before.")
    else:
        os.makedirs("SnoopedLogs")
        print("The snoot is beginning to toot for the first time.")

def LogSettings(): # This creates the settings file sand checks
    if os.path.isfile("Snoot.conf"):
        # If our setting file exists, cool
        print("The Python's snoot remembers your setting!")
        # Read the file
    else:
        print("Snooter is confused, so Snooter is going to generate a memory node!")
        SETTINGS = open('MemoryNode.conf', "w")

        #Write our File
        SETTINGS.write("system_toggle = on \n")
        SETTINGS.write("keep_files_days = 0 \n")
        #SETTINGS.write("date_format = mm/dd/yyyy")

        #Close the file write process
        SETTINGS.close()


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