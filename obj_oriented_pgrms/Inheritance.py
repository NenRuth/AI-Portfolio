"""Inheritance means a class can “inherit” or reuse attributes and methods from another class.
Real-Life Analogy
Think of a Parent–Child relationship:
The Parent (base class) has some characteristics (e.g. eyes, height).
The Child (subclass) inherits those automatically (no need to rewrite them).
The child can also have extra features or behave differently.



#Create a Parent Class (base class)"""
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print("My name is " + self.name + " and I am " + str(self.age) + " years old.")


# #Create a subclass
# class Student(Person):
#     def __init__(self, name, age, grade):
#         # Call the parent class constructor using super()
#         super().__init__(name, age)
#         self.grade = grade

#     def study(self):
#         print(self.name + " is studying for grade " + str(self.grade) + ".")

# #Create Instances
# p1 = Person("Mrs. Obi", 40)
# s1 = Student("Ada", 14, 8)


#Use the Methods
# p1.introduce()  
# s1.introduce()   # This is so cos it can use info inherited from p1
# s1.study()       


#Overriding Methods from the Parent Class: If the child wants to change how something works, 
#it can override it. To do this, you define a method in the child class with the same name as the
#method you want to override in the parent class.

# class Student(Person):
#     def introduce(self):
#         print(f"My name is {self.name}, I'm {self.age}, and I’m a student!")
# s1.introduce()


#multiple subclass
# class Vehicle:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def start_engine(self):
#         print("The " + self.brand + self.model + "engine has started.")

#     def stop_engine(self):
#         print(f"The {self.brand} {self.model} engine has stopped.")


# class Car(Vehicle):   #inherits from Vehicle with an additional attribute, door.
#     def __init__(self, brand, model, year, doors):
#         super().__init__(brand, model, year)  # collects attributes from parent class
#         self.doors = doors

#     def open_trunk(self):
#         print("The trunk of the " + self.brand + self.model  + "is now open.")


# class Bus(Vehicle):  #with an additional attribute, capacity.
#     def __init__(self, brand, model, year, capacity):
#         super().__init__(brand, model, year)
#         self.capacity = capacity

#     def pick_passengers(self):
#         print(f"The {self.brand} {self.model} is picking up {self.capacity} passengers.")


# class Motorcycle(Vehicle):
#     def __init__(self, brand, model, year, has_sidecar):
#         super().__init__(brand, model, year)
#         self.has_sidecar = has_sidecar

#     def wheelie(self):
#         print(f"The {self.brand} {self.model} does a wheelie!")


# #Creating Instances (Objects)
# car1 = Car("Toyota", "Camry", 2022, 4)
# bus1 = Bus("Mercedes", "Sprinter", 2021, 20)
# bike1 = Motorcycle("Yamaha", "R1", 2023, False)


# #Calling Methods
# car1.start_engine()      # Inherited from Vehicle
# car1.open_trunk()        # From Car

# bus1.start_engine()      # Inherited from Vehicle
# bus1.pick_passengers()   # From Bus

# bike1.start_engine()     # Inherited from Vehicle
# bike1.wheelie()          # From Motorcycle



#Instances as Attributes
#this is when an instance of one class is used as an attribute (i.e., a property) inside another class.
#This is called Composition — where one class is made up of other classes. It’s different from inheritance.

# class Address:
#     def __init__(self, city, country):
#         self.city = city
#         self.country = country

#     def show_address(self):
#         print(f"{self.city}, {self.country}")


# class Student:
#     def __init__(self, name, age, city, country):
#         self.name = name
#         self.age = age
#         self.address = Address(city, country)  # instance as attribute

#     def show_details(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#         print("Address:", end=" ")
#         self.address.show_address()

# # Create instance
# student1 = Student('Ruth', 22, 'Lagos', 'Nigeria')
# student1.show_details()

# You can access nested attributes like:
# student1.address.city  # returns 'Lagos'



#Importing Classes 
#(Import specific classes)
# class IceCreamStand:
#     def __init__(self, name, cuisine, flavors):
#         self.name = name
#         self.cuisine = cuisine
#         self.flavors = flavors

#     def display_flavors(self):
#         print("Available flavors:")
#         for flavor in self.flavors:
#             print("-", flavor) #isn’t doing anything “special” in Python — it’s just a string used for formatting (to make the printed list look neat).

# from ice_cream_stand import IceCreamStand #(this line will import data/codes in the ice_cream_stand.py file. So a file must be stored/saved in this name for it to work)

#Create an instance
# my_stand = IceCreamStand("Cool Treats", "ice cream", ["mango", "lemon", "cookie dough"])

# #Call the method
# my_stand.display_flavors()


# #Import multiple classes
# from ice_cream_stand import Restaurant, IceCreamStand

# restaurant = Restaurant("Mama's Kitchen", "Nigerian dishes")
# restaurant.describe_restaurant()

# my_stand = IceCreamStand("Cool Treats", "ice cream", ["vanilla", "mint"])
# my_stand.display_flavors()


