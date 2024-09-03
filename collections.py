# Collections are our complex data types.
# Different ways of storing our data.
#
# Lists - ordered(indexed), mutable, collection of values -
# [a{index position 0}, b{index position 1}, c{index position 2/-1}]
#
# Dictionaries - unordered(no index positions, keys are unique), mutable, collection of key:pair values -
# {key: value, key1: value key2: value}
#
# Tuples - ordered, immutable (can't be changed), collection of values (a, b, c)
# or no brackets at all. x = 1, 2, 3
#
# Sets - unordered, mutable, collection of unique values - {a, b, c}
#
#
# Lists: 
# lists are stored in []
# colours = ["blue", "red", "yellow", "orange"]
# print(colours)

# Direct Access
# print(colours[0])
# print(colours[3])
# print(colours[-2])

# Slicing:
# Create a sub list up to but not including the 2nd number
# print(colours[0:2]) # blue and red
# print(colours[1: ]) # no second number slices to the end

# Altering a list with direct access
# food = ["rice", "pasta", "apple", "bread"]
# print(food)
# food[0] = "pizza" # change rice to pizza
# print(food)
# del food[1] # deletes pasta from the list 
# print(food)

# Nested Lists
# numbers = [1, 2, 3, 4]
# letters = ["a", "b", "c", "d"]

# combined = [numbers, letters]
# print(combined[0][1], combined[1][1])

# String Methods 
# https://www.w3schools.com/python/python_ref_string.asp

# Append 
# Adds to the end of the list
# my_fruits = ["apple", "orange", "pear"]
# my_fruits.append("strawberries")
# print(my_fruits)
# ['apple', 'orange', 'pear', 'strawberries']

# Remove - 
# my_fruits = ["apple", "orange", "pear"]
# my_fruits.remove("apple")
# print(my_fruits)
# ['orange', 'pear']

# Insert
# my_fruits = ["apple", "orange", "pear"]
# my_fruits.insert(0, "mango")
# print (my_fruits)
# ['mango', 'apple', 'orange', 'pear']
# my_fruits.insert(0, "grapes")
# print (my_fruits)
# ['grapes', 'mango', 'apple', 'orange', 'pear']

# Extend
# my_fruits = ["apple", "orange", "pear"]
# my_fruits.extend(["melon", "blueberry"])
# print(my_fruits)
# ['apple', 'orange', 'pear', 'melon', 'blueberry']

# Reverse 
# my_fruits.reverse()
# print(my_fruits)
# ['blueberry', 'melon', 'pear', 'orange', 'apple']

# Sort
# my_fruits.sort()
# print(my_fruits)

# Join
# x = "#".join(my_fruits)#
# print(x)

# Dictionaries
# {} key:value pairs

# No indexing. 
# keys unique values can be anything.
# drinks = {"fizzy": "sprite", "still": "water", "juice": "orange", "alcoholic": "wine"}
# print(drinks)

# Direct Access
# print(drinks["still"])
# drinks["non-alcohlic"] = "water"
# print(drinks)
# drinks["non-alcohlic"] = "squash"
# print(drinks)

# Methods
# Values/Keys/Items
# print(drinks.values())
# print(drinks.keys())
# print(drinks.items())

# Get method
# print(drinks.get("still"))
# print(drinks.get("stille"))
# print(drinks.get("stille", "not-found"))

# Update 
# drinks.update({"sugery": "cola"})
# print(drinks)

# Pop
# print(drinks.pop("non-alcohlic"))
# print(drinks)

# Exercise
# authors = {
#     "Marian Keyes": ["Rachels Holiday", "Watermelon", "The Break"],
#     "Charles Dickens": ["Great Expectations", "Oliver Twist", "A Christmas Carol"],
#     "Stephen King": ["It", "The Shining", "The Stand"]
# }

# author_name = input("Enter an author name: ")
# books = authors.get(author_name, "Author not found")
# print(f"{author_name}'s books; {', '.join(books)}")

# Tuples
# Similar to lists but immutable
# Slighty quicker and uses slightly less memory
# Use () or no brackets at all 
# Methods available are count() and index()
# Built in functions also like zip, max, len ,min etc...

# rectangle = 10, 5

# Sets
# https://www.w3schools.com/python/python_ref_set.asp
# No index, unique values 

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union - Combines sets removes duplicates
# print(set1.union(set2))
# outcome {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection - Returns a set, that is the intersection of two other sets
# print(set1.intersection(set2))
# outcome {4, 5}

# Difference - Returns a set containing the difference between two or more sets
# print(set1.difference(set2))
# outcome - {1, 2, 3}

# Symmetrical difference - Returns a set with the symmetric differences of two sets
# print(set1.symmetric_difference(set2))
# outcome {1, 2, 3, 6, 7, 8}