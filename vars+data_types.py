# Variables - a reference (a name), a selection of memory (memory location).
# Location is protected, can be called/altered/deleted on by name.

person_one_age = 30
x = 30

# Naming convention
# Should be descriptive, lowercase, never start with a number.
# Follow teams style and be consistent.
# Pep-8 style guide
# e.g -
# 1var = cant start with a number
# Var = Capitals are reserved for class names
# VAR = constant - just a convention - means we do not want the value to change.
# print = avoid built in python keyword. print_ as workaround.

# person_one_age = snake_case
# personOneAge - camelCase

# Scope:
# global_variable = "accessible everywhere"
# def my_function():
#     local_variable = "accessible only in this function"
#     print(local_variable) # this will work
#     print(global_variable) # this will also work
# my_function()

# In Built Functions
# print("prints to standard output")
# input('prompts for an input in standard input') default to a string.
# type (what is the data type)

# Data Types
# x - 10 integer
# y = '10' string
# z = True/False Booleans
# v = 10.25 float - decimal number

# Escape Characters
# \ "hi 'you", \"hello\" " - Breaks up speech so the " isnt recognised as end of line
# \n - ends line, creates a new line
# \t - inserts tab
# \u - unicode e.g \U#FFFFFF changes text to color #FFFFF or \U0001f604 a smiley face
# An example -
# print("person1: \tHey how are you?\nperson2: \tIm good thanks \U0001f604")
# Will print out -
# person1:    Hey how are you?
# person2:    Im good thank (smiley face)

# BODMAS -
# Brackets 
# Order Of
# Division /
# Multiplication *
# Addition +
# Subtraction -
# Floor Division // - is a division operation that returns the largest integer that is less than or equal to the result of the division - e.g 10//3 = 3
# Modulo % - is the remainder after dividing one number by another. e.g 10%3 = 1

# String Concatanation

# name = input("What is your name? ")
# age = int(input("What is your age? "))
# message = "your name is {}, your age is {}".format(name, age)
# print("your name is " + name)
# print("your name is", name, "your age is", age)
# print(f"your name is {name}, your age is {age}")
# print(message)

# String Methods

# print("HELLO WORLD".lower())
# print("hello world".upper())
# print("hello world".count("l"))
# print("hello world world world".replace("world", "class", 2))
# print("hello world".split()) # - whitespace is the default to split the words to change do the following
# print("hello,world".split(",")) # - now splits by the comma