# Part 1 - 

# person = 19
# if person >= 18:
#     print("You are in catergory A")
# elif person >= 16:
#     print("You are in catergory B")
# else:
#     print("You are in catergory C")

# Part 2 - Calculator

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# operator = int(input("Select corresponding number for your operation -\n 1. Add +\n 2. Subtract -\n 3. Multiply *\n 4. Divide /\n 5. Square S\n : "))

# if operator == 1:
#     result = num1 + num2
# elif operator == 2:
#     result = num1 - num2
# elif operator == 3:
#     result = num1  * num2
# elif operator == 4:
#     result = num1 / num2
# elif operator == 5:
#     result = num1 ** 2
# else: 
#     print("Please try again")
# print("Answer is", result)

# Task 2 - Calculate Exam Grades

# grade = int(input("Enter grade? "))
# if grade < 1 or grade > 100:
#     print("Error: marks must be between 1 and 100")
# elif grade < 50:
#     print("Fail")
# elif grade >= 50 and grade <= 60:
#     print("Pass")
# elif grade >= 61 and grade <= 70:
#     print("Merit")
# else:
#     print("Distinction")

# Task 3 - Calculate Exam Grades with levels

# mark = int(input("Enter grade? "))
# level = int(input("Enter level 1 or 2: "))

# if mark < 1 or mark > 100:
#   print("Error: marks must be between 1 and 100")
# elif level == 1:
#   if mark < 50:
#     print("Fail")
#   elif mark <= 60:
#     print("Pass")
#   elif mark <= 70:
#     print("Merit")
#   else:
#     print("Distinction")
# elif level == 2:
#   if mark < 40:
#     print("Fail")
#   elif mark <= 50:
#     print("Pass")
#   elif mark <= 65:
#     print("Merit")
#   else:
#     print("Distinction")
# else:
#   print("Invalid level. Please enter 1 or 2.")



# Task 4 - Pythagoras
# In this lab you'll write a program that calculates the lengths of sides of a triangle using Pythagoras’s Theorem.

# Pythagoras’ Theorem states that the square of the long side (C) of a right-angled triangle is the sum of the squares of the two shorter sides (A and B).  
# ​C**2 = A**2 + B**2

# (**2 in Python will raise to power of 2)  
# C
# B
# A

# Add a new file: Pythagoras.py  to your existing project and make it the startup file.
# 1. Print a menu:  
# Pythagoras’ Calculator  
# 1. Find the length of A given B and C  
# 2. Find the length of B given A and C
# 3. Find the length of C given A and B
 
# 2. Print the result.  
# 3. If ‘1’ is entered, prompt for the length of sides: B and C, calculate the length of side: A
# 4. If ‘2’ is entered, prompt for the length of sides: A and C, calculate the length of side: B
# 5. If ‘3’ is entered, prompt for the length of sides: A and B, calculate the length of side: C
 
# ** End **
