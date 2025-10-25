#Extracting Data Using JSon

# import json

# # Load the data into a list.
# filename = 'population_data.json'
# with open(filename) as f:
# 	pop_data = json.load(f)  #store the data. The json.load() function converts the data into a format Python can work with: in this case, a list.

# # Print the 2010 population for each country.
# for pop_dict in pop_data:  #loop through each item in pop_data, store each dictionary in pop_dict.
# 	if pop_dict['Year'] == '2010':
# 		country_name = pop_dict['Country Name']
# 		population = pop_dict['Value']
# 		print(country_name + ": " + population)


#this prints for a particular country, the year and population. 
# import json
# filename = 'population_data.json'
# with open(filename) as f:
# 	pop_data = json.load(f)
# for pop_dict in pop_data:
# 	if pop_dict['Country Name'] == 'Nigeria':
# 		country_name = pop_dict['Country Name']
# 		population = pop_dict['Value']
# 		year = pop_dict['Year']
# 		print(country_name + ': ' + population + ', ' + year + '.')

# import json
# filename = 'population_data.json'
# with open(filename) as f:
# 	pop_data = json.load(f)
# for pop_dict in pop_data:
# 	if pop_dict['Year'] == '2010' and pop_dict['Country Name'] == 'Nigeria':
# 		#country_name = pop_dict['Country Name']
# 		population = pop_dict['Value']
# 		#year = pop_dict['Year']
# 		print(population)

# Converting Strings into Numerical Values
# Every key and value in population_data.json is stored as a string. To work with the population data, 
# we need to convert the population strings to numerical values. We do this using the int() function. 

# import json
# filename = 'population_data.json'
# with open(filename) as f:
# 	pop_data = json.load(f)
# for pop_dict in pop_data:
# 	if pop_dict['Year'] == '2010' and pop_dict['Country Name'] == 'Nigeria':
# 		#country_name = pop_dict['Country Name']
# 		population = int(pop_dict['Value'])
# 		#year = pop_dict['Year']
# 		print(population)

# import json
# filename = 'population_data.json'
# with open(filename) as f:
# 	pop_data = json.load(f)
# for pop_dict in pop_data:
# 	if pop_dict['Country Name'] == 'Nigeria':
# 		country_name = pop_dict['Country Name']
# 		population = int(pop_dict['Value'])
# 		year = int(pop_dict['Year'])
# 		print(country_name + ': ' + str(population) + ', ' + str(year) + '.')

#some of the numbers contains a decimal and can give an error response when outputing. To correct it, 
#convert the string to a float and then convert that float to an integer. 

# import json
# filename = 'population_data.json'
# with open(filename) as f:
# 	pop_data = json.load(f)
# for pop_dict in pop_data:  
# 	if pop_dict['Year'] == '2010':
# 		country_name = pop_dict['Country Name']
# 		population = int(float(pop_dict['Value']))  #The float() function turns the string into a decimal, and the int() function drops the decimal part of the number and returns an integer.
# 		print(country_name + ": " + str(population))


# import json
# from pygal.i18n import COUNTRIES
# for country_code in sorted(COUNTRIES.keys()):
# 	print(country_code, COUNTRIES[country_code])


# from pygal.i18n import COUNTRIES
# def get_country_code(country_name):
# 	"""Return the Pygal 2-digit country code for the given country."""
# 	for code, name in COUNTRIES.items():
# 		if name == country_name:
# 			return code
# # If the country wasn't found, return None.
# 	return None
# print(get_country_code('Andorra'))
# print(get_country_code('United Arab Emirates'))
# print(get_country_code('Afghanistan'))



# from pygal.i18n import COUNTRIES
# print(COUNTRIES['us'])


# import pygal
# wm = pygal.Worldmap()
# wm.title = 'North, Central, and South America'
# wm.add('North America', ['ca', 'mx', 'us'])
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
# 	'gy', 'pe', 'py', 'sr', 'uy', 've'])
# wm.render_to_file('americas.svg')

# import pygal

# # Define your own country dictionary
# COUNTRIES = {
#     'us': 'United States',
#     'gb': 'United Kingdom',
#     'fr': 'France',
#     'de': 'Germany'
# }

# # Example: create a simple bar chart
# bar_chart = pygal.Bar()
# bar_chart.title = 'Sample Country Data'
# for code, name in COUNTRIES.items():
#     bar_chart.add(name, [len(name)])  # just example data

# bar_chart.render_in_browser()  # opens chart in your browser


# import pygal

# # Simple country dataset
# COUNTRIES = {
#     'us': 'United States',
#     'gb': 'United Kingdom',
#     'fr': 'France',
#     'de': 'Germany',
#     'cn': 'China',
#     'jp': 'Japan',
#     'in': 'India'
# }

# # Example data for each country
# data = {
#     'us': 100,
#     'gb': 50,
#     'fr': 80,
#     'de': 60,
#     'cn': 120,
#     'jp': 90,
#     'in': 110
# }

# # Use a Bar chart to represent countries (workaround for "world map")
# bar_chart = pygal.Bar()
# bar_chart.title = 'Sample Country Data'

# for code, name in COUNTRIES.items():
#     bar_chart.add(name, [data[code]])

# # Option 1: render in browser (needs lxml)
# bar_chart.render_in_browser()

# # Option 2: render to SVG file (no lxml needed)
# #bar_chart.render_to_file('world_chart.svg')

