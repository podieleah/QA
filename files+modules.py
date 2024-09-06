# modules

# libraries - such standard library. Can contain multiple packages and modules.
# Packages - directories of python modules.  
# modules - just python files. 

# many built in and held in memory. Others need to imported. Other also we can install.
# pip - is our package manager. 

# pypi.org

#import math

#number = 10

#answer = math.sqrt(number) # modulename.method(args)

#print(answer)

#import math
#import random

#def random_pi():
#    return math.ceil(random.randint(1,10) * math.pi)

#for i in range(5):
#    print(random_pi())

# just with desired objects to save memory

#from math import ceil, floor, pi
#from random import randint

#def random_pi():
 #   return floor(randint(1,20) * pi)

#for i in range(5):
    #print(random_pi())

# exercise:
# Create 2 files, one called dice.py - write a function that will
# generate a random numer between 1 and 6.
# in the second file import the dice module and simulate throwing 2 dice.
# print its result.
# Check dice & dice_throw files

# Files 
# Important for logs, storing and retrieving data, sharing data, configs, running scripts
# Read, write and edit files
# Most files types are supported. Some require importing modules.

# .txt files
# Read mode ("r") - default mode - used for reading a file
# Write mode ("w") - opens a file for editing, creates a new file if it doesn't exist
# Append mode ("a") - Opens for writing, will create a file, appends to the end

# e.g-

# file = open("filename.txt", "mode")

# ...... do something

# file.close() # Remember to close the file

# Reading from a file:
# read() - Read the entire file
# readline() - Reads a line and moves to the next line
# readlines() - Reads all of the lines and puts them in a list
# seek() - go to a line defaults to line 1

# Writing to a file:
# write() - used to write a string to the file
# writelines() - used to write a list to the file

# file = open("lines.txt", "r")

# lines = file.readlines()

# print(lines)

# file = open("lines.txt", "w")

# for n in range(1,11):
#     newline = "This is a new line" + " " + str(n) + "\n"
#     file.write(newline)

# file.close()

# file = open("lines.txt", "r")

# outfile = ""

# for line in range(1, 11):
#     if line % 2 == 0:
#         outfile += file.readline()
#     else: 
#         file.readline()

# file = open("lines.txt", "w")

# file.write(outfile)
# file.close()

# with open("filename.txt", "mode") as file:
#     for n in range(1, 10):
#         newline = . . . . . 
#     file.write(newline)
#     # we do not need to close the file.

