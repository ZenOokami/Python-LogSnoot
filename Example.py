print("As an example, let's create a random log!")
import LogSnoot

LOG = LogSnoot.Snoop()

print("We've now opened a text file! Let's add in our own custom log!")
user_input = input("Input something: ")

LOG.write(user_input)

print("Lets test a labeled statement!")
LOG.writeE("This is where an error for a particular statement goes.")
LOG.writeW("This is where warning goes, in case a conditional statement should never reach or something.")

print("And now we close our file at the end of our program!")
print("This has been just an example!")

LOG.close()
