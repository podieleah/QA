# If, Elif and Else
# Allows for different pathways for our code to take
# Remember Order of Precedence - PEMDAS
# https://www.tutorialspoint.com/python/python_operator_precedence.htm

# my_bool = True
# if my_bool:
#     print("MyBool is True")
# else:
#     print("MyBool is False")


# is_admin = False
# is_verified = True
# on_holiday = False
# if (is_admin or is_verified) and not on_holiday:
#     print("access granted")
# else:
#     print("access denied")



# Operators
# https://www.w3schools.com/python/python_operators.asp

# equals to ==
# not equals to !=
# greater than >
# greater than or equal to >=
# less than <
# less than or equal to <=

# money = 10
# if money >= 10:
#     print("I have some money")
# else:
#     print("Not enough money")


#Elif statements 

# temp = 30
# if temp >= 30:
#     print("Its very hot")
# if temp > 25 and temp < 30:
#     print("Quite hot")
# if temp > 15 and temp < 25:
#     print("Its warm")
# if temp > 10 and temp < 15:
#     print("Get a coat")
# else: 
#     print("pretty bad")

# This is lenghty and requires more runtime as there are more statements for python to evaluate, instead use -

# temp = 16
# if temp >= 30:
#     print("Its very hot")
# elif temp > 25:
#     print("Quite hot")
# elif temp > 15:
#     print("Its warm")
# elif temp > 10:
#     print("Get a coat")
# else: 
#     print("pretty bad")

# Exercise
# User to input a grade/mark
# if the mark 85 and above - print distinction
# if between 65 and 84 - print pass
# anything else - print fail
# Use if, elif, else flow

# grade = int(input("Enter grade? "))
# if grade >= 85:
#     print("Distinction")
# elif grade >= 65:
#     print("Pass")
# else:
#     print("Fail")

# Multiple comparators

# deposit = 500
# password = "password1"

# if 0 < deposit < 100 and password == "password1":
#     print(f"Thank you for your deposit of £{deposit}")
# else: 
#     print("Deposit failed")

# Not
# The statements are false, so it is true that the statements are false, when a NOT is present.
# if not 0 < deposit < 100 and password != "password1":
#     print("Deposit Failed")
# else:
#     print("Thank you for your deposit")


# IN and NOT IN - used more for input validations
# Wrong way around, user should not be able to get through on the else statement.
# name = "root33"
# if name in ("root", "admin", "user"):
#     print("Invalid Username")
# else: 
#     print("Accepted")

# Makes more sense as uses the else statement as a catch all/error handling
# if name not in ("root", "admin", "user"):
#     print("User Accepted")
# else:
#     print("Invalid Username")

# Exercise
# Weight converter app
# User to input their weight
# User to select KGs or Lbs
# if statement to check the unit entered 
# logic to convert the weight (kgs to lbs or lbs to kgs)
# print out the converted value
# error handling for upper/lower case
# Optional - error handling for input validation.

# Exercise in a function
# def convert_weight():
#   weight = float(input("Enter your weight: "))
#   unit = input("Enter unit 'kg' or 'lbs': ").lower()
#   if unit == "kg":
#     weight_lbs = weight * 2.20462
#     print(f"{weight} kilograms is equal to {weight_lbs:.2f} pounds.")
#   elif unit == "lbs":
#     weight_kg = weight / 2.20462
#     print(f"{weight} pounds is equal to {weight_kg:.2f} kilograms.")
#   else:
#     print("Invalid unit. Please enter 'kg' or 'lbs'.")
# convert_weight()


# Not in a function
# weight = float(input("Enter your weight: "))
# unit = input("Enter your unit kg or lbs: ").lower()
# if unit == "kg":
#   weight_lbs = weight * 2.20462
#   print(f"{weight} kilograms is equal to {weight_lbs:.2f} pounds.")
# elif unit == "lbs":
#   weight_kg = weight / 2.20462
#   print(f"{weight} pounds is equal to {weight_kg:.2f} kilograms.")
# else:
#   print("Invalid unit. Please enter 'kg' or 'lbs'.")


# Exercise 2
# Rewrite without using if statements or an in built functions (no max)
# Highest number 

# num = 10
# num1 = 20
# if num > num1:
#   print(num)
# else: 
#   print(num1)

# Solution 1 -
# larger = num1 * (num > num1) + num1 * (num1 > num)
# print(larger)

# Solution 2 -
# result = num1 + (num - num1) * (num >= num1)
# print(result)




