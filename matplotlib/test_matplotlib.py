# import matplotlib
# print("Matplotlib version:", matplotlib.__version__)


# import matplotlib.pyplot as plt
# # Simple data
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# # Plot the line chart
# plt.plot(x, y, color='green', marker='*')

# # Add title and labels
# plt.title("My First Matplotlib Chart")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")

# # Show the chart window
# plt.show()



# import matplotlib.pyplot as plt
# squares = [1, 4, 9, 16, 25]
# plt.plot(squares)
# plt.show()


#Changing the Label Type and Graph Thickness
# import matplotlib.pyplot as plt
# #input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.plot(squares, linewidth=5)

# # Set chart title and label axes.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)

# # Set size of tick labels.
# plt.tick_params(axis='both', labelsize=14)
# plt.show()



#To plot a single point, use the scatter() function
# import matplotlib.pyplot as plt
# plt.scatter(2, 4)
# plt.show()

# import matplotlib.pyplot as plt
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)

# plt.scatter(x_values, y_values, s=50) #use the s argument to set the size of the dots used to draw the graph.
# plt.show()




# import matplotlib.pyplot as plt
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, edgecolor='pink', c='red', s=40)

# # Set chart title and label axes.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)


# # Set the range for each axis.
# plt.axis([0, 1100, 0, 1100000])
# plt.show()




# import matplotlib.pyplot as plt
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
# #plt.scatter(x_values, y_values, c =(0, 0, 0.8), edgecolor='none', s=40)


# #to assign each point a color based on its y-value:
# #plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# # Set chart title and label axes.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)


# # Set the range for each axis.
# plt.axis([0, 1100, 0, 1100000])
# plt.show()


# If you want your program to automatically save the plot to a file, you can
# replace the call to plt.show() with a call to plt.savefig()


# import matplotlib.pyplot as plt
# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
# #plt.scatter(x_values, y_values, c =(0, 0, 0.8), edgecolor='none', s=40)


# #to assign each point a color based on its y-value:
# #plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# # Set chart title and label axes.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)


# # Set the range for each axis.
# plt.axis([0, 1100, 0, 1100000])
# # If you want your program to automatically save the plot to a file, you can
# # replace the call to plt.show() with a call to plt.savefig():
# plt.savefig('more')

# #'more' will be used as the nname if the file.


# DIY
# 15-1. Cubes: A number raised to the third power is a cube. Plot the first five cubic numbers, and then 
# plot the first 5000 cubic numbers.
# 15-2. Colored Cubes: Apply a colormap to your cubes plot.

# import matplotlib.pyplot as plt
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 8, 27, 64, 125]
# plt.title("Cube Graph", fontsize=20)
# plt.xlabel("Value", fontsize=12)
# plt.ylabel("Square of Value", fontsize=12)

# plt.scatter(x_values, y_values, s=50) #use the s argument to set the size of the dots used to draw the graph.
# plt.show()


# import matplotlib.pyplot as plt
# x_values = list(range(1, 5001))
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, c =(0, 0, 0.8), edgecolor='none', s=30)

# #to assign each point a color based on its y-value:
# #plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# # Set chart title and label axes.
# plt.title("Square Numbers", fontsize=20)
# plt.xlabel("Value", fontsize=10)
# plt.ylabel("Square of Value", fontsize=10)

# # Set the range for each axis.
# plt.axis([0, 5100, 0, 5500000])
# plt.savefig('larger_set')
# plt.show()


# import matplotlib.pyplot as plt
# x_values = list(range(1, 5001))
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, c =(0, 0, 0.8), edgecolor='none', s=30)

# #to assign each point a color based on its y-value:
# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, edgecolor='none', s=40)

# # Set chart title and label axes.
# plt.title("Square Numbers", fontsize=20)
# plt.xlabel("Value", fontsize=10)
# plt.ylabel("Square of Value", fontsize=10)

# # Set the range for each axis.
# plt.axis([0, 5100, 0, 5500000])
# plt.savefig('larger_set')
# plt.show()


# A random walk is a path that has no clear direction but is determined by a series of random decisions, 
# each of which is left entirely to chance.

# To create a random walk, create a RandomWalk class, which will make random decisions about which 
# direction the walk should take. The class needs three attributes: one variable to store the number of 
# points in the walk and two lists to store the x- and y-coordinate values of each point in the walk.

# Pick a Random Number
# import random
# number = random.randint(1, 10)
# print("Your random number is:", number)
###random.randint(1, 10) picks an integer between 1 and 10 (both included).

# Pick a Random Item from a List
# import random
# colors = ["red", "blue", "green", "yellow", "purple"]
# chosen_color = random.choice(colors)
# print("The computer picked:", chosen_color)
###random.choice(list) picks one random item from the list.

# Simulate a Dice Roll
# import random
# dice = random.randint(1, 6)
# print("You rolled a:", dice)

