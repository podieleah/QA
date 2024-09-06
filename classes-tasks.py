# to -do:
# classes lab
# extra classes challenges 
# rps as a class - on rock_paper_scissors.py
# optional bookshelf challenges

#1. Create a Rectangle class with attributes length and width. 
#Add methods to calculate the area and perimeter of the rectangle. 

class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def calculate_area(self):
    return self.length * self.width

  def calculate_perimeter(self):
    return 2 * (self.length + self.width)

rectangle = Rectangle(5, 3)
area = rectangle.calculate_area()
print("Area: ", area)

perimeter = rectangle.calculate_perimeter()
print("Perimeter: ", perimeter)

#2. Create a BankAccount class with attributes account_number and balance. 
#Add methods to deposit and withdraw money from the account. 

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
       if amount > 0:
          self.balance += amount
          print(f"Deposited £{amount}. New balance: £{self.balance}")
       else:
          print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
       if amount > 0 and amount <= self.balance:
          self.balance -= amount
          print(f"Withdrew £{amount}. New balance £{self.balance}")
       elif amount <= 0:
          print("Invalid withdrawal amount. Amount must be greater than 0.")
       else:
          print("Insufficient funds.")

account = BankAccount("12345678", 200)
account.deposit(800)
account.withdraw(500)


#3. Create a Car class with attributes make, model, and year. 
#Add methods to get and set the values of the attributes. 

class Car:
    def __init__(self, make, model, year):
      self.make = make
      self.model = model
      self.year = year

    def get_make(self):
      return self.make
    
    def set_make(self, make):
       self.make = make

    def get_model(self):
       return self.model
    
    def set_model(self, model):
       self.model = model
    
    def get_year(self):
       return self.year
    
    def set_year(self, year):
       self.year = year
    
my_car = Car("BMW", "3 Series", 2022)
my_car.set_make("BMW")
my_car.set_model("X5")
my_car.set_year(2023)

print(my_car.get_make())
print(my_car.get_model())
print(my_car.get_year())
      

#4. Create a Product class with attributes name, price, and quantity. 
#Add methods to calculate the total value of the product (price * quantity) 
#and add or remove items from the product inventory. 



#Harder challenge (stretch goal): 

#Create a Book class and BookShelf class that can be used to manage a collection of books. 
#Create a Book class that has the following attributes: 
#title (str), author (str), publisher (str), publication year (int). 
#The class should also have a str method that returns the book's information in a 
#formatted string. 
#Create a BookShelf class that has the following attributes: 
#capacity (int), list of books (list). 
#The class should have the following methods: 
#- add_book: adds a book to the list of books if the shelf is not full 
#- remove_book: removes a book from the list of books if it exists on the shelf 
#- find_book_by_title: searches for a book by its title 
#and returns the book object if found 
#- find_books_by_author: searches for books by a specific author 
#and returns a list of book objects if found 
#The class should also have a str method that returns a string representation 
#of the books on the shelf. 

#Create four Book objects and add them to a BookShelf object with a capacity of three. 
#Test the BookShelf object by adding, removing, and finding books by title and author.
#Print the BookShelf object after each action.