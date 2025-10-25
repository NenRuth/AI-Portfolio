# import csv

# filename = 'sitka_weather_07-2014.csv'  #storing the name of the file. 
# with open(filename) as f:
# 	reader = csv.reader(f) #calling the csv.reader() and pass it the file object as an argument to create a reader object associated with that file
# 	header_row = next(reader)
# 	print(header_row)


#Printing the Headers and Their Positions
# import csv

# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
# 	reader = csv.reader(f)
# 	header_row = next(reader)
# for index, column_header in enumerate(header_row): #use enumerate()on the list to get the index of each item, as well as the value.
# 	print(index, column_header)

#Extracting and Reading Data
# import csv
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
# 	reader = csv.reader(f)
# 	header_row = next(reader)
# 	highs = [] # Get high temperatures from file.
# 	for row in reader:
# 		highs.append(row[1])
# 	print(highs) 

#the output is in strings. for it to be read by matplotlib, convert it to int. 

#strings to numbers with int()
# import csv
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
# 	reader = csv.reader(f)
# 	header_row = next(reader)
# 	highs = []
# 	for row in reader:
# 		high = int(row[1])
# 		highs.append(high)
# 	print(highs)


#Plotting Data in a Temperature Chart
# import csv
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
# 	reader = csv.reader(f)
# 	header_row = next(reader)
# 	highs = []
# 	for row in reader:
# 		high = int(row[1])
# 		highs.append(high)
# 	print(highs)

# from matplotlib import pyplot as plt

# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(highs, c='red')

# plt.title("Daily high temperatures, July 2014", fontsize=24)
# plt.xlabel('', fontsize=16)
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
# plt.show()

# from datetime import datetime
# first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
# print(first_date)
# 2014-07-01 00:00:00


#Plotting Dates
# import csv
# from datetime import datetime
# from matplotlib import pyplot as plt

# filename = 'sitka_weather_07-2014.csv' # Get dates and high temperatures from file.
# with open(filename) as f:
# 	reader = csv.reader(f)
# 	header_row = next(reader)
	
# 	dates, highs = [], []  #create two empty lists to store the dates and high temperatures from the file
# 	for row in reader:
# 		current_date = datetime.strptime(row[0], "%Y-%m-%d")
# 		dates.append(current_date)
# 		high = int(row[1])
# 		highs.append(high)

# fig = plt.figure(dpi=128, figsize=(10, 6))  # Plot data.
# plt.plot(dates, highs, c='blue')

# # Format plot/labelling
# plt.title("Daily high temperatures, July 2014", fontsize=24)  #only for the month of July. 
# plt.xlabel('', fontsize=16)

# fig.autofmt_xdate()
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
# plt.show()


#Plotting a Longer Timeframe
# import csv
# from datetime import datetime
# from matplotlib import pyplot as plt

# filename = 'sitka_weather_2014.csv' # Get dates and high temperatures from file for the yr.
# with open(filename) as f:
# 	reader = csv.reader(f)
# 	header_row = next(reader)
	
# 	dates, highs = [], []  #create two empty lists to store the dates and high temperatures from the file
# 	for row in reader:
# 		current_date = datetime.strptime(row[0], "%Y-%m-%d")
# 		dates.append(current_date)
# 		high = int(row[1])
# 		highs.append(high)

# fig = plt.figure(dpi=128, figsize=(10, 6))  # Plot data.
# plt.plot(dates, highs, c='blue')

# # Format plot/labelling
# plt.title("Daily high temperatures - 2014", fontsize=18)  #for the whole yr. 
# plt.xlabel('', fontsize=10)

# fig.autofmt_xdate()  #makes the date label diagonally
# plt.ylabel("Temperature (F)", fontsize=10)
# plt.tick_params(axis='both', which='major', labelsize=10)
# plt.show()


#Plotting a Second Data Series
# import csv
# from datetime import datetime
# from matplotlib import pyplot as plt

# filename = 'sitka_weather_2014.csv'
# with open(filename) as f:
# 	reader = csv.reader(f)
# 	header_row = next(reader)
# 	dates, highs, lows = [], [], []
# 	for row in reader:
# 		current_date = datetime.strptime(row[0], "%Y-%m-%d")
# 		dates.append(current_date)
# 		high = int(row[1])
# 		highs.append(high)
# 		low = int(row[3])
# 		lows.append(low)

# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates, highs, c='red')
# plt.plot(dates, lows, c='blue')

# plt.title("Daily high and low temperatures - 2014", fontsize=12)
# plt.show()


#strings to numbers with int()
# import csv
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
# 	reader = csv.reader(f)
# 	header_row = next(reader)
# 	highs = []
# 	for row in reader:
# 		high = int(row[1])
# 		highs.append(high)
# 	print(highs)


#strings to numbers with int()
# import csv
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as f:
# 	reader = csv.DictReader(f)
# 	header_row = next(reader)
# 	highs = []
# 	for row in reader:
# 		if row['AKDT'] == '2025-10-03':   # your target date
			
