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
4. Close the log when you close the program: <LOG.close()> *(If you end up closing the program or it crashes before the close command is given then it'll automatically flush and create the log)*

You can also check the "Example.py" file to run it and get a feeling for how it works.

# The Snoot.conf

This is the configuration file for Snooter. What you set here is what Snooter will remember.

At the current time, the MemoryNode _(Snoot.conf)_ is rather limited, but here's how you make use of it:

The file is depenend on Lines - as in the Line's order are very important as well as their values:

### Line1:
System State | This line determines if Snooter will generate logs for you.

When set to "on", Snooter will generate logs. When set to "off" Snooter will not. If set to anything else, You'll
confuse Snooter and he'll assume the default, which is on.

### Line2: 
Max Log Storage | This line determines how many Logs you'd like Snooter to hold on to. If set to 0, he will
store unlimited amount. 

When to set to any number above 0, he'll create a cap, and will do you the favor of deleting the
oldest files until you're at your cap.

### Line3:


___

# F.A.Q.s

**Q) Why the name "LogSnoot"?**

_A) Was bored while in class while I made this - I've been wanting to generate log files for awhile now,
decided to do it quicky in python - pythons made me think of the snakes from those funny internet videos where
they edit anime kawaii effects on them with statems "Human, stop - you given me a fright - you booped my snoot!" So,
the snoot is sniffing for snoops for a log._


**Q) What are your plans for this module?**

_A) Aside from recreating the project in other languages, such as Java, I don't know. I think I may try make the project
a bit easier to use and possibly expand on features?_


**Q) How do I use this?**

_A) As stated above, Import the project and create an instance, check the Example.py file for an example._


**Settings Layout**

We may want to eventually add the ability to set "profiles".

Other than that, we want our settings file to list a set of variables that will be used for later on, because of this
we can use simple boolean variables for most, int settings for more complex settings option.

+ LogSnoot_Enabled = True
+ How_Long_to_Keep_Log = 0
+ etc.

# Planned Features
+ A separate file that runs a GUI allowing a simpler way to change options regarding the 
configuration file.
+ The ability to set different output formats.
+ Including other "personalities" for Snooter, ideally a more sophisticated Snooter without the joking mood.

# Change Log
*Most recent update first*

**Version 2.3.0**

+ Modified MemoryNode.conf to now be Snoot.conf
+ Core files needed by the module will now be stored in a generated folder named "LogSnoot"
+ Better formatting for logging

**Version 2.1.2**

+ Fixed log naming layout to default into a format that sorts better in most systems.
+ Added new functions for adding spaces between each LOG line.

**Version 2.0.1**

+ Fixed bugs resulting in off-set number of files being deleted when max_files_keep is > 0

**Version 2.0.0**

+ Added MemoryNode.conf generator: This file contains settings for the user to set. Currently has to be changed by hand
+ With the Config file, you can now leave your Snoot code in your project, but disable it from generating more Logs.
+ With the config file, you can now set a Max number of Logs to keep, allowing Snooter's snoot to find which ones to delete when you're over the max.

**Version 1.2.0**

+ Added Log-Levels: Info, Warn, Error
+ Modified spacing of text in the Logs
+ Updated filename function

**Version 1.0.0**

+ The Snoot has been booped!

