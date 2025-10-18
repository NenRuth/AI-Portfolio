"""Inheritance means a class can “inherit” or reuse attributes and methods from another class.
Real-Life Analogy
Think of a Parent–Child relationship:
The Parent (base class) has some characteristics (e.g. eyes, height).
The Child (subclass) inherits those automatically (no need to rewrite them).
The child can also have extra features or behave differently.



#Create a Parent Class (base class)"""
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print("My name is " + self.name + " and I am " + str(self.age) + " years old.")


# #Create a subclass
# class Student(Person):
#     def __init__(self, name, age, grade):
#         # Call the parent class constructor using super()
#         super().__init__(name, age)
#         self.grade = grade

#     def study(self):
#         print(self.name + " is studying for grade " + str(self.grade) + ".")

# #Create Instances
# p1 = Person("Mrs. Obi", 40)
# s1 = Student("Ada", 14, 8)


#Use the Methods
# p1.introduce()  
# s1.introduce()   # This is so cos it can use info inherited from p1
# s1.study()       


#Overriding Methods from the Parent Class: If the child wants to change how something works, 
#it can override it. To do this, you define a method in the child class with the same name as the
#method you want to override in the parent class.

# class Student(Person):
#     def introduce(self):
#         print(f"My name is {self.name}, I'm {self.age}, and I’m a student!")
# s1.introduce()


#multiple subclass
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def start_engine(self):
        print("The " + self.brand + self.model + "engine has started.")

    def stop_engine(self):
        print(f"The {self.brand} {self.model} engine has stopped.")


class Car(Vehicle):   #inherits from Vehicle with an additional attribute, door.
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)  # collects attributes from parent class
        self.doors = doors

    def open_trunk(self):
        print("The trunk of the " + self.brand + self.model  + "is now open.")


class Bus(Vehicle):  #with an additional attribute, capacity.
    def __init__(self, brand, model, year, capacity):
        super().__init__(brand, model, year)
        self.capacity = capacity

    def pick_passengers(self):
        print(f"The {self.brand} {self.model} is picking up {self.capacity} passengers.")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def wheelie(self):
        print(f"The {self.brand} {self.model} does a wheelie!")


#Creating Instances (Objects)
car1 = Car("Toyota", "Camry", 2022, 4)
bus1 = Bus("Mercedes", "Sprinter", 2021, 20)
bike1 = Motorcycle("Yamaha", "R1", 2023, False)


#Calling Methods
car1.start_engine()      # Inherited from Vehicle
car1.open_trunk()        # From Car

bus1.start_engine()      # Inherited from Vehicle
bus1.pick_passengers()   # From Bus

bike1.start_engine()     # Inherited from Vehicle
bike1.wheelie()          # From Motorcycle






#Instances as Attributes
