# != not equal to
# = assigns a value to a variable
# == asks/checks if the value of something is true/false 

# cars = ['toyota', 'honda', 'lexus', 'mb', 'bmw', 'hyundai']
# for car in cars:
# 	if car == 'bmw':  #whenever car is bmw, print it in uppercase
# 		print(car.upper())
# 	if car == 'mb':   #whenever car is mb, print it in prrercase
# 		print(car.upper())
# 	else:
# 		print(car.title())	

# 	if car != 'telsa':
# 		print("I'll like to checkout telsa too!")

# for car in cars:
#  if car == 'bmw':
# print(car.upper())
# else:
# print(car.title())

# To check whether two conditions are both True simultaneously, use the keyword
# and to combine the two conditional tests; if each test passes, the overall
# expression evaluates to True. If either test fails or if both tests fail, the
# expression evaluates to False.

# age_0 = 22
# age_1 = 18
# age_0 >= 21 and age_1 >= 21
# False
# age_1 = 22
# age_0 >= 21 and age_1 >= 21
# True

# The keyword or allows you to check multiple conditions as well, but it
# passes when either or both of the individual tests pass. An or expression
# fails only when both individual tests fail.

# age_0 = 22
# age_1 = 18
# age_0 >= 21 or age_1 >= 21
# True
# age_0 = 18
# age_0 >= 21 or age_1 >= 21
# False

# To find out whether a particular value is already in a list, use the keyword
# in.
# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# 'mushrooms' in requested_toppings
# True
# 'pepperoni' in requested_toppings
# False


# To know if a value does not appear in a list. You can use the keyword not. 
# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'
# if user not in banned_users:
# print(user.title() + ", you can post a response if you wish.")


#DIY: You don’t have to limit the number of tests you create to 10. 
# If you want to try more comparisons, write more tests and add them to conditional_tests.py. 
# Have at least one True and one False result for each of the following:
# • Tests for equality and inequality with strings
# soup = 'nsala'
# if soup == 'oha':
# 	print("Aye, I want!")
# else:
# 	print('oh no!')

# game = 'soccer'
# if game != 'tennis':
# 	print("I'm in!")
# else:
# 	print("I don't want soccer please")

# • Tests using the lower() function
# name = 'Ifunanya'
# name.lower() == 'ifunanya'

# • Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to.
# age = 30
# age < 30
# age > 30
# age <= 30
# age >= 30

# • Tests using the and keyword and the or keyword
# meemma = 18
# mama = 17
# if meemma >= 18 and mama <= 18:
# 	print('yes! they are eligible to vote.')

# meemma = 18
# mama = 17
# if meemma < 18 or mama >= 18:
# 	print('yes! they are eligible to vote.')

# • Test whether an item is in a list
#oha_soup = ['stockfish', 'dryfish', 'tozo', 'ogiri']
# if 'kpomo' in oha_soup:
# 	print('Does the kpomo have fat?')
# 'tozo' in oha_soup
# if 'tozo' in oha_soup:
# 	print('Does the kpomo have fat?')
# • Test whether an item is not in a list
# if 'crayfish' not in oha_soup:
# 	print('please add crayfish')


#if-elif-else chain: works when only one test passes. it’s only appropriate to use when you
# just need one test to pass. As soon as Python finds one test that passes, it
# skips the rest of the tests.
#a series of simple if statements with no elif or else blocks check all of the conditions of
#interest. In this case, you should use a series of simple if statements with no
#elif or else blocks.

#DIY: Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# alien_color = ['green', 'yellow','red']

# • Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points.

# if alien_color == 'green':
# 	print('Josh just earned 5 points!')

# • Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)
# if alien_color == 'black':
# 	print("Oh, that's null!")
# else:
# 	print('He won extra points!')

# Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
# write an if-else chain.

# alien_color = ['blue', 'yellow', 'black', 'green']
# if alien_color == 'white':
# 	print("oh didn't know aliens could be white")
# elif 'black' in alien_color:
# 	print("omg, must be scary!")
# else:
# 	print("I really do not wish to see an alien")

# • If the alien’s color is green, print a statement that the player just earned
# 5 points for shooting the alien.
# if 'green' in alien_color:
# 	print("I just scored 5 points for shooting thr alien!")
# else:
# 	print("Nothing!")

# • If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.
# if 'brown' not in alien_color:
# 	print("That's 10 points!")
# • Write one version of this program that runs the if block and another that
# runs the else block.


#DIY
# Stages of Life: Write an if-elif-else chain that determines a person’s
# stage of life. Set a value for the variable age, and then:
# age = 30 
# # • If the person is less than 2 years old, print a message that the person is
# # a baby.
# if age < 2:
# 	print('He is a baby')
# # • If the person is at least 2 years old but less than 4, print a message that
# # the person is a toddler.
# elif age >= 2:
# 	print('He is toddler')
# # • If the person is at least 4 years old but less than 13, print a message that
# # the person is a kid.
# elif age >= 13:
# 	print('He is a kid')

# • If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager.
# elif age <=20:
# 	print('He is a teenager')
# • If the person is at least 20 years old but less than 65, print a message that
# the person is an adult.
# elif age < 65:
# 	print('He is an adult')
# • If the person is age 65 or older, print a message that the person is an
# elder.
# elif age >= 65:
# 	print('He is an elder')
# else:
# 	print("Well, that's stages of life!")


#DIY: Make a list of five or more usernames, including the name 'admin'. 
# users = ['shal', 'admin', 'josh', 'joel', 'nazo']

# Imagine you are writing code that will print a greeting to each user after
# they log in to a website. Loop through the list, and print a greeting to each user:
# for user in users:
# 	print(user.title() + ", you're welcome back!")

# • If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# for user in users:
# 	if user == 'admin':
# 		print("Hello admin, would you like to see a status report?")
# • Otherwise, print a generic greeting, such as Hello Eric, thank you for logging
# in again.
# else:
# 	print("Hello " + user + ", thanking you for loggin back in again.")

# No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# users = []
# if users:
# 	else:
# 	print("Not sure if you're registered")
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct
# message is printed.
# Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.

#current_users = ['shal', 'admin', 'josh', 'joel', 'nazo']

# • Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.

#new_users = ['sommy', 'admin', 'josh', 'nen', 'nazo']

# • Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.

# for new_user in new_users:
# 	if new_user in current_users:
# 		print("The username is in use, choose another username")
# else:
# 	print("The username is available")
# • Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted.

# Ordinal Numbers: Ordinal numbers indicate their position in a list, such
# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# • Store the numbers 1 through 9 in a list.
# • Loop through the list.
# • Use an if-elif-else chain inside the loop to print the proper ordinal ending
# for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
# 7th 8th 9th", and each result should be on a separate line.	

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
	if number == 1:
		print(number "+ st")
	if number == 2:
		print(number "+ nd")
	if number == 3:
		print(number "+ rd")
# else:
# 	print(number + 'th')		