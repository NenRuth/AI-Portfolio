#Python’s dictionaries, allow you to connect pieces of related information. In Python, a dictionary is wrapped in braces, {}.
# first_child = {'age':'16', 'color':'chocolate', 'name':'meemma', 'height':'5.11'}
# print(first_child['color'])
# print(first_child['age'])
# print(first_child['name'].title())
# print(first_child['height'])


#first_child = 'name'
#new_name = first_child['name']
#print('name' + 'new_name')

#alien_0 = {'color': 'green', 'points': 5}
#new_points = alien_0['points']
#print("You just earned " + str(new_points) + " points!")

# #Adding New Key-Value Pairs: to add a new key-value pair, you
# would give the name of the dictionary followed by the new key in square
# brackets along with the new value.
#first_child['class'] = 'ss2'
#first_child['ssize'] = '45'
#print(first_child)

#Starting with an Empty Dictionary: To start filling an empty dictionary,
#define a dictionary with an empty set of braces and then add each key-value
#pair on its own line.

#first_child = {}
#first_child['color'] = 'chocolate'
#first_child['height'] = '5.11'
#first_child['name'] = 'meemma'
#first_child['class'] = 'ss2'
#first_child['age'] = '16'
#first_child['ssize'] = '45'
#print(first_child)

#Modifying Values in a Dictionary
#To modify a value in a dictionary, give the name of the dictionary with the
#key in square brackets and then the new value you want associated with that key.
#first_child['age'] = '17'
#print(first_child['name'] +  ' was ' +   first_child['age']  + ' last year. He is now 17')

#using conditionlal statements, elif
#original_ssize = '45'
#if first_child['age'] == '15':
	#ssize = '49'
#elif first_child['age'] == '17':
	#ssize = '30'
#else: 
	#ssize = '20'

#print(first_child['name'] +  ' was ' +   first_child['age']  + ' last year. He is now 17')

#Removing Key-Value Pairs
# first_child = {'age':'16', 'color':'chocolate', 'name':'meemma', 'height':'5.11'}
# print(first_child['color'])
# print(first_child['age'])
# print(first_child['name'])
# print(first_child['height'])

# #to delete a ky-value pair, use del

# del first_child['color']
# print(first_child)

# to add back...
# first_child['class'] = 'ss2'
# first_child['ssize'] = '45'
# first_child['color'] = 'chocolate'
# print(first_child)

# #A Dictionary of Similar Objects. You can also use a dictionary to store one
# kind of information about many objects.

#assuming you gave a form where you asked people to fill in their fav dish
# fav_dish = {
# 	'sam':'yam sauce',
# 	'sarah':'jollof rice',
# 	'emmy':'porridge yam',
# 	'nen':'oha soup',
# 	'val':'beans',
# 	'jay':'spag',
# 	'mo':'noodles',	
# }
# print("Sarah's fav dish is "  +  fav_dish['sarah'].title() + "." + " She love it cos of the smoky aroma.")

# #To see which dish a person chose, we ask for the value at:
# print(fav_dish['jay'].title())

# #you can also break this long print statement
# print("Sarah's fav dish is "  +  
# 	fav_dish['sarah'].title() + "." + 
# 	" She love it cos of the smoky aroma.")

#DIY
# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.
# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.
# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

#6.1
# fav_gal = {
# 	"first_name":"ify", 
# 	"last_name":"jaja", 
# 	"age":"15", 
# 	"city":"043", 
# 	"color":"choco",
# 	"class":"jss2",
# 	}
# print(fav_gal)

#6.2
# fav_nums = {
# 	"nen":"1",
# 	"sommy":"2",
# 	"josh":"3",
# 	"kay":"4",
# 	"api":"5",
# 	"bebe":"6",
# }
# print(fav_nums)

#6.3
# fav_prog_lang = {
# 	"python":"a type of prog lang",
# 	"elif":"a conditional statement",
# 	"int":"a whole number",
# 	"string":"an alphabet or word",
# 	"=":"assignment",
# 	"==":"equality", 
# 	"append":"to add",
# 	"tuple":"an immutable list",
# }
# #print(fav_prog_lang)