# Importing the whole module
# means you bring in the entire file — all its classes, functions, and variables — and refer to them 
# using the module’s name.
# So instead of:
# from ice_cream_stand import IceCreamStand
# you do:
# import ice_cream_stand

# class IceCreamStand:
#     def __init__(self, name, cuisine, flavors):
#         self.name = name
#         self.cuisine = cuisine
#         self.flavors = flavors

#     def display_flavors(self):
#         print("Available flavors:")
#         for flavor in self.flavors:
#             print("-", flavor)
# import ice_cream_stand   # importing the whole module

# #creating instance
# my_stand = ice_cream_stand.IceCreamStand("Cool Treats", "ice cream", ["vanilla", "mango", "strawberry"])
# #calling method
# my_stand.display_flavors()


#DIY
# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store 
# two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() 
# that prints these two pieces of information, and a method called open_restaurant() that prints a message
# indicating that the restaurant is open. Make an instance called restaurant from your class. Print the 
# two attributes individually, and then call both methods.

# 9-1
# class Restaurant():
# 	def __init__(self, name, cuisine):
# 		self.name = name
# 		self.cuisine = cuisine
# 	def describe_restaurant(self): 
# 		print('This is ' + self.name.title() + '. Their main cuisine is ' + self.cuisine + '.')
# 	def open_restaurant(self):
# 		print(self.name.title() + ' is open for business today!')
# food = Restaurant('delly', 'plain white sauce')
# print(food)

# food.describe_restaurant()
# food.open_restaurant()


""" DIY 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called 
IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166) 
or Exercise 9-4 (page 171). Either version of the class will work; just pick the one you like better. 
Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method."""


# class IceCreamStand(Restaurant):
# 	def __init__(self, name, cuisine):
#     	super().__init__(name, cuisine)
#     	self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint', 'cookies and cream']

#     def display_flavors(self):
#         print('\n', self.name + 'offers the following flavors:')
#         for flavor in self.flavors:
#             print(flavor.title())

# # Create an instance  
# my_icecream_stand = IceCreamStand("Cool Treats", "ice cream")
# print(my_icecream_stand)

# #call the method
# my_icecream_stand.describe_restaurant()
# my_icecream_stand.display_flavors()  		


"""DIY 9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits 
from the User class you wrote in Exercise 9-3 (page 166) or Exercise 9-5 (page 171). Add an attribute, 
privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so 
on. Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method."""

# class User():
# 	def __init__(self, first_name, last_name, user_name, age, dob, coutry ):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.user_name = user_name
# 		self.age = age
# 		self.dob = dob
# 		self.coutry = coutry
# 	def describe_user(self):
# 		print('My name is ' + self.first_name + self.last_name + ',' + ' aged ' +  self.age + 
# 			'. I was born in ' + self.coutry + ' on ' + self.dob + '.')
# 	def greet_user(self):
# 		print('Hello ' + self.first_name + self.last_name + '...')

# class Admin(User):
#     def __init__(self, first_name, last_name, user_name, age, dob, coutry ):
#         super().__init__(first_name, last_name, user_name, age, dob, coutry)
#         self.privileges = ['can add post','can delete post','can ban user']


#     def show_privileges(self):
#         print('\nWelcome ' + self.first_name + self.last_name + ', these are the things you have access to:')
#         for privilege in self.privileges:
#             print('\n',privilege)

# #Creating an instance of Admin
# new_admin = Admin('kay', 'glo', 'glokay', '30', '29th of Jan, 1800','NZ')

# #call your method
# new_admin.describe_user()
# new_admin.show_privileges()


"""DIY 9-8. 
Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that 
stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. 
Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use 
your method to show its privileges."""

# Base class
# class User():
#   def __init__(self, first_name, last_name, user_name, age, dob, coutry ):
#       self.first_name = first_name
#       self.last_name = last_name
#       self.user_name = user_name
#       self.age = age
#       self.dob = dob
#       self.coutry = coutry
#   def describe_user(self):
#       print('My name is ' + self.first_name + self.last_name + ',' + ' aged ' +  self.age + 
#           '. I was born in ' + self.coutry + ' on ' + self.dob + '.')
#   def greet_user(self):
#       print('Hello ' + self.first_name + self.last_name + '...')

# class Admin(User):
#     def __init__(self, first_name, last_name, user_name, age, dob, coutry ):
#         super().__init__(first_name, last_name, user_name, age, dob, coutry)
#         self.privileges = Privileges(['can add post','can delete post','can ban user'])

# # Privileges class
# class Privileges:
#     def __init__(self, privileges=[]):
#         self.privileges = privileges

#     def show_privileges(self):
#         print("Privileges:")
#         for privilege in self.privileges:
#             print("-", privilege)

# # # Create an Admin instance
# admin_user = Admin("Ruth", "Shalem", "ruth_s", "30", "June 12, 1995", "Nigeria")

# # # Call the show_privileges method (through the Privileges instance)
# admin_user.privileges.show_privileges()
