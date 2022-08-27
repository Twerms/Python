filenames = ['cats.txt', 'dogs.txt']
for file in filenames:
    try:
        with open(file) as cd:
            print('Reading file: ' + file)
            meownbark = cd.read()
    except FileNotFoundError:
        print("The file you finding is missing")
    else:
        print(meownbark + '\n')
print('\n')    
    
filenames = ['cats.txt', 'dogs.txt']
for file in filenames:
    try:
        with open(file) as cd:
            print('Reading file: ' + file)
            meownbark = cd.read()
    except FileNotFoundError:
        pass
    else:
        print(meownbark + '\n')
print('\n') 
        
import json
numbers = [1, 2, 3, 4, 5, 6]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
    print(numbers)
print('\n') 
            
import json
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input('What is your name? ')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back!")
else: 
    print("Welcome back " + username + "!")
print('\n') 
            
import json
def greet_user():
    '''Greet the user by name.'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input('What is your name? ')
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print('We will remember you next time!')
    else:
        print('Welcome back ' + username + "!")
greet_user()
print('\n') 
        
import json
def get_stored_username():
    '''Get stored username if available.'''
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    '''Prompt for new username'''
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back!")
greet_user()
