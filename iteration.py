# iteration is another word for loops.
# repeating blocks of code over and over.
# saves time, avoids duplicating code. 

# 2 types of loops - while/for

# While Loop
# a while loop while continuously execute code until a condition is met.
# if the condition the never met the while loop wont stop.
# we have conditions to start a while loop - if not met it wont start. 
# x = 0
# while x < 101:
#     print(x)
#     x += 1 # plus one and loop
#     # Will print 0, 1, 2, 3, 4 etc until it gets to 101 (stops printing at 100)


# Break - Stops the Loop
# i = 1
# while i < 6:
#     print(i) # 1. will print 1
#     if i == 3: # 3. once it gets to 3 will stop looping
#         break
#     i += 1 # 2. will add 1 and go back to step 1
#     # Will print 1, 2, 3 then stop.


# Continue - Will skip an iteration in a loop
# j = 0
# while j < 6:
#     j += 1
#     if j == 3:
#         continue
#     print(j)
#     # Will print 1, 2, 4, 5, 6 - skips 3


# While True
# while True:
#     name = input("Enter your name: ")
#     if name == "quit":
#         break
#     else:
#         print(f"Hello {name}")
# This will print the following continuously until you enter "quit" to break the loop
# Enter your name: Jodie
# Hello Jodie
# Enter your name: quit


# For Loops - will iterate over a collection - lists/dictionaries/strings etc.
# my_fruits = ["apple", "orange", "kiwi"] # our list
#  # item         #iterables
# for x in my_fruits: # iterables in my item
#     print(x)
#     # prints apple orange kiwi

# numbers = [1, 2, 3, 4]
# for number in numbers:
#     print(numbers)
#     # Will print - [1, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 4]

# numbers = [1, 2, 3, 4]
# l = 0
# while l < len(numbers):
#     print(numbers[1])
#     l += 1
#     # will print - 2 2 2 2

# for a in range(5):
#      print(a)
#      # will print 0, 1, 2, 3, 4

# for a in range(1,4):    
#     print(a)
#     # will print 1, 2, 3

# for a in range(1, 10, 2):
#     print(a)
#     # will print 1, 3, 5, 7, 9


# Strings
# for letter in "hello":
#     print(letter)

# for work in "hello world".split():
#     print(word)


# List Comprehension - is for making a list
        #expression  #item     #iterable
# result = [x**2 for x in range(5)]
# print(result)
# # Prints 0-4 sqaured as a list - [0, 1, 4, 9, 16]

# Make the same formula above more pythonic -
# result = [] # Create an empty list
# for x in range(5):
#     result.append(x**2) # Add answer to the list
# print(results) # prints [0, 1, 4, 9, 16]

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#                     # expression    #item   #iterable       #condition
# even_squared_numbers = [number**2 for number in numbers if number % 2 == 0]
# print(even_squared_numbers)
# Will print the even numbers squared [4, 16, 36, 64, 100]


# Dictionaries
# for i in {"drink": "water"}:
#     print(i)
#     # prints drink (only the key)

# for i in {"drink": "water"}.values():
#     print(i)
#     # prints water (only the value)

# for i in {"drink": "water"}.items():
#     print(i)
#     # prints ('drink', 'water') 

# for i, j in {"drink": "water"}.items():
#     print(i, j)
#     # splits the key and value, prints drink water


# Nested For Loops
# for i in range(1, 3):
#     for j in range(1,4):
#         print(i, "x", j, "=", i*j)
#         # prints 
#         # 1 x 1 = 1 
#         # 1 x 2 = 2 
#         # 1 x 3 = 3 
#         # 2 x 1 = 2 
#         # 2 x 2 = 4
#         # 2 x 3 = 6
#         # 2 x 2 = 4
#         # 2 x 3 = 6


# Exercise 
# Write a loop that takes 5 names and prints the name + is cool
# while loop 
# for loop 
# list comprehension 
# optional - list com 1 line only

# While Loop
# counter = 0
# while counter < 5:
#     name = input("Enter a name: ")
#     print(name + " is cool")
#     counter += 1

# For Loop
# for x in range(5):
#     name = input("Enter a name: ")
#     print(name + " is cool")

# List comp in 1 line
# [print(f"{name} is cool") for name in [input("Enter a name: ") for x in range(5)]]