#Looping Through a Dictionary
#imagine you want to store information about a user on a website.
# user1 = {
# 	"username":"fyja",
# 	"first_name":"ify", 
# 	"last_name":"jaja", 
# 	"age":"15", 
# 	"city":"043", 
# 	"color":"choco",
# 	"class":"jss2",
# 	}
# print(user1["username"])
#print(user1["first_name"])
# print(user1["last_name"])
# print(user1["age"])
# print(user1["city"])
# print(user1["color"])
# print(user1["class"])

# print(user1)


#Looping Through All Key-Value Pairs, using a for loop:

# for key, value in user1.items():
# 	print("\nKey: " + key)
# 	print("Value: " + value)
# #or use this too
# for k, v in user1.items():
# 	print("\nKey: " + key)
# 	print("Value: " + value)

# for name, language in fav_prog_lang.items():
# 	print(name.title() + " is " + language + ".")

#Looping Through All the Keys in a Dictionary. keys() is used to print only the Key
# for name in fav_prog_lang.keys():
# 	print(name.title())
# #or use
# for name in fav_prog_lang:
# 	print(name.title())

# fav_prog_lang2 = ["elif", "int"]

# for name in fav_prog_lang.keys():
# 	print(name.title())
	
# 	if name in fav_prog_lang2:
# 		print("Hey " + name.title() + "," + " why is it your 2nd fav language?")
# if "C" not in fav_prog_lang.keys():
# 	print("\nPlease I suggest you add it!")


#Looping Through a Dictionary’s Keys in Order using sorted()
# for name in sorted(fav_prog_lang.keys()):
# 	print("Hey " + name.title() + "," + " \nthank you for filling the form!")

#Looping Through All Values in a Dictionary
# print("The following languages have been identified:")
# for language in fav_prog_lang.values():
# 	print(language)

#but in a poll with a large number of respondents, this would result in a very repetitive
#list. To see each language chosen without repetition, we can use a set. When you wrap set() around a list that contains duplicate items, Python
#identifies the unique items in the list and builds a set from those items.

# for language in set(fav_prog_lang.values()):
# 	print(language)

#DIY
# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.
# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.
# 6-6. Polling: Use the code in favorite_languages.py (page 104).
# • Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

# fav_prog_lang = {
# 	"python":"a type of prog lang",
# 	"elif":"a conditional statement",
# 	"int":"a whole number",
# 	"string":"an alphabet or word",
# 	"=":"assignment",
# 	"==":"equality", 
# 	"append":"to add",
# 	"tuple":"an immutable list",
# 	"title":"to print the 1st word in cap letter",
# 	"lower":"to print in lower letters",
# 	"upper":"to print in cap letters",
# 	"keys":"used to print only the KEY",
# 	"sorted":"to arrange in order",
# 	"values":"used to print only the value",
# }
# #print(fav_prog_lang)

# #6-4
# for key, value in fav_prog_lang.items():
# 	print("\nKey: " + key)
# 	print("Value: " + value)

# 6-5
# riv_n_cou = {"nigeria":"r.niger", "eygpt":"nile", "zambia":"r.congo"}
# print("These rivers either is the source or just passed through these countries:") 
# for language in riv_n_cou.values():
# 	print(language.title())

# for name, language in riv_n_cou.items():
# 	print("\n" + language.title() + " runs through " + name.title() + ".")


# print("The following rivers have been identified here:")
# for language in riv_n_cou.values():
# 	print(language.title())

# print("\nThe following countries have rivers flowing tru them:")
# for name in riv_n_cou.keys():
# 	print(name.title())

#6-6
# fav_prog_lang = {
# 	"python":"a type of prog lang",
# 	"elif":"a conditional statement",
# 	"int":"a whole number",
# 	"string":"an alphabet or word",
# 	"=":"assignment",
# 	"==":"equality", 
# 	"append":"to add",
# 	"tuple":"an immutable list",
# 	"title":"to print the 1st word in cap letter",
# 	"lower":"to print in lower letters",
# 	"upper":"to print in cap letters",
# 	"keys":"used to print only the KEY",
# 	"sorted":"to arrange in order",
# 	"values":"used to print only the value",
# }

# fav_prog_lang2 = ["elif", "int", "item", "sorted"]
# for name in fav_prog_lang.keys():
# 	print(name.title())
	
# 	if name in fav_prog_lang2:
# 		print("Hey " + name.title() + "," + " thank you for joining the poll!")
# if "C" not in fav_prog_lang.keys():
# 	print("\nPlease I suggest you add it!")