# Shuffle a List (like shuffling cards)
# import random
# cards = ["Ace", "King", "Queen", "Jack", "10", "9"]
# random.shuffle(cards)
# print("Shuffled deck:", cards)
###random.shuffle(list) rearranges the items in random order.

# Create Random Floating-Point Numbers
# import random
# for i in range(3):
#     print(random.random())  # prints a random number between 0.0 and 1.0


#Creating the RandomWalk() Class

# import random
# import matplotlib.pyplot as plt

# class RandomWalk:
#     """A class to generate random walks."""

#     def __init__(self, num_points=5000):
#         """Initialize attributes of a walk."""
#         self.num_points = num_points

#         # All walks start at (0, 0)
#         self.x_values = [0]
#         self.y_values = [0]

#     def fill_walk(self):
#         """Calculate all the points in the walk."""

#         # Keep taking steps until the walk reaches the desired length
#         while len(self.x_values) < self.num_points:

#             # Decide which direction to go and how far to go in that direction
#             x_direction = random.choice([1, -1])
#             x_distance = random.choice([0, 1, 2, 3, 4])
#             x_step = x_direction * x_distance

#             y_direction = random.choice([1, -1])
#             y_distance = random.choice([0, 1, 2, 3, 4])
#             y_step = y_direction * y_distance

#             # Reject moves that go nowhere
#             if x_step == 0 and y_step == 0:
#                 continue

#             # Calculate the new position
#             x = self.x_values[-1] + x_step
#             y = self.y_values[-1] + y_step

#             self.x_values.append(x)
#             self.y_values.append(y)


# # --- Make the random walk and plot it ---

# rw = RandomWalk(5000)      # Create an instance
# rw.fill_walk()             # Generate points

# # Plot the points
# plt.style.use('classic')
# fig, ax = plt.subplots(figsize=(10, 6), dpi=100)
# ax.plot(rw.x_values, rw.y_values, linewidth=1)

# # Emphasize the first and last points
# ax.scatter(0, 0, c='green', edgecolors='none', s=100)     # Start
# ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)  # End

# # Remove axes
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)

# plt.show()


# import matplotlib.pyplot as plt
# from random import choice

# class RandomWalk():
# 	"""A class to generate random walks."""
# 	def __init__(self, num_points=5000):
# 		"""Initialize attributes of a walk."""
# 		self.num_points = num_points
# # All walks start at (0, 0).
# 		self.x_values = [0]
# 		self.y_values = [0]

# 	def fill_walk(self):
# 		"""Calculate all the points in the walk."""
# # Keep taking steps until the walk reaches the desired length.
# 	while len(self.x_values) < self.num_points:

# # Decide which direction to go and how far to go in that direction.
# 		x_direction = choice([1, -1])
# 		x_distance = choice([0, 1, 2, 3, 4])
# 		x_step = x_direction * x_distance
# 		y_direction = choice([1, -1])
# 		y_distance = choice([0, 1, 2, 3, 4])
# 		y_step = y_direction * y_distance
# # Reject moves that go nowhere.
# 		if x_step == 0 and y_step == 0:
# 			continue
	
# # Calculate the next x and y values.
# next_x = self.x_values[-1] + x_step
# next_y = self.y_values[-1] + y_step
# self.x_values.append(next_x)
# self.y_values.append(next_y)


# from random_walk import RandomWalk
# # Make a random walk, and plot the points.
# rw = RandomWalk()
# rw.fill_walk()

# plt.scatter(rw.x_values, rw.y_values, s=15)
# plt.show()



#Generating Multiple Random Walks: one way is to wrap it in a while loop. 
# import matplotlib.pyplot as plt
# from random_walk import RandomWalk
# # Keep making new walks, as long as the program is active.
# while True:
# # Make a random walk, and plot the points.
# 	rw = RandomWalk()
# 	rw.fill_walk()
# 	plt.scatter(rw.x_values, rw.y_values, s=15)
# 	plt.show()
# keep_running = input("Make another walk? (y/n): ")
# if keep_running == 'n':
# 	break



#Creating the Die Class
# from random import randint
# class Die:
#     """A class representing a single die."""

#     def __init__(self, num_sides=6):
#         """Assume a six-sided die by default."""
#         self.num_sides = num_sides

#     def roll(self):
#         """Return a random value between 1 and the number of sides."""
#         return randint(1, self.num_sides)

# #Roll the Die and Store Results
# # Create a D6 (six-sided die)
# die = Die()

# # Make some rolls, and store results in a list
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)


# #Analyze the Results: count how often each number appeared.
# frequencies = []
# # Possible outcomes: 1 through 6
# for value in range(1, die.num_sides + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# import pygal
# # Make a bar chart
# hist = pygal.Bar()

# hist.title = "Results of Rolling One D6 1000 Times"
# hist.x_labels = ['1', '2', '3', '4', '5', '6']
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"

# hist.add('D6', frequencies)
# hist.render_to_file('die_visual.svg')
