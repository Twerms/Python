from re import L


class Pirate():
    '''Create a future king of the pirates build.'''
    def __init__(self, name, age, fruit):
        '''Set the pirate's name, age, fruit'''
        self.name = name
        self.age = age
        self.fruit = fruit
    def awakened_fruit(self):
        '''Simulate the pirate awakening his/her devil fruit.'''
        print(self.name.title() + "'s devil fruit, " + self.fruit + ', has awakened!')
mugiwara = Pirate('luffy', 19, 'hito hito no mi')
mugiwara.awakened_fruit()
print('\n')

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.name + " is a popular restaurant known for it's " + self.cuisine_type + '.')
    def open_restaurant(self):
        print(self.name + ' is now open.')
food_place = Restaurant('Red Lobsters', 'sea food')
print('I love going to ' + food_place.name + ' because I love eating ' + food_place.cuisine_type + '!')
food_place = Restaurant('Grill Masters BBQ', 'barbeque')
print('We should go to ' + food_place.name + '.')
food_place.describe_restaurant()
print('\n')

class User():
    def __init__(self, first_name, last_name, age, gender):
        '''Display the first name, last name, age, height, and weight of the user.'''
        self.full_name = first_name.title() + ' ' + last_name.title()
        self.age = age
        self.gender = gender
    def describe_user(self):
        '''Summary of the user's information'''
        user_description = "This user's name is " + self.full_name.title() + ', is ' + str(self.age) + ' years old and is ' + self.gender + '.'
        return user_description
    def greet_user(self):
        '''Print a personalized greeting to the user.'''
        if self.gender == 'male':
            print('Welcome back, King ' + self.full_name.title() + '!')
        elif self.gender == 'female':
            print('Welcome back, Queen ' + self.full_name.title() + '!')
person = User('Francis', 'Belocura', 19, 'male')
person.describe_user()
person.greet_user()
print('\n')

class User():
    def __init__(self, first_name, last_name, age, gender):
        '''Display the first name, last name, age, height, and weight of the user.'''
        self.full_name = first_name.title() + ' ' + last_name.title()
        self.age = 0
        self.gender = gender
    def describe_user(self):
        '''Summary of the user's information'''
        user_description = "This user's name is " + self.full_name.title() + ', is ' + str(self.age) + ' years old and is ' + self.gender + '.'
        return user_description
    def greet_user(self):
        '''Print a personalized greeting to the user.'''
        if self.gender == 'male':
            print('Welcome back, King ' + self.full_name.title() + '!')
        elif self.gender == 'female':
            print('Welcome back, Queen ' + self.full_name.title() + '!')
person = User('Francis', 'Belocura', 19, 'male')
person.age = 20
print(person.describe_user())
person.greet_user()
print('\n')

class User():
    def __init__(self, first_name, last_name, age, gender):
        '''Display the first name, last name, age, height, and weight of the user.'''
        self.full_name = first_name.title() + ' ' + last_name.title()
        self.age = 0
        self.gender = gender
    def describe_user(self):
        '''Summary of the user's information'''
        user_description = "This user's name is " + self.full_name.title() + ', is ' + str(self.age) + ' years old and is ' + self.gender + '.'
        return user_description
    def greet_user(self):
        '''Print a personalized greeting to the user.'''
        if self.gender == 'male':
            print('Welcome back, King ' + self.full_name.title() + '!')
        elif self.gender == 'female':
            print('Welcome back, Queen ' + self.full_name.title() + '!')
    def update_age(self, new_age):
        '''Set a new value for the age.'''
        self.age = new_age
    def increment_age(self, added_age):
        '''Add a given amount to the age.'''
        self.age += added_age
person = User('Francis', 'Belocura', 19, 'male')
person.update_age(20)
person.increment_age(2)
print(person.describe_user())
person.greet_user()
print('\n')

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(self.name + " is a popular restaurant known for it's " + self.cuisine_type + '.')
    def open_restaurant(self):
        print(self.name + ' is now open.')
    def update_number_served(self):
        self.number_served = 20
restaurant = Restaurant('Red Lobsters', 'sea food')
restaurant.update_number_served()
restaurant.describe_restaurant()
print('This restaurant has served ' + str(restaurant.number_served) + ' people today.')
print('\n')

