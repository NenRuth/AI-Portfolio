# How the input() Function Works:
# The input() function pauses your program and waits for the user to enter
# some text. Once Python receives the user’s input, it stores it in a variable to
# make it convenient for you to work with.

# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print("Hello, " + name + "!")

#When you use the input() function, Python interprets everything the user enters as a string

#using int()
# The int() function converts a string representation of a number to a numerical representation.
# for example:
# age = input("How old are you? ")
# How old are you? 21
# age = int(age)
# age >= 18
# True

#How to you use the int() function in an actual program

# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 36:
# 	print("\nYou're tall enough to ride!")
# else:
# 	print("\nYou'll be able to ride when you're a little older.")


# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
# 	print("\nThe number " + str(number) + " is even.")
# else:
# 	print("\nThe number " + str(number) + " is odd.")

#while Loops
# The for loop takes a collection of items and executes a block of code ONCE for each item in the collection. 
# In contrast, the while loop RUNS as long as, or while, a CERTAIN CONDITION IS TRUE.

# current_number = 1
# while current_number <= 5:
# 	#print(current_number)

# current_number = 6
# if current_number <= 5:
# 	print(current_number)
# else:
# 	print("That isn't correct")

#current_number += 1. (The += operator is shorthand for current_number = current_number + 1.)

# current_number = 1
# while current_number <= 5:
# 	print(current_number)
# current_number += 1


#Letting the User choose when to Quit
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = " "
# while message != 'quit':
# 	message = input(prompt)
# 	print(message)

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = " "
# while message != 'quit':
# 	message = input(prompt)
# if message != 'quit':
# 	print(message)

#Using break to Exit a Loop. The break is used to exit a loop entirely. 
# prompt = "\nPlease enter the name of a city you have visited: "
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
# 	city = input(prompt)
# 	if city == 'quit':
# 		break
# 	else:
# 		print("I'd love to go to " + city.title() + "!")

#Using a Flag


#Using continue in a Loop: the continue statement to return to the beginning of the loop 
#(instead of breaking out of it entirely) based on the result of a conditional test.
# current_number = 0
# while current_number < 10:
# 	current_number += 1
# 	if current_number % 2 == 0:
# 		continue
# 	print(current_number)

# explanation: the count is increased by 1 so current_number is 1. 
# The if statement checks the modulo of current_number and 2. 
# If the modulo is 0 (which means current_number is divisible by 2), 
# the continue statement tells Python to ignore the rest of
# the loop and return to the beginning. If the current number is not divisible
# by 2, the rest of the loop is executed and Python prints the current
# number.

#Avoiding Infinite Loops
# x = 1
# while x <= 5:
# 	print(x)
# 	x += 1

# DIY
# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.
# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.
# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.
# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
# ctrl-C or close the window displaying the output.

#7.4
# pizza_toppings = "\ncheese, carbbage, hotdog, carrot, tomato_ketchup."
# pizza_toppings += "\nI’ll add these toppings to your pizza. "

# message = " "
# while message != 'quit':
# 	message = input(pizza_toppings)
# 	if message != 'quit':
# 		print(message)

# 7-5
#MovieTickets
#age = input("How old are you? ")
# age = 12
# if age < 3:
# 	print("your tickect is free!")
# if age >= 3 and age <= 12:
# 	print("your tickect is $10!")
# else:
# 	print("you're above 12, your tickect is $15!")

#7.6
# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value.

# age = 12
# while age >= 13:
# 	print(age)
# 	#age += 1
# 	if age > 13:
# 		print("Hey, I am above 12!")
# 	else:
# 		print("Oh no!")

# age = 12
# while age >= 25:
# 	print(age)

# 	if age <= 5:
# 		print(age)
# 	else:
# 		print("That isn't correct")
# 	break

#Using a while Loop with Lists and Dictionaries	

# A for loop is effective for looping through a list, but you shouldn’t modify
# a list inside a for loop because Python will have trouble keeping track of the
# items in the list. To modify a list as you work through it, use a while loop.
# Using while loops with lists and dictionaries allows you to collect, store, and
# organize lots of input to examine and report on later.

#Moving Items from One List to Another
# Imagine a list of newly registered but unverified users of a website. After verifying 
#these users, how can they move to a separate list of confirmed users?

# unconfirmed_users = ['nen', 'som', 'josh', 'kay']
# confirmed_users = []

# while unconfirmed_users:
# 	new_users = unconfirmed_users.pop()

# 	print(new_users.title() + ',' + ' I am confirming if you are verified')
# 	confirmed_users.append(new_users)

# print('\nOkay, for now these are the confirmed users:')
# for confirmed_user in confirmed_users:
# 	print(confirmed_user)


#Removing All Instances of Specific Values from a List using remove()
#remove() takes off specific value from a list esp when there's a repetition

# groceries = ['maggi', 'salt', 'species', 'flakes', 'salt', 'noodles', 'salt']
# print(groceries)

# while 'salt' in groceries:
# 	groceries.remove('salt')

# print(groceries)

#Filling a Dictionary with User Input
# responses = {}
# # Set a flag to indicate that polling is active.
# polling_active = True

# while polling_active:
# # Prompt for the person's name and response.
# name = input("\nWhat is your name? ")
# response = input("Which mountain would you like to climb someday? ")
# # Store the response in the dictionary:
# responses[name] = response
# # Find out if anyone else is going to take the poll.
# repeat = input("Would you like to let another person respond? (yes/ no) ")

# if repeat == 'no':
# polling_active = False
# # Polling is complete. Show the results.
# print("\n--- Poll Results ---")

# for name, response in responses.items():
# print(name + " would like to climb " + response + ".")

#DIY 7-8. 
# Make a list called sandwich_orders and fill it with the names of various
# sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.

# sandwich_orders = ['shar', 'hotdog', 'cake','biscuit']
# finished_sandwiches = []

# while sandwich_orders:
# 	new_orders = sandwich_orders.pop()

# 	print('Please your ' + new_orders +  ' sandwich is ready')

# 	finished_sandwiches.append(new_orders)

# print('\nThese are the sandwiches I made today:')
# for finished_sandwich in finished_sandwiches:
# 	print(finished_sandwich + ' sandwich')

#DIY 7-9. 
# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in 
# the list at least three times. Add code near the beginning of your program to print a message
# saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

# sandwich_orders = ['shar','pastrami','hotdog', 'cake','pastrami','biscuit','pastrami']
# print('This is our list of sandwich for today:')

# for sandwich_order in sandwich_orders:
# 	print(sandwich_order)

# print('\nHello, The Deli has run out of pastrami sandwich.')

# finished_sandwiches = []

# print('\nApologies, this is the current list of our sandwich:')

# while 'pastrami' in sandwich_orders:
# 	sandwich_orders.remove('pastrami')
# new_orders = sandwich_orders.pop()

# print('\n', sandwich_orders)

# for sandwich_order in sandwich_orders:
# 	print(sandwich_order)

# finished_sandwiches.append(new_orders)


#DIY7-10. 
# Dream Vacation: Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.