# 		# high = int(row[1])
# 		# highs.append(high)
# 			print("High Temp:", row['High_Temp'])
# 			print("Low Temp:", row['Low_Temp'])
# 			print("Mean Humidity:", row['Mean_Humidity'])
# 			print(row)


#To read data from a specific date
# import csv
# file_path = "sitka_weather_07-2014.csv"
# target_date = '2014-7-2'  # change to any day you want

# with open(file_path, 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         # Clean spaces in column names and values
#         clean_row = {key.strip(): value.strip() for key, value in row.items()}

#         if clean_row['AKDT'] == target_date:
#             print(f"Weather data for {target_date}:")
#             for key, value in clean_row.items():
#                 print(f"{key}: {value}")
#             break
#     else:
#         print(f"No data found for {target_date}.")


#To visualize
# import csv
# import matplotlib.pyplot as plt

# filename = "sitka_weather_07-2014.csv"
# target_date = '2014-7-2'  # You can change this date to any specific day in your file.

# with open(filename, 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         # Clean up header and value spaces
#         clean_row = {key.strip(): value.strip() for key, value in row.items()}

#         if clean_row['AKDT'] == target_date:
#             # Extract relevant data
#             max_temp = float(clean_row['Max TemperatureF'])
#             mean_temp = float(clean_row['Mean TemperatureF'])
#             min_temp = float(clean_row['Min TemperatureF'])

#             # Plot the data
#             temps = [max_temp, mean_temp, min_temp]
#             labels = ['Max Temp (°F)', 'Mean Temp (°F)', 'Min Temp (°F)']

#             plt.bar(labels, temps, color=['red', 'orange', 'blue'])
#             plt.title(f"Temperatures for {target_date}")
#             plt.ylabel("Temperature (°F)")
#             plt.xlabel("Temperature Type")
#             plt.grid(axis='y', linestyle='--', alpha=0.7)
#             plt.show()
#             break
#     else:
#         print(f"No data found for {target_date}.")



#To read data from a specific date and print only selected values (e.g., temperatures):
# import csv
# filename = "sitka_weather_07-2014.csv"
# target_date = '2014-7-2'  # change to any day you want

# with open(filename, 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         # .strip() closes the spaces in column_header names and values
#         clean_row = {key.strip(): value.strip() for key, value in row.items()}

#         if clean_row['AKDT'] == target_date:
#             print(f"Weather data for {target_date}:")
#             for key, value in clean_row.items():
#                 print(f"{key}: {value}")
#                 print("High Temp:", clean_row['Max TemperatureF'])
#                 print("Mean Temp:", clean_row['Mean TemperatureF'])
#                 print("Low Temp:", clean_row['Min TemperatureF'])
#             break
#     else:
#         	print(f"No data found for {target_date}.")

#Error-Checking: Sometimes, data amay not be complete. Missing data can result in exceptions that
# crash our programs if we don’t handle them properly. To address this issue, we’ll run errorchecking
# code when the values are being read from the CSV file to handle
# exceptions that might arise when we parse our data sets.

# filename = 'death_valley_2014.csv'
# with open(filename) as f:
# 	reader = csv.reader(f)
# 	header_row = next(reader)
# 	dates, highs, lows = [], [], []
# 	for row in reader:
# 		try:
# 			current_date = datetime.strptime(row[0], "%Y-%m-%d")
# 			high = int(row[1])
# 			low = int(row[3])
# 		except ValueError:
# 			print(current_date, 'missing data')
# 		else:
# 			dates.append(current_date)
# 			highs.append(high)
# 			lows.append(low)
# # Plot data.
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates, highs, c='red')
# plt.plot(dates, lows, c='blue')

# # Format plot.
# title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
# plt.title(title, fontsize=20)


#DIY
# Choose any location you’re interested in, and make a visualization that plots its rainfall. 
# Start by focusing on one month’s data, and then once your code is working, run it for a full year’s 
# data.

# import csv
# from datetime import datetime
# import matplotlib.pyplot as plt
# filename = 'weather.csv'
# #target_date = '2016-01-02'  # change to any day you want

# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)

#     dates, highs, lows, avg = [], [], [], []
#     for row in reader:
#         try:
#             current_date = datetime.strptime(row[0], "%Y-%m-%d")
#             high = int(row[9])
#             low = int(row[10])
#             avg = int(row[8])
#         except ValueError:
#             print(current_date, 'missing data')
#         else:
#             dates.append(current_date)
#             highs.append(high)
#             lows.append(low)

# # Plot data.
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates, highs, c='red', alpha=0.5)
# plt.plot(dates, lows, c='blue', alpha=0.5)
# plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# # Format plot.
# title = "Weather data over a period"
# plt.title(title, fontsize=12)
# plt.xlabel('', fontsize=8)
# fig.autofmt_xdate()
# plt.ylabel("Temperature (F)", fontsize=8)
# plt.tick_params(axis='both', which='major', labelsize=8)

# plt.show()



# 
