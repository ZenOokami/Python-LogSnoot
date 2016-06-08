print("As an example, let's create a random log!")
import LogSnoot

LOG = LogSnoot.Snoop()

print("We've now opened a text file! Let's add in our own custom log!")
user_input = input("Input something: ")

LOG.write(user_input)

print("And now we close our file at the end of our program!")

LOG.close()