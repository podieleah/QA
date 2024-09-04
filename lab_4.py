# Part 1

ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

#1
length_of_ages = len(ages)
print("Length of ages list: ", length_of_ages)

#2
for age in ages:
    print("Ages: ", age)

#3
new_ages = []

for i in range(len(ages)):
  new_age = ages[i] + 1
  new_ages.append(new_age)

for age in new_ages:
  print("Updated ages:", age)

#4
valid_ages = []

for i in range(len(ages)):
  age = ages[i]
  if 16 <= age <= 65:
    valid_ages.append(age)

for i in range(len(ages) - 1, -1, -1):
  if ages[i] < 16 or ages[i] > 65:
    del ages[i]

print("Updated ages: ")
for age in ages:
  print(age)

#5
count_16_25 = 0

for age in ages:
  if 16 <= age <= 25:
    count_16_25 += 1

print("Count of 16-25 year olds: ", count_16_25)

#6
ages.sort()
for age in ages:
  print("Sorted ages: ", age)

#7
total_ages = len(ages)
print(f"Proportion of ages between 16 and 25: {count_16_25 / total_ages:.2%}")



# Part 2
# Similar to task in lab 3 but this time using an "in" keywork instead of the len method 

word = input("Enter a word: ")
vowels = "aeiou"
count = 0

for char in word:
  if char.lower() in vowels:
    count += 1

print(f"The number of vowels in '{word}' is {count}")