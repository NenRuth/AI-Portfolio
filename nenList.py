#List: a collection of items in a particular order. In Python, square brackets [] indicate a list. 
#for example
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#print(bicycles)
#elements in a list are numbered from 0, thus, trek = 0, cannondale  = 1, etc.

#To access the element in a List, you tell python the position (aka index) of that element.
#for example:
# print(bicycles[0])
# print(bicycles[2])
# print(bicycles[1])
# print(bicycles[3])
# print(bicycles[0].title())

#To access he last element in a List, -1, -2, -3, etc. for example
# print(bicycles[-1])
# print(bicycles[-3].title())

#Using Individual Values from a List
# message = "My first bicycle was a " +  (bicycles[2].title()) + "."
# print(message)
# message = "Later, I got a " + (bicycles[0].title()) + " and a " + (bicycles[3].title()) + "."
# print(message)
# message = "Among the 3, I prefer " + (bicycles[0].title()) + "."
# print(message)

#DIY:
# 1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.
#names = ['sommy', 'josh', 'pkay', 'ahpi', 'pshal']
# print(names)
# print(names[0].title())
# print(names[1].title())
# print(names[2].title())
# print(names[3].title())
# print(names[4].title())

# 2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message
# should be the same, but each message should be personalized with the person’s name.
# message = "Hey " + (names[0].title()) + "," + " how are you today?!"
# print(message)
# message = "Hey " + (names[1].title()) + "," + " how are you today?!"
# print(message)
# message = "Hey " + (names[2].title()) + "," + " how are you today?!"
# print(message)
# message = "Hey " + (names[3].title()) + "," + " how are you today?!"
# print(message)
# message = "Hey " + (names[4].title()) + "," + " how are you today?!"
# print(message)

# 3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”
# favorite_cars = ['IS350', 'camero', 'dodge', 'ford', 'telsa', 'bmw']
# print(favorite_cars)
# message = 'I love ' + favorite_cars[2] + ' products alot!'
# print(message) 
# message = '2025, I am getting ' + favorite_cars[0] + ', ' + favorite_cars[1] + ', and ' + favorite_cars[5].upper() + '.'
# print(message)

#Modifying Elements in a List
#motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)

#Adding Elements to a List: use .append() (this will only add element at 
# the end of the list) or .insert() (this let's you choose where to add the element).
# for example
# motorcycles.append('ducati')
# print(motorcycles)

# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert(0, 'ducati')
# print(motorcycles)
# motorcycles.insert(2, 'mitbushi')
# print(motorcycles)

#Removing Elements from a List: You can remove an item according to its position 
# in the list or according to its value. This can be done using del 
#(allows you to del a particular eleemnt) or pop() method. 
#the pop() removes the last item on the list.
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)
# motorcycles = ['ducati', 'honda', 'mitbushi', 'yamaha', 'suzuki']
# del motorcycles[2]
# print(motorcycles) 

# motorcycles = ['ducati', 'honda', 'mitbushi', 'yamaha', 'suzuki']
# print(motorcycles)
# p_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(p_motorcycle)
# fav_motorcycle = motorcycles.pop()
# print(fav_motorcycle)

#Popping Items from any Position in a List
# first_owned = motorcycles.pop(0)
# print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# Removing an Item by Value: used to remove an item when the value is not known
# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)

# DIY: Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.
# Guest = ['Arinze', 'Bemzy', 'Angelo', 'Rolly', 'Abass', 'Bond', 'Osondu', 'Michael', 'Mark']
# message = 'Hey ' + (Guest[0].title()) + "!," + " here's an IV to my dinner ball."
# print(message)
# message = 'Hey ' + (Guest[1].title()) + "!," + " here's an IV to my dinner ball."
# print(message)
# message = 'Hey ' + (Guest[2].title()) + "!," + " here's an IV to my dinner ball."
# print(message)
# message = 'Hey ' + (Guest[3].title()) + "!," + " here's an IV to my dinner ball."
# print(message)
# message = 'Hey ' + (Guest[4].title()) + "!," + " here's an IV to my dinner ball."
# print(message)
# message = 'Hey ' + (Guest[5].title()) + "!," + " here's an IV to my dinner ball."
# print(message)
# message = 'Hey ' + (Guest[6].title()) + "!," + " here's an IV to my dinner ball."
# print(message)
# message = 'Hey ' + (Guest[7].title()) + "!," + " here's an IV to my dinner ball."
# print(message)
# message = 'Hey ' + (Guest[8].title()) + "!," + " here's an IV to my dinner ball."
# print(message)

