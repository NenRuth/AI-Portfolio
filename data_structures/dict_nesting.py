#Nesting: store a set of dictionaries in a list or a list of items as a value in a dictionary. 
# nesting allows you keep dictionaries inside a list, a list of items inside a dictionary, or even a
# dictionary inside another dictionary.

#A List of Dictionaries
# fav_gal1 = {
# 	"first_name":"ify", 
# 	"last_name":"jaja", 
# 	"age":"15", 
# 	"city":"043", 
# 	"color":"choco",
# 	"class":"jss2",
# 	}

# fav_gal2 = {
# 	"first_name":"dima", 
# 	"last_name":"ubaja", 
# 	"age":"10", 
# 	"city":"042", 
# 	"color":"choco",
# 	"class":"g1",
# 	}

# fav_gal3 = {
# 	"first_name":"nen", 
# 	"last_name":"ra", 
# 	"age":"18", 
# 	"city":"044", 
# 	"color":"choco",
# 	"class":"g5",
# 	}
# fav = [fav_gal1, fav_gal2, fav_gal3]
# for fav_gal in fav:
# 	print(fav_gal)

#we can use range() to create a fleet of 30 fav_gal
# Make an empty list for storing fav_gal.

# fav = []
# for favv in range(30):
# 	new_fav = {
# 	"first_name":"nen", 
# 	"last_name":"ra", 
# 	"age":"18", 
# 	"city":"044", 
# 	"color":"choco",
# 	"class":"g5",
# 	"food":"rice"
# 	}
# 	fav.append(new_fav)
# for fav_gal in fav[:5]:
# 	print("\n", fav)
# print("...")

# print("\nTotal number of fav: " + str(len(fav)))


#a list inside a dictionary. 
# sharwama = {
# 	"pork_shar":"carbage",
# 	"chick_shar":["carbage", "sauage", "carrot"],
# }
# #print("Please confirm your order: " +  sharwama["pork_shar"] + " " sharwama["chick_shar"] + "-pork sharwama with additional")

# for chick_shar in sharwama['chick_shar']:
# 	print("\t" + chick_shar)

#You can nest a list inside a dictionary any time you want more than one value to be associated
#with a single key in a dictionary.

# sibs = {
	#"nen":["techy","teacher"],
# 	"sommy":"herbs",
# 	"josh":["techy","elcengr"],
# 	"kay":["engr","past"],
# 	"api":"teacher",
# }
# for name, language in sibs.items():
# 	print("Hey " + name + "," + " what and what are you into?")
# 	for language in language:
# 		print("\t" + language)

# for name, language in sibs.items():
# 	if sibs == ["sommy","api"]:
# 		print("Nahh, just this...")

#A Dictionary in a Dictionary
# users = {
# 	'nen':{
# 	'first':'nen',
# 	'last':'ralph',
# 	'location':'asb',
# 	},
# 	'ra':{
# 	'first':'shal',
# 	'last':'ze',
# 	'location':'abj',
# 	},
# }
# for name, language in users.items():
# 	print('\nname:' + name)

# full_name = language['first'] + " " + language['last']
# location = language['location']
# print("\tFull name: " + full_name.title())
# print("\tLocation: " + location.title())

#DIY
# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.
# Dictionaries 115
# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.
# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.
# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.
# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information
# you have stored about it.
# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example programs
# from this chapter, and extend it by adding new keys and values, changing
# the context of the program or improving the formatting of the output.

#6.7
# fav_gal = {
# 	"first_name":"ify", 
# 	"last_name":"jaja", 
# 	"age":"15", 
# 	"city":"043", 
# 	"color":"choco",
# 	"class":"jss2",
# 	},

# fav_gal2 = {
# 	"first_name":"dima", 
# 	"last_name":"ubaja", 
# 	"age":"10", 
# 	"city":"042", 
# 	"color":"choco",
# 	"class":"g1",
# 	},

# fav_gal3 = {
# 	"first_name":"nen", 
# 	"last_name":"ra", 
# 	"age":"18", 
# 	"city":"044", 
# 	"color":"choco",
# 	"class":"g5",
# 	}
# people = [fav_gal, fav_gal2, fav_gal3]
# for name in people:
# 	print("\n", name)

#6-8
# cat = {
# 	'name':'sasi',
# 	'age':'1yr',
# 	'owner':'paul',
# 	}
# dog = {
# 	'name':'pif',
# 	'age':'2yrs',
# 	'owner':'dan',
# 	}
# goat = {
# 	'name':'kid',
# 	'age':'3yrs',
# 	'owner':'sam',
# 	}
# pets = [cat, dog, goat]

# for key, value in pets.items():
# 	print("\nKey: " + key)
# 	print("Value: " + value)

# for name, language in pets.items():
# 	print('\nname: ' + name)

# fullname = language['name']
# age = language['age']
# owner = language['owner']
# print('\tfullname: ' + fullname.title())
# print('\towner: ' + owner.title())
# print('\tage: ' + age)

# fav = [fav_gal1, fav_gal2, fav_gal3]
# for animals in pets:
# 	print(animals)

#6.9

# favorite_places = {
# 	"nen":["france", "monaco", "japan"],
# 	"som":"india",
# 	"josh":["poland","nz"],
# 	}
# for name, language in favorite_places.items():
# 	print(name)
# for language in language:
# 	print('\nname:' + name)
#  	print('language:' + language)

#6.10
# fav_nums = {
# 	"nen":["1","16","24"],
# 	"sommy":["2","12","7"],
# 	"josh":["3","11"],
# 	"kay":["4","100"],
# 	"api":["5","1"],
# 	"bebe":["6","56","40"],
# }
# for key, value in fav_nums.items():
# 	print(fav_nums)
# for value in value:
# 	print('\nkey:' + key)
# 	print('value:' + value)