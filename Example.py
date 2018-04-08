print("As an example, let's create a random log!")
import LogSnoot

LOG = LogSnoot.Snoop()

print("We've now opened a text file! Let's add in our own custom log!")

LOG.timeStampStart()
custom_start = LOG.customTimeStamp()

user_input = input("Input something: ")

LOG.write(user_input)

LOG.timeStampEnd()
custom_end = LOG.customTimeStamp()

print("Took " + str("%.2f" % LOG.time_length) + " seconds long.")
print("Lets test a labeled statement!")
LOG.writeE("This is where an error for a particular statement goes.")
LOG.writeW("This is where warning goes, in case a conditional statement should never reach or something.")
LOG.debug("Testing Debug")

time_length = LOG.getTimeLength(custom_start, custom_end)
print("Custom Time Length: " + str(time_length))

print("And now we close our file at the end of our program!")

LOG.close()
