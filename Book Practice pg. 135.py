from re import L
from xml.dom import ValidationErr


def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
greet_user('francis')

def make_shirt(size='large', text='I love Python'):
    """Display size and text message of shirt,"""
    print('\nThe size of the shirt is ' + size + '.')
    print('The message on the shirt says ' + '"' + text + '."')
make_shirt()

def describe_city(city, country):
    """Displays a city and country it's from."""
    print('\n' + city.title() + ' City is in ' + country.title() + '.')
describe_city('cebu', 'the philippines')

def get_formatted_name(first_name, last_name):
    '''Return a full name, neatly formatted.'''
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print('\n' + musician)

def city_country(city, country):
    '''Return the city and it's country in that order.'''
    formatted_name = '"' + city.title() + ', ' + country.title() + '"'
    return formatted_name
place = city_country('cebu city', 'Philippines')
print('\n' + place)
place = city_country('jakarta', 'indonesia')
print(place)

def make_album(album, artist):
    '''Display an artist and an album of theirs.'''
    album_artist = {
        'Album Title': album.title(),
        'Artist Name': artist.title()
    }
    return album_artist
album_by_artist = make_album('an evening with silk sonic', 'silk sonic')
print('\n' + str(album_by_artist))
album_by_artist = make_album('presenting the fabulous ronnettes', 'the ronnettes')
print(album_by_artist)

def make_album(album, artist):
    '''Display an artist and an album of theirs.'''
    album_artist = {'Album Title': album.title(),'Artist Name': artist.title()}
    return album_artist
while True:
    print('\nWhat is your favorite album?')
    print('Enter "quit" anytime to stop the program.')
    album = input('What album are you thinking of? ')
    if album == 'quit':
        break
    artist = input('Which artist created the album? ')
    if artist == 'quit':
        break
    artist_title = make_album(album, artist)
    print(artist_title)
print('\n')

def greet_users(names):
    '''Greet users listed.'''
    for name in names:
        print("Hi it's nice to have you back, " + name + '!')
usernames = ['Francis', 'Kenneth', 'Andrew', 'Parker']
greet_users(usernames)
print('\n')

def print_models(unprinted_models, completed_models):
    '''Simulate printing each unprinted model unti none are left.'''
    while unprinted_models:
        currently_modeled = unprinted_models.pop()
        print('Currently printing: ' + currently_modeled)
        completed_models.append(currently_modeled)
def show_completed_models(completed_models):
    '''Show all models were printed.'''
    print('The following models have finished printing:')
    for completed_model in completed_models:
        print(completed_model)
unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron', 'luffy figure']
completed_models = []
print('List of models to print: ' + str(unprinted_models))
print_models(unprinted_models[:], completed_models)
show_completed_models(completed_models)
print('\n')

def CountFrequency(my_list):
    freq = {}
    for items in my_list:
        freq[items] = my_list.count(items)    
    for key, value in freq.items():
        print (str(key) + ': ' + str(value))
my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
CountFrequency(my_list)
print('\n')

def show_magicians(magicians):
    '''Print the name of each magician on the list'''
    for magician in magicians:
        print('Introducing to the stage, ' + magician.title() + '!')
magicians = ['david blaine', 'criss angel', 'houdini', 'pip the magic dragon']
show_magicians(magicians)
print('\n')

def make_great(magicians):
    '''Add the phrase "the Great" to the magicians' names.'''
    for magician in magicians:
        print('The Great ' + magician.title() + '!')
magicians = ['david blaine', 'criss angel', 'houdini', 'pip the magic dragon']
make_great(magicians)
print('\n')

def make_great(magicians):
    '''Add the phrase "the Great" to the names by making a new list'''
    great_magicians = []
    while magicians:
        great_magician = 'The Great ' + magicians.pop() 
        great_magicians.append(great_magician)
    for great_magician in great_magicians:
        magicians.append(great_magician)
magicians = ['David Blaine', 'Criss Angel', 'Houdini', 'Pip the Magic Dragon']
make_great(magicians)
show_magicians(magicians)

def show_magicians(magicians):
    '''Print the name of each magician on the list'''
    for magician in magicians:
        print('Introducing to the stage, ' + magician.title() + '!')
magicians = ['david blaine', 'criss angel', 'houdini', 'pip the magic dragon']
show_magicians(magicians)
print('\n')



def make_great(magicians):
    '''Add the phrase "the Great" to the names by making a new list and keeping the original list'''
    great_magicians = []
    while magicians:
        great_magician = 'The Great ' + magicians.pop() 
        great_magicians.append(great_magician)
    for great_magician in great_magicians:
        magicians.append(great_magician)
    return magicians
magicians = ['David Blaine', 'Criss Angel', 'Houdini', 'Pip the Magic Dragon']
print('\nGreat Magicians: ')
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)
print('\nOriginal Magicians: ')
show_magicians(magicians)
print('\n')

question = 'What toppings would you like on your pizza? '
def make_pizza(toppings, finished_toppings):
    '''Display what toppings are being selected by customer.'''
    active = True
    while active:
        request = input(question)
        toppings.append(request)
        for topping in toppings:
            if topping == 'quit':
                active = False
            else:
                print('Adding: '+ str(topping))
        if topping != 'quit':
            removed_toppings = toppings.pop()
            finished_toppings.append(removed_toppings)
def final_toppings(finished_toppings):
    '''Display what toppings are being added to the pizza.'''
    print('The following have been added to your pizza:')
    for finished_topping in finished_toppings:
        print(finished_topping.title())
toppings = []
finished_toppings = []
make_pizza(toppings, finished_toppings)
final_toppings(finished_toppings)

def make_profile(name, age, **user_info):
    '''Display information of the user for their profile'''
    profile = {}
    profile['Name:'] = name.title()
    profile['Age:'] = age
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = make_profile('jack', '19', Height= '160 cm', weight= '160 lbs')
print(user_profile)