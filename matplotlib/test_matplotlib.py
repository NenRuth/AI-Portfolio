# import matplotlib
# print("Matplotlib version:", matplotlib.__version__)

import matplotlib.pyplot as plt

# Simple data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot the line chart
plt.plot(x, y, color='blue', marker='o')

# Add title and labels
plt.title("My First Matplotlib Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Show the chart window
plt.show()