class User():
    def __init__(self, first_name, last_name, age, gender):
        '''Display the first name, last name, age, height, and weight of the user.'''
        self.full_name = first_name.title() + ' ' + last_name.title()
        self.age = 0
        self.gender = gender
        self.login_attempts = 1
    def describe_user(self):
        '''Summary of the user's information'''
        user_description = "This user's name is " + self.full_name.title() + ', is ' + str(self.age) + ' years old and is ' + self.gender + '.'
        return user_description
    def greet_user(self):
        '''Print a personalized greeting to the user.'''
        if self.gender == 'male':
            print('Welcome back, King ' + self.full_name.title() + '!')
        elif self.gender == 'female':
            print('Welcome back, Queen ' + self.full_name.title() + '!')
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
login_tries = User('Francis', 'Belocura', 19, 'male')
login_tries.increment_login_attempts()
print('Login Attempts: ' + str(login_tries.login_attempts))
login_tries.reset_login_attempts()
print('Login Attempts: ' + str(login_tries.login_attempts))
login_tries.increment_login_attempts()
print('Login Attempts: ' + str(login_tries.login_attempts))
print('\n')

class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        print(self.name + " is a popular restaurant known for it's " + self.cuisine_type + '.')
    def open_restaurant(self):
        print(self.name + ' is now open.')
    def update_number_served(self):
        self.number_served = 20
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []
    def display_flavors(self):
        print('Here are the flavors available:')
        for flavor in self.flavors:
            print(flavor.title())
ice_cream_restaurant = IceCreamStand('Infinity Conez', 'Ice Cream')
ice_cream_restaurant.flavors = ['vanilla', 'rocky road', 'chocolate', 'strawberry']
ice_cream_restaurant.display_flavors()
print('\n')

class User():
    def __init__(self, first_name, last_name, age, gender):
        '''Display the first name, last name, age, height, and weight of the user.'''
        self.full_name = first_name.title() + ' ' + last_name.title()
        self.age = 0
        self.gender = gender
        self.login_attempts = 1
    def describe_user(self):
        '''Summary of the user's information'''
        user_description = "This user's name is " + self.full_name.title() + ', is ' + str(self.age) + ' years old and is ' + self.gender + '.'
        return user_description
    def greet_user(self):
        '''Print a personalized greeting to the user.'''
        if self.gender == 'male':
            print('Welcome back, King ' + self.full_name.title() + '!')
        elif self.gender == 'female':
            print('Welcome back, Queen ' + self.full_name.title() + '!')
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
class Admin(User):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges()
class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        print('Privileges:')
        for privilege in self.privileges:
            print(privilege)
francis = Admin('Francis', 'Belocura', 19, 'male')
francis_privileges = ['Can Add Post', 'Can Delete Posts', 'Can Ban Users']
francis.privileges.privileges = francis_privileges
francis.privileges.show_privileges()
print('\n')

from collections import OrderedDict
random_list = OrderedDict()
random_list['hello'] = 'hi'
random_list['goodbye'] = 'bye'
random_list['pewdiepie'] = 'friday with pewdiepie!'
for key, value in random_list.items():
    print(key + ', ' + value)
print('\n')

from random import randint
class Die:
    def __init__(self, sides = 6):
        self.sides = sides
    def roll_dice(self):
        return randint(1, self.sides)
class Ten_Sided_Die(Die):
    def __init__(self, sides=6):
        super().__init__(sides)
        self.sides = 10
d6 = Die()
results = []
for roll_num in range(10):
    result = d6.roll_dice()
    results.append(result)
print(results)
d10 = Ten_Sided_Die()
results = []
for roll_num in range(10):
    result = d10.roll_dice()
    results.append(result)
print(results)

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
print('\n')

class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185           
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    def upgrade_battery(self):
        if self.battery_size == 60:
            self.battery_size = 85
            print('Battery size upgraded.')
        elif self.battery_size == 85:
            print('The battery has already been upgraded')
class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""
    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery() 
print("Original electric car's battery size:")
ec_specs = ElectricCar('Tesla', 'Model X', '2022')
ec_specs.battery.describe_battery()
ec_specs.battery.get_range()
print("\nUpgraded electric car's battery size:")
ec_specs.battery.upgrade_battery()
ec_specs.battery.describe_battery()
ec_specs.battery.get_range()
print('\nUpgrading the battery a second time:')
ec_specs.battery.upgrade_battery()
ec_specs.battery.describe_battery()
ec_specs.battery.get_range()
print('\n')

import time
presidents = []
startTime = time.time() #when time.time() is called it gives the exact seconds of when it was called since 1970
while len(presidents) != 3 and  time.time() - startTime < 3: 
  #subtracting time.time() by startTime, we get seconds passed since startTime was first created, therefore allowing us to keep track of time passed in the program
  president = input("You have 3 seconds to name 3 presidents: ")
  presidents.append(president)
print("Time's Over! The presidents you named were: ")
for president in presidents:
  print (president.title())    