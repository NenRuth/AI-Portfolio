#RANGE

#for chefs in range(1,5):
	#print(chefs)

#Converting range to list using list()
# chefs = list(range(1,5))
# print(chefs)

#using range() to skip numbers
# num = list(range(1,15,3)) #3 tells the num it'll be skip counting in, 1,15 tells the num range it'll print.
# print(num)

#In python, two asterisks (**) represent exponents.

# squares = []
# for value in range(1,11):
# 	squares.append(value**2)
# print(squares)

# nums = []
# for num in range(1,11):
# 	nums.append(num**2)
# print(nums)

# squares = [value**2 for value in range(1,11)]
# print(squares)

#digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#min(digits)
# 0
# max(digits)
# 9
# sum(digits)

#DIY: Counting to Twenty: Use a for loop to print the numbers from 1 to 20,inclusive.
# for nums in range(1,21):
# 	print(nums)
# #If you want it to be in a list
# nums = list(range(1,21))
# print(nums)	

# . One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)
# nums = list(range(1,1000001))
# print(nums)

# for nums in range(1,1000001):
# 	print(nums)

# . Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.
# nums = list(range(1,1000001))
# print(nums)

# . Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.
# for nums in range(1,21,2):
# 	print(nums)
# nums = list(range(1,21,2))
# print(nums)

# . Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
# nums = list(range(3, 31,3))
# print(nums)

# for nums in range(3,31,3):
# 	print(nums)

# . Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.
# nums = []
# for num in range(1,10):
# 	nums.append(num**3)
# print(nums)

# . Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.
# nums = [num**3 for num in range(1,10)]
# # print(nums)

#Slicing a List: working with a specific group of items in a list.

#Copying a list
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# print(friend_foods)

# print("\nMy fav foods are-:")
# print(my_foods)

# print("\nMy son's fav food are-:")
# print(friend_foods)

#Tuples: allow you to create a list of items that cannot change. Python refers to values that cannot
#change as immutable, and an immutable list is called a tuple. use parentheses instead of square
#brackets.
#dimensions = (100,200,50)
# print(dimensions[0])
# print(dimensions[2])

#Looping Through All Values in a Tuple
# for dimension in dimensions:
# 	print(dimension)

# DIY: 
# Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the
# change.
# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a block of code that rewrites the tuple, and then use a for
# loop to print each of the items on the revised menu.

#buffets = ('vegsoup', 'vegsauce','vegyam', 'vegrice', 'vegbeans')
# for buffet in buffets:
# 	print(buffet)

#buffets[0] = ('porridge') 

# print('\nThe old menu include:')
# for buffet in buffets:
# 	print(buffet)

#buffets = ('okro', 'oha', 'nsala', 'bitterleaf')
#print('\nRevised meun include:')
#for buffet in buffets:
	#print(buffet)

