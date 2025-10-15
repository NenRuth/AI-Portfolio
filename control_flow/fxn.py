#Functions allow you to break your programs into small parts, each of which does one specific job.
#note: very few of these codes didn't run the way I wanted it to due to some tiny errors I was unable
#to figure out. Will come back to them later. 

# def greet_user():
# # 	"""Display a simple greeting."""
# 	print("Hello!")
# greet_user()

# def greet_user(username):
# 	"""Display a simple greeting."""
# 	print("Hello, " + username.title() + "!")
# greet_user('jesse')
# greet_user('sarah')
# greet_user('nen')
# greet_user('josh')

#An argument is a piece of information that is passed from a function call to a function. The value
# 'jesse' in greet_user('jesse') is an example of an argument.
# parameter, a piece of information the function needs to do its job. The variable username in 
# the definition of greet_user() is an example of a parameter. 

# DIY 
# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone 
# what you are learning about in this chapter. Call the function, and make sure the message displays 
# correctly.

# def display_message():
# 	print('Hey everyone, this is chapt 8 and I am learning Functions in Python!')
# display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. 
# The function should print a message, such as One of my favorite books is Alice in Wonderland. 
# Call the function, making sure to include a book title as an argument in the function call.

# def favorite_book(title):
# 	print(title + ' is one of my favorite books!')
# favorite_book('Nigerian_Men')
# favorite_book('Cognitive_Computing in Education')
# favorite_book('Climate_Tech & Education')

#Positional Arguments

# def start_up_coys(seo, academy):
# 	print(seo + ',' + academy + ',' +  'are my start up coy.')
# 	# print(start_up_coys)

# start_up_coys('nendigi', 'netatutors')


# def describe_pet(animal_type, pet_name):
# 	"""Display information about a pet."""
# 	print("\nI have a " + animal_type + ".")
# 	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# def start_up_coys(seo, academy, writing, saas):
# 	print(seo + ',' + academy + ',' + writing + ',' saas + ',' + 'are my start up coys:')
# 	# print(start_up_coys)
# start_up_coys('nendigi', 'netatutors', 'netalearners', 'nenvoice')

#NB: order matters in positional arguments. 

#Keyword Arguments: keyword argument is a name-value pair that you pass to a function.
# keyword argument directly associate the name and the value within the argument, so when you
# pass the argument to the function, there’s no confusion (for example; you won’t end up with a 
# harry named Hamster)

# def describe_pet(animal_type, pet_name):
# 	"""Display information about a pet."""
# 	print("\nI have a " + animal_type + ".")
# 	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet(animal_type='hamster', pet_name='harry')


# def start_up_coys(seo, academy):
# 	print('\n', seo.title() + ', ' +  academy.title() + ',' +  ' are my start up coy.')
# 	# print(start_up_coys)

# start_up_coys(seo = 'nendigi', academy = 'netatutors')

# #Default Values
# def start_up_coys(seo, academy = 'neta academy'):
# 	print('\n', seo.title() + ', ' +  academy.title() + ',' +  ' are my start up coy.')

# start_up_coys('nendigi')


# start_up_coys('nenval')

#nb: neta academy is the default value here. 
# When you use default values, any parameter with a default value needs to be listed
# after all the parameters that don’t have default values. This allows Python to continue
# interpreting positional arguments correctly.


# Equivalent function calls: positional arguments, keyword arguments, and default values can all 
# be used together. 

# Unmatched arguments occur when you provide fewer or more arguments than a function needs to do 
# its work. 

# def describe_pet(animal_type, pet_name):
# 	"""Display information about a pet."""
# 	print("\nI have a " + animal_type + ".")
# 	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet('animal_type','pet_name')


# DIY 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a 
# message that should be printed on the shirt. The function should print a sentence summarizing
# the size of the shirt and the message printed on it. Call the function once using positional 
# arguments to make a shirt. Call the function a second time using keyword arguments.
# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a 
# message that reads I love Python. Make a large shirt and a medium shirt with the default message, 
# and a shirt of any size with a different message.
# 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its 
# country. The function should print a simple sentence, such as Reykjavik is in Iceland. 
# Give the parameter for the country a default value. Call your function for three different cities,
# at least one of which is not in the default country.

#8-3
# def make_shirt(cloth_size):

# 	print('I want' + cloth_size)
# make_shirt(' UK size 30, and "Hello Neta" should be printed on the back.')


###make_shirt(' UK size 32, and "NetaTutors logo" printed on the front.')
###make_shirt(' UK size 34, but it should be plain.')


#positional arguments
# def make_shirt(cloth_size, script):
# 	print('UK size 30, "Hello Neta" should be printed on the back, is all I want for now.')

# make_shirt('UK size 30', '"Hello Neta" should be printed on the back, is all I want for now')

