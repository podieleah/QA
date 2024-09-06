# classes is part of OOP (object orientated programming)
# key concepts:
# class - a blueprint - of attributes (vars/args) and methods (functions)
# object - is an instance of a class.
# allows us to make multiple objects of the same type. 

#class Dog:
  #  energy = "high" # setting an attribute of the class. 

 #   def speak(self):
 #       print("bark")


#fido = Dog() # initiales the object of the class

#fido.speak() # calling a method

#print(fido.energy)
#fido.energy = "low" # changing value for an attribute. 

#print(fido.energy)

#class Students():
#    pass

#student1 = Students()
#student2 = Students()

#student1.first = "john"
#student1.last = "smith"
#student1.age = 10

#print(student1.age, student1.last)

#class Students:
#    def __init__(self, first, last, age): # init method, called a dunder, signifies a background task. 
#        self.first = first # init method initialsies the object with these values.
#        self.last = last # the self param refers to the object itself.
#        self.age = age # self maps the class data to the object.  


#student1 = Students("john", "smith", 10)
#student2 = Students("katie", "smith", 12)

#print(student1.age, student2.age)


#class Students:
 #   def __init__(self, first, last, age): # init method, called a dunder, signifies a background task. 
 #       self.first = first # init method initialsies the object with these values.
 #       self.last = last # the self param refers to the object itself.
 #       self.age = age # self maps the class data to the object. 
 #       self.full = first + " " + last  


#student1 = Students("john", "smith", 10)
#student2 = Students("katie", "smith", 12)

#print(student1.full, student2.full)


#class Students:
    #def __init__(self, first, last, age): # init method, called a dunder, signifies a background task. 
   #     self.first = first # init method initialsies the object with these values.
   #     self.last = last # the self param refers to the object itself.
  #      self.age = age # self maps the class data to the object. 
  #      self.full = first + " " + last  

 #   def fullname(self):
 #       return self.first + " " + self.last

#student1 = Students("john", "smith", 10)
#student2 = Students("katie", "smith", 12)

#print(student1.fullname())
#print(Students.fullname(student2))


# change an attribute with a method

#class Students:
  #  def __init__(self, first, last, age): # init method, called a dunder, signifies a background task. 
   ##     self.first = first # init method initialsies the object with these values.
  #      self.last = last # the self param refers to the object itself.
   #     self.age = age # self maps the class data to the object. 
  #      self.full = first + " " + last  

 #   def fullname(self):
 #       return self.first + " " + self.last

 #   def change_age(self):
 #       self.age = self.age + 1

#student1 = Students("john", "smith", 10)
#student2 = Students("katie", "smith", 12)

#student1.change_age()
#Students.change_age(student2)

#print(student1.age, student2.age)

# self class variable -  a var the objetcs will use. 

#class Students:
    
    #age_increase_amount = 25

    #def __init__(self, first, last, age): # init method, called a dunder, signifies a background task. 
       # self.first = first # init method initialsies the object with these values.
       # self.last = last # the self param refers to the object itself.
      #  self.age = age # self maps the class data to the object. 
     #   self.full = first + " " + last  

    #def fullname(self):
     #   return self.first + " " + self.last

    #def change_age(self):
        #self.age = self.age + self.age_increase_amount

#student1 = Students("john", "smith", 10)
#student2 = Students("katie", "smith", 12)

#print(student1.age)
#student1.change_age()
#print(student1.age)

#print(student1.age_increase_amount)
#print(student2.age_increase_amount)

# __dict__

#print(student1.__dict__)
#print(student2.__dict__)
#print(Students.__dict__)

# change to the variable

#student1.age_increase_amount = 10
#print(student1.__dict__)
#print(student2.__dict__)

#student1.change_age()
#student2.change_age()

#print(student1.age, student2.age)

# non self class variable - not for the object to use.

#class Students:
    
   # age_increase_amount = 25
   # num_of_students = 0

    #def __init__(self, first, last, age): # init method, called a dunder, signifies a background task. 
       # self.first = first # init method initialsies the object with these values.
      #  self.last = last # the self param refers to the object itself.
     #   self.age = age # self maps the class data to the object. 
    #    self.full = first + " " + last  

   #     Students.num_of_students += 1

  #  def fullname(self):
  #      return self.first + " " + self.last

 #   def change_age(self):
 #       self.age = self.age + self.age_increase_amount


#print(Students.num_of_students)
#student1 = Students("2", "2", 2)
#student2 = Students("2", "2", 2)
#print(Students.num_of_students)

# parent child classes.

#class Animal: # this will be our parent class
   # def __init__(self, name, species):
  #      self.name = name
  #      self.species = species

 #   def eat(self):
 #       print(f"{self.name} is eating")

#class Cat(Animal):
  #  def __init__(self, name, species, breed):
  #      super().__init__(name, species)
  #      self.breed = breed
    
 #   def meow(self):
 #       print("meow")

#my_cat = Cat("w", "w", "w")

#my_cat.eat()
#my_cat.meow()

#print(my_cat)

# with a str method

class Animal: # this will be our parent class
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

    def __str__(self):
        return f"{self.name} - {self.species} - {self.__class__.__name__}"

class Cat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
    
    def meow(self):
        print("meow")

    def __str__(self):
        return super().__str__() + f"- {self.breed}"


my_cat = Cat("name", "species", "breed")

print(my_cat)