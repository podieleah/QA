# Task 1

# Sqaures

i = 1
while i <= 100:
  square = i ** 2
  print(f"Number: {i}, Square: {square}")
  if square >= 2000:
    break
  i += 1

# Factorial

number = int(input("Enter an number: "))
factorial = 1
i = 1
while i <= number:
  factorial *= i
  i += 1
print(f"The factorial of {number} is {factorial}")

# Investment

initial_investment = 100
target_value = 1000
interest_rate = 0.1
years = 0
current_value = initial_investment

while current_value < target_value:
  current_value *= (1 + interest_rate)
  years += 1
print(f"It will take {years} years for the investment to reach £{target_value}.")

# Input an integer between two limits

min_value = 1
max_value = 100
attempts = 0

while attempts < 3:
  try:
    number = int(input(f"Enter an integer between {min_value} and {max_value}: "))
    if min_value <= number <= max_value:
      print(f"You entered: {number}")
      break
    else:
      print("Invalid input. Please enter a number between 1 and 100.")
      attempts += 1
  except ValueError:
    print("Invalid input. Please enter an integer.")
    attempts += 1

if attempts == 3:
  print("None")

# Vowels

word = input("Enter a word: ")
vowels = "aeiou"
count = 0
i = 0

while i < len(word):
  if word[i].lower() in vowels:
    count += 1
  i += 1

print(f"The number of vowels in '{word}' is {count}")


# Average Exam Mark 

while True:
  math_mark = int(input("Enter Math mark (0-100): "))
  if 0 <= math_mark <= 100:
    break
  else:
    print("Invalid mark. Please enter a number between 0 and 100.")

while True:
  english_mark = int(input("Enter English mark (0-100): "))
  if 0 <= english_mark <= 100:
    break
  else:
    print("Invalid mark. Please enter a number between 0 and 100.")

while True:
  ict_mark = int(input("Enter ICT mark (0-100): "))
  if 0 <= ict_mark <= 100:
    break
  else:
    print("Invalid mark. Please enter a number between 0 and 100.")

average_mark = (math_mark + english_mark + ict_mark) / 3

if average_mark >= 65:
  result = "Pass"
else:
  result = "Fail"

print("Average mark:", average_mark)
print("Overall result:", result)