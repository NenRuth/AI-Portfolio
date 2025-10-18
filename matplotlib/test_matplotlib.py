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

