#Object-oriented programming is one of the most effective approaches to writing software.
# In object-oriented programming you write classes that represent real-world things
# and situations, and you create objects based on these classes. 
# When you write a class, you define the general behavior that a whole category of objects can have.

# Making an object from a class is called instantiation, and you work with instances of a class.
#nb: capitalized names refer to classes in Python. A function that’s part of a class is a method. 
#Variables that are accessible through instances like this are called attributes.
#In object-oriented programming (OOP), an instance is a specific, individual object created from a class.
#A class is like a template or blueprint that defines what an object should look like and what it can do.

# Think of a class as a recipe, and each instance as a cake baked from that recipe. You can make many cakes
# (instances) from the same recipe (class), and each cake is its own separate object.


# A class is a blueprint — a plan that describes:
# what data (called attributes) the object will have, and
# what actions (called methods) it can do.

# For example.
# class Dog:
#     def __init__(self, name, color):
#         self.name = name     # attribute
#         self.color = color   # attribute

#     def bark(self):          # method
#         print("Woof woof!")

# Actually, a Class of anything can be created. 

# class Car:
# 	def __init__(self, brand, model, year):
# 		self.brand = brand
# 		self.model = model
# 		self.year = year
# ##these are these attributes of this car (more like xteristics). Next is to define the ACTION they do (method).
# 	def move(self):
# 		print('I like that car that just moved past us. The brand name is ' + self.brand + 
# 			' and model is ' + self.model + ', ' + str(self.year) + '.')

# # Creating instances
# car1 = Car("Toyota", "Camry", 2025)
# car2 = Car("Honda", "Accord", 2024)
# car3 = Car("Lexus", "IS350", 2026)

# # Accessing data
# print(car1)   
# print(car2)   
# print(car3) 

# # Calling a method
# car1.move() 
# car2.move() 
# car3.move() 



# class Model:
# 	def __init__(self, name, age, height, color):
# 		self.name = name
# 		self.age = age
# 		self.height = height
# 		self.color = color

# 	def career(self):
# 		print('This is ' + self.name.title() + '. She is ' + str(self.age) + ', ' + self.height + 
# 			' and ' + self.color + ' in complexion.')

# mod1 = Model('sheila', 20, '5.11', 'chocolate')
# mod2 = Model('nelly', 19, '6.0', 'fair')
# mod3 = Model('nen', 18, '6.1', 'dark')

# print(mod1)
# print(mod2)
# print(mod3)

# mod1.career()
# mod2.career()
# mod3.career()



# #Creating the Dog Class
# class Dog:
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def sit(self):
# 		print(self.name.title() + " is now sitting.")

# 	def roll_over(self):
# 		print(self.name.title() + " rolled over!")

# doggg = Dog("willie", 2)

# print(doggg)   

# doggg.sit() 
# doggg.roll_over() 


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


# DIY 9-2. 
# Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from 
# the class, and call describe_restaurant() for each instance.

# class Restaurant():
# 	def __init__(self, name, cuisine):
# 		self.name = name
# 		self.cuisine = cuisine
# 	def describe_restaurant(self): 
# 		print('This is ' + self.name.title() + '. Their main cuisine is ' + self.cuisine + '.')
# 	def open_restaurant(self):
# 		print(self.name.title() + ' is open for business today!')
# food1 = Restaurant('delly', 'plain white sauce')
# food2 = Restaurant('wholly', 'veg sauce')
# food3 = Restaurant('crunches', 'jollof sauce')

# print(food1)
# print(food2)
# print(food3)

# food1.describe_restaurant()
# food1.open_restaurant()

# food2.describe_restaurant()
# food2.open_restaurant()

# food3.describe_restaurant()
# food3.open_restaurant()


#DIY 
# 9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then 
# create several other attributes that are typically stored in a user profile. Make a method 
# called describe_user() that prints a summary of the user’s information. Make another method called
# greet_user() that prints a personalized greeting to the user. Create several instances representing 
# different users, and call both methods for each user.		

# class User():
# 	def __init__(self, first_name, last_name, user_name, age, dob, coutry ):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.user_name = user_name
# 		self.age = age
# 		self.dob = dob
# 		self.coutry = coutry
# 	def describe_user(self):
# 		print('My name is ' + self.first_name + self.last_name + ' aged, ' +  self.age + 
# 			'. I was born in ' + self.coutry + ' on ' + self.dob + '.')
# 	def greet_user(self):
# 		print('Hello ' + self.first_name + self.last_name + '...')

# use1 = User('gracious', 'pee', 'pshal', '28', '19th of Oct, 1910', 'Nigeria')
# use2 = User('ruth', 'ralph', 'rulph', '20', '9th of Aug, 1900','Canada')
# use3 = User('kay', 'glo', 'glokay', '30', '29th of Jan, 1800','NZ')

# print(use1)
# print(use2)
# print(use3)

# use1.describe_user()
# use1.greet_user()

# use2.describe_user()
# use2.greet_user()

# use3.describe_user()
# use3.greet_user()


# Setting a Default Value for an Attribute
# Every attribute in a class needs an initial value, even if that value is 0 or an empty string.
# An attribute can be given/assigned a default value. for example, 
# class User():
# 	def __init__(self, first_name, last_name, user_name, age, height, dob, coutry ):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.user_name = user_name
# 		self.age = age
# 		self.dob = dob
# 		self.coutry = coutry
#		self.height = 5

# Modifying Attribute Values
# You can change an attribute’s value in three ways: you can change the value directly through an instance,
# set the value through a method, or increment the value (add a certain amount to it) through a method. 
# Let’s look at each of these approaches. The simplest way to modify the value of an attribute is to access
# the attribute directly through an instance.

#DIY
# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166). Add an attribute called 
# number_served with a default value of 0. Create an instance called restaurant from this class. 
# Print the number of customers the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of customers that have been served. 
# Call this method with a new number and print the value again. Add a method called 
# increment_number_served() that lets you increment the number of customers who’ve been served. 
# Call this method with any number you like that could represent how many customers were served in, say, 
# a day of business.

#DIY 9-4
# class Restaurant():
#  	def __init__(self, name, cuisine):
#  		self.name = name
#  		self.cuisine = cuisine
# 		self.number_served = 0	
#  	def describe_restaurant(self): 
#  		print('This is ' + self.name.title() + '. Their main cuisine is ' + self.cuisine + '.')
#  	def open_restaurant(self):
# 		print(self.name.title() + ' is open for business today!')

# """changing the attribute directly"""
# self.new_number_served = 20

# food = Restaurant('delly', 'plain white sauce')
# print(food)
# print(self.name  + 'has served 25 customers today!' )

# food.describe_restaurant()
# food.open_restaurant()


"""DIY 9-5. Login Attempts: Add an attribute called login_attempts to your User class from 
Exercise 9-3 (page 166). Write a method called increment_login_attempts() that increments the value 
of login_attempts by 1. Write another method called reset_login_attempts() that resets the value 
of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and then call 
reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.