# #keyword arguments
# def make_shirt(cloth_size, script):
# 	print('UK size 30, "Hello Neta" should be printed on the back, is all I want for now.')

# make_shirt(cloth_size ='UK size 30', script = '"Hello Neta" should be printed on the back, is all I want for now')

#8-4
# def make_shirt(cloth_size, script):
# 	print('I want UK size ' + cloth_size + ',' ' and ' + script + ' should be printed on the back, that is all I want for now.')

# make_shirt(cloth_size = '50', script = 'I love Python')

# 8-5
# def describe_city(city, country):
# 	print(city + ' is in ' + country)

# describe_city('Reykjavik', 'Iceland')
# describe_city('\nAbj', 'Nigeria')
# describe_city('\nParis', 'France')
	

# def describe_city(city, country = 'Nigeria'):
# 	print(city + ' is in ' + country)

# describe_city('\nLagos')
# describe_city('PH city')
# describe_city('Onitsha')


#Return Values: When you call a function that returns a value, you need to provide a
#variable where the return value can be stored.

# def get_formatted_name(first_name, last_name):
# 	full_name = first_name + ' ' + last_name
# 	return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# def your_name(first_name, last_name):
# 	full_name = first_name +' ' + last_name
# 	return full_name
# writer = your_name('ruth', 'ralph')
# print(writer)

# def your_name(first_name, middle_name, last_name):
# 	full_name = first_name +' ' + middle_name + ' ' + last_name
# 	return full_name
# writer = your_name('ruth', 'ifunanya', 'ralph')
# print(writer)


#Making an argument optional: You can use default values to make an argument optional. 
# To make get_formatted_name() work without a middle name, we set the default value of middle_name 
# to an empty string and move it to the end of the list of parameters:

# def your_name(first_name, last_name, middle_name= ''):
# 	if middle_name:
# 		full_name = first_name +' ' + middle_name + ' ' + last_name
# 	else:
# 		full_name = first_name + ' ' + last_name
# 	return full_name
# writer = your_name('ruth', 'ralph')
# print(writer)
# writer = your_name
# writer = your_name('ruth', 'ifunanya', 'ralph')
# print(writer)

#this function works for people with just a first and last name, and it works for people who 
#have a middle name as well.

# def get_formatted_name(first_name, last_name, middle_name=''):
# 	"""Return a full name, neatly formatted."""
# 	if middle_name:
# 		full_name = first_name + ' ' + middle_name + ' ' + last_name
# 	else:
# 		full_name = first_name + ' ' + last_name
# 	return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# musician = get_formatted_name


#Returning a dictionary

# def my_name(first_name, last_name):
# 	person = {'first':first_name, 'last':last_name}
# 	return person
# writer = my_name('ruth', 'ralph')
# print(writer)


# def build_person(first_name, last_name, age=''):
# 	person = {'first': first_name, 'last': last_name}
# 	if age:
# 		person['age'] = age
# 	return person
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)


#Using a Function with a while Loop
# def my_name(first_name, last_name):
# 	full_name = first_name + ' ' + last_name
# 	return full_name.title()
# # This is an infinite loop!
# while True:
# 	print("\nPlease tell me your name:")
# f_name = input("First name: ")
# l_name = input("Last name: ")
# formatted_name = my_name(f_name, l_name)
# print("\nHello, " + formatted_name + "!")
# 	break


#DIY
# 8-6. City Names: Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value that’s returned.
# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, and it should return a dictionary 
# containing these two pieces of information. Use the function to make three dictionaries representing
# different albums. Print each return value to show that the dictionaries are storing the album 
# information correctly.Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the number of tracks, add 
# that value to the album’s dictionary. Make at least one new function call that includes the number
# of tracks on an album.
# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users 
# to enter an album’s artist and title. Once you have that information, call make_album() with the 
# user’s input and print the dictionary that’s created. Be sure to include a quit value in the while 
# loop.

#8-6. 
# def city_country(city, country):
# 	c_in_coun = city + ',' + ' ' + country
# 	return c_in_coun
# explorer1 = city_country('Abj', 'Nigeria')
# explorer2 = city_country('Lag', 'Nigeria')
# explorer3 = city_country('PH', 'Nigeria')
# print(explorer1)
# print(explorer2)
# print(explorer3)


# 8-7.
# def make_album(full_name, al_name):
# 	artist = {'f_name':full_name, 'l_name':al_name}
# 	return artist
# producer = make_album('obo', 'funds')
# print(producer)

# def make_album(full_name, al_name):
# 	artist = {'f_name':full_name, 'l_name':al_name}
# 	return artist
# producer = make_album('runtown', 'mad_over_you')
# print(producer)

# def make_album(full_name, al_name):
# 	artist = {'f_name':full_name, 'l_name':al_name}
# 	return artist
# producer = make_album('simi', 'duduke')
# print(producer)

#Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the number of tracks, add 
# that value to the album’s dictionary. Make at least one new function call that includes the number
# of tracks on an album.

# def make_album(full_name, al_name, no_of_tracks=''):
# 	if no_of_tracks:
# 		make_album = full_name +' ' + al_name + ' ' + no_of_tracks
# 	else:
# 		make_album = full_name +' ' + al_name
# 	return make_album

# artist = {'f_name':full_name, 'l_name':al_name}
# producer = make_album('obo', 'funds')
# print(producer)

# producer = make_album('obo', 'funds','no_of_tracks = 6')
# print(producer)


#Passing a List: When you pass a list to a function, the function gets direct access to the contents 
#of the list.

# def greet_users(names):
# 	for name in names:
# 		note = 'Hello ' + name + '!'
# 		print(note)
# usernames = ['nen', 'sam', 'val']
# greet_users(usernames)


#Modifying a List in a function: When you pass a list to a function, the function can modify the list.
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
# 	current_design = unprinted_designs.pop()

# # Simulate creating a 3D print from the design.
# print("Printing model: " + current_design)
# completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
# 	print(completed_model)


# unprinted_designs = ['tecno', 'itel', 'samsung', 'redmi']
# completed_models = []

# while unprinted_designs:
# 	new_designs = unprinted_designs.pop()
# print('Models that need to be printed:' + '\n', new_designs)
# completed_models.append(new_designs)

# print('\nThese have been printed:')
# for completed_model in completed_models:
# 	print(completed_model)


#Preventing a Function from Modifying a List
# Sometimes you’ll want to prevent a function from modifying a list. For
# example, say that you start with a list of unprinted designs and write a
# function to move them to a list of completed models, as in the previous
# example. You may decide that even though you’ve printed all the designs,
# you want to keep the original list of unprinted designs for your records. But
# because you moved all the design names out of unprinted_designs, the list is
# now empty, and the empty list is the only version you have; the original is
# gone. In this case, you can address this issue by passing the function a copy
# of the list, not the original. Any changes the function makes to the list will
# affect only the copy, leaving the original list intact.
# You can send a copy of a list to a function like this:
# function_name(list_name[:])
# The slice notation [:] makes a copy of the list to send to the function.
# If we didn’t want to empty the list of unprinted designs. 

# we could call print_models() like this:
# print_models(unprinted_designs[:], completed_models)


#DIY
# 8-9. Magicians: Make a list of magician’s names. Pass the list to a function
# called show_magicians(), which prints the name of each magician in the list.
# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding
# the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.
# 8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians’ names. Because the
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original
# names and one list with the Great added to each magician’s name.

#8-9
# def show_magicians(names):
# 	for name in names:
# 		magic = name.title() + ' he is magician.'
# 		print(magic)
# magicians = ['nen', 'sam', 'val']
# show_magicians(magicians)

#8-10
# def make_great(names):
# 	for name in names:
# 		magic = 'Great ' + name
# 		print(magic)
# magicians = ['nen', 'sam', 'val']
# make_great(magicians)



#Passing an Arbitrary Number of Arguments: The asterisk in the parameter name *toppings tells Python
#to make an empty tuple called toppings and pack whatever values it receives into this tuple.
#for example
# def make_pizza(*toppings):
# 	"""Print the list of toppings that have been requested."""
# 	print(toppings)
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# """Summarize the pizza we are about to make."""
# print("\nMaking a pizza with the following toppings:")
# for topping in toppings:
# 	print("- " + topping)


# def oha_soup(*proteins):
# 	print(proteins)
# oha_soup('crayfish')
# oha_soup('stockfish', 'icefish', 'beef', 'pork', 'goatmeat')
# print('\nThese are the proteins on the menu:')

# for protein in proteins:
# 	print(protein)


# If you want a function to accept several different kinds of arguments, the parameter that accepts an 
# arbitrary number of arguments must be placed last in the function definition.

# For example, if the function needs to take in a size for the pizza, that
# parameter must come before the parameter *toppings. 

# def oha_soup(size, *proteins):
# 	print(proteins)
# oha_soup('crayfish')
# oha_soup('stockfish', 'icefish', 'beef', 'pork', 'goatmeat')
# print('\nThese are the proteins on the menu:')

# for protein in proteins:
# 	print(protein)


# print('\nYou ordered' + str(size) + 'kg of these proteins')
# for protein in proteins:
# 	print(protein)

# oha_soup(10, 'crayfish')
# oha_soup(12, 'stockfish', 'icefish', 'beef', 'pork', 'goatmeat')





# BMI Calculator

# 1. Get user input
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# 2. Calculate BMI
bmi = weight / (height ** 2)

# 3. Display result
print(f"\nYour BMI is: {bmi:.2f}")

# 4. Determine category
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("You have a normal weight.")
elif 25 <= bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
