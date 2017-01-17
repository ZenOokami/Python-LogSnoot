# Python-LogSnoot
A python module framework that is targeted at allowing any python project to be able to create log files in order to keep note on exactly what is going on.

Master Branch: [ ![Codeship Status for ZenOokami/Python-LogSnoot](https://app.codeship.com/projects/bd828c50-bbe0-0134-cf62-4683eea0ea95/status?branch=master)](https://app.codeship.com/projects/195766)

Dev Branch: [ ![Codeship Status for ZenOokami/Python-LogSnoot](https://app.codeship.com/projects/bd828c50-bbe0-0134-cf62-4683eea0ea95/status?branch=Dev)](https://app.codeship.com/projects/195766)

**How to use?**

Rather simple:

1. Import the package
2. Create an instance of the class from the package, I recommend: <LOG = LogSnoot.Snoop> but "LOG" can be replaced with
anything.
3. Use the class functions to make your logs: <LOG.writeI(your_input_here)>
4. Close the log when you close the program: <LOG.close()>

You can also check the "Example.py" file to run it and get a feeling for how it works.


**F.A.Q.s**

Q) Why the name "LogSnoot"?

A) Was bored while in class while I made this - I've been wanting to generate log files for awhile now,
decided to do it quicky in python - pythons made me think of the snakes from those funny internet videos where
they edit anime kawaii effects on them with statems "Human, stop - you given me a fright - you booped my snoot!" So,
the snoot is sniffing for snoops for a log.


Q) What are your plans for this module?

A) Aside from recreating the project in other languages, such as Java, I don't know. I think I may try make the project
a bit easier to use and possibly expand on features?


Q) How do I use this?

A) As stated above, Import the project and create an instance, check the Example.py file for an example.


**Settings Layout**

We may want to eventually add the ability to set "profiles".

Other than that, we want our settings file to list a set of variables that will be used for later on, because of this
we can use simple boolean variables for most, int settings for more complex settings option.

+ LogSnoot_Enabled = True
+ How_Long_to_Keep_Log = 0
+ etc.


**Change Log**

Version 1.2.0

+ Added Log-Levels: Info, Warn, Error
+ Modified spacing of text in the Logs
+ Updated filename function

Version 1.0.0

+ The Snoot has been booped!