# DIY: You just found a bigger dinner table, so now more space is available. 
# Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

# Guest = ['Arinze', 'Bemzy', 'Angelo', 'Rolly', 'Abass', 'Bond', 'Osondu', 'Michael', 'Mark']
# Guest.insert(9, 'Great')
# Guest.insert(0, 'EK')
# Guest.append('Victor')
# print(Guest)
# print("I'm adding " + Guest[0] + ', ' + Guest[10] + ', ' + 'and ' + Guest[11] + " since I found a bigger hall.")

#DIY: Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

#Guest = ['Arinze', 'Bemzy', 'Angelo', 'Rolly', 'Abass', 'Bond', 'Osondu', 'Michael', 'Mark']
# message = "I'm so sorry guys, I can only invite 2 persons at the time"
# r_guest = Guest.pop()
# print(Guest)
# print(r_guest + ", " + "I'm so sorry guys, I can only invite 2 persons at the time")

# r_guest = Guest.pop()
# print(Guest)
# print(r_guest + ", " + "I'm so sorry guys, I can only invite 2 persons at the time")

# r_guest = Guest.pop()
# print(Guest)
# print(r_guest + ", " + "I'm so sorry guys, I can only invite 2 persons at the time")

# r_guest = Guest.pop()
# print(Guest)
# print(r_guest + ", " + "I'm so sorry guys, I can only invite 2 persons at the time")

# r_guest = Guest.pop()
# print(Guest)
# print(r_guest + ", " + "I'm so sorry guys, I can only invite 2 persons at the time")

# r_guest = Guest.pop()
# print(Guest)
# print(r_guest + ", " + "I'm so sorry guys, I can only invite 2 persons at the time")

# r_guest = Guest.pop()
#print(Guest)
# print(r_guest + ", " + "I'm so sorry guys, I can only invite 2 persons at the time")

# print(Guest)
# message = 'Hey ' + (Guest[0].title()) + "!," + " here's an IV to my dinner ball."
# print(message)
# message = 'Hey ' + (Guest[1].title()) + "!," + " here's an IV to my dinner ball."
# print(message)

# del Guest[0]
# del Guest[1]

#Organizing a List: you can organize a list using sort(), 
#cars = ['bmw', 'audi', 'toyota', 'subaru']
#cars.sort()
#print(cars)

# #You can also sort this list in reverse alphabetical order using reverse=True
#cars = ['bmw', 'audi', 'toyota', 'subaru']
#cars.sort(reverse=True)
#print(cars)

#sorted(): used for already sorted list. 
#reverse(): used to change the order of the list. 
#cars.reverse()
#print(cars)

#Finding the Length of a List: use len()
#len(cars)

#DIY: Think of at least five places in the world you’d like to visit.
#• Store the locations in a list. Make sure the list is not in alphabetical order.
#• Print your list in its original order. Don’t worry about printing the list neatly, 
#just print it as a raw Python list.
# f_places = ['paris', 'ny', 'dubai', 'island', 'japan']
# print(f_places)

#• Use sorted() to print your list in alphabetical order without modifying the
#actual list.
# f_places.sort()
# print(f_places)

#• Show that your list is still in its original order by printing it.
# f_places.sort(reverse=True)
# print(f_places)

#• Use sorted() to print your list in reverse alphabetical order without changing
#the order of the original list.
# print(sorted(f_places))

#• Show that your list is still in its original order by printing it again.
# f_places = ['paris', 'ny', 'dubai', 'island', 'japan']
# print(f_places)
#• Use reverse() to change the order of your list. Print the list to show that its
#order has changed.
# f_places = ['paris', 'ny', 'dubai', 'island', 'japan']
# f_places.reverse()
# print(f_places)
#• Use reverse() to change the order of your list again. Print the list to show
#it’s back to its original order.
# f_places.reverse()
# print(f_places)
#• Use sort() to change your list so it’s stored in alphabetical order. Print the
#list to show that its order has been changed.
# f_places = ['paris', 'ny', 'dubai', 'island', 'japan']
# f_places.sort()
# print(f_places)
#• Use sort() to change your list so it’s stored in reverse alphabetical order.
#Print the list to show that its order has changed.