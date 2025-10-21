# class Restaurant():
# 	def __init__(self, name, cuisine):
# 		self.name = name
# 		self.cuisine = cuisine
# 	def describe_restaurant(self): 
# 		print('This is ' + self.name.title() + '. Their main cuisine is ' + self.cuisine + '.')
# 	def open_restaurant(self):
# 		print(self.name.title() + ' is open for business today!')
# food = Restaurant('delly', 'plain white sauce')
# print(food)

# food.describe_restaurant()
# food.open_restaurant()


# class IceCreamStand(Restaurant):
# 	def __init__(self, name, cuisine):
# 		super().__init__(name,cuisine)
# 		self.flavors = ['vanilla', 'chocolate', 'strawberry', 'mint', 'cookies and cream']

# 	def display_flavors(self):
# 		print('\n', self.name + 'offers the following flavors:')
# 		for flavor in self.flavors:
# 			print(flavor.title())

# Create an instance  
my_icecream_stand = IceCreamStand('Cool Treats', 'ice cream')
print(my_icecream_stand)

#call the method
my_icecream_stand.describe_restaurant()
my_icecream_stand.display_flavors()  		
