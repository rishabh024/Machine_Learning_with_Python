'''
Python sys module provides various functions that allow us to interact with the interpreter directly.
'''

import sys

''' sys.argv is used to get arguments at command line by user.The first argument, argv[0] is the name of the 
Python script itself. Depending on the platform that you are running on, the first argument may contain the 
full path to the script or just the file name.'''

print('The command line arguments are:')
for i in sys.argv:
    print(i)

# sys.version – This stores the information about the current version of python
print(sys.version)

# input from sys module
user_input = sys.stdin.readline()
print("Input is:- " + user_input)

# stdout also prints the no of bytes to be printed on screen
print(sys.stdout.write("university"))

# It displays a string containing the version number of the current Python interpreter.
print(sys.version)
print(sys.version_info)

# It is used to see what particular operating system/platform, we’re using to run the program
print(sys.platform)

# Path variable stores the directory path in the form of a list of strings
# path displays the python path set in current system
# Path index stores the directory containing the script that was used to invoke the Python interpreter at the index “Zero”
print(sys.path[0])
print(sys.path)

# It displays the copyright information on currently installed Python version
print(sys.copyright)

# getrefcount() method returns the count for references to an object where it is used.
# Python keeps track of this value, as, when this value reaches 0 in a program, the memory for this variable is cleaned up
# getrefcount()- get reference count

a = int(input("enter no"))
b = input("enter string")
print(sys.getrefcount(a))
print(sys.getrefcount(b))
print(sys.getrefcount(756))

# sys.executable gives the absolute path to the Python interpreter. This is useful when you are using
# someone else’s machine and need to know where Python is installed

print(sys.executable)

# sys.maxsize:- It returns the largest integer, a variable can take.
# On a 32-bit platform, it is 2**31 - 1
# On a 64-bit platform, it is 2**63 - 1
print(sys.maxsize)

# sys.exit() function allows the developer to exit from Python. The exit function takes an optional argument,
# typically an integer, that gives an exit status. Zero is considered a “successful termination”.
sys.exit(0)

# This method makes the Python interpretor exits the current flow of execution abruptly
sys.exit(1)
