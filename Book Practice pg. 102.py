from typing import OrderedDict


alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("\nOriginal x-position: " + str(alien_0['x_position']))
#move to right
#how far based on current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("\nNew x-position: " + str(alien_0['x_position']))

francis = {
    'first_name': 'Francis Clarence', 
    'last_name': 'Belocura', 
    'age': 19, 
    'city': 'Clovis'
    }
print("Francis' age is " + str(francis['age']) + '.')
for key, value in francis.items():
    print('\nKey: ' + str(key).title())
    print('Value: ' + str(value).title() + '\n')
    
rivers = {'nile': 'egypt', 'mississippi':'mississippi', 'amazon': 'peru'}
for key, value in rivers.items():
    print('The ' + key.title() + ' River flows through ' + value.title() + '.')
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c', 
    'edward': 'ruby',
    'phil': 'python'
}
should_take = ['jen', 'sarah', 'francis', 'kenneth']
for people in should_take:
    if people in favorite_languages.keys():
        print('\nThank you for responding to the poll, ' + people.title() + '!')
    else:
        print('\nPlease take the poll, ' + people.title() + '.\n')
        
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print('Total number of aliens: ' + str(len(aliens)))

# random prompt i thought of
print('\nHow many letters in the word?')
word = input('What word are you thinking of? ')
print('The word "' + word + '" has ' + str(len(word)) + ' letters.') 

people = {
    'francis': {
        'first_name': 'Francis Clarence', 
        'last_name': 'Belocura', 
        'age': 19, 
        'city': 'Clovis'
    },
    'kenneth': {
        'first_name': 'Kenneth',
        'last_name': 'Castillo',
        'age': 18,
        'city': 'Clovis'
    },
    'Andrew': {
        'first_name': 'Andrew',
        'last_name': 'Carter',
        'age': 18,
        'city': 'Clovis'
    }
    }
for key, value in people.items():
    print('\nUser: ' + key.title())
    full_name = value['first_name'] + ' ' + value['last_name']
    age = value['age']
    location = value['city']

    print(key.title() + "'s details:")
    print('\tFull name: ' + full_name)
    print('\tAge: ' + str(age))
    print('\tLocation: ' + location)    
pets = {
    'ryu': {
        'name': 'Ryu',
        'breed': 'Labrador',
        'age': 4
    },
    'ayumi': {
        'name': 'Ayumi',
        'breed': 'Goldren Retreiver',
        'age': 3
    },
    'britney': {
        'name': 'Britney',
        'breed': 'German Shepherd',
        'age': 3
    }
}
for name, details in pets.items():
    print('\nThese are the details for ' + name.title() + ':')
    print('\tName: ' + details['name'])
    print('\tBreed: ' + details['breed'])
    print('\tAge: ' + str(details['age']))
