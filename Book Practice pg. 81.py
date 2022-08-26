answer = input('3+3= ')
if answer == '6':
    print('Correct answer. Congrats, you are a nerd!')
else:
    print('No. Why are you so stupid?')

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
car = 'toyota'
print("\nIs car == 'toyota'? I predict True.")
print(car == 'toyota')

food = ['chicken', 'apple', 'brocolli', 'rice']
fave_food = input('What food item are you looking for? ')
if fave_food.lower() in food:
    print('We do have ' + fave_food.lower() + ' in our list.')
else:
    print('Sorry but that item is not on our list.')
    
human_years = input('How old are you? ')
human_years = int(human_years)
print('You would be ' + str(round(human_years/7)) + ' in dog years.')

alien_color = ['green']
if 'green' in alien_color:
    print('\nYou just earned 5 points!')
    
alien_color = ['red']
if 'green' in alien_color:
    print('\nYou just earned 5 points!')   
    
alien_color = ['red']
if 'green' in alien_color:
    print('\nYou just earned 5 points!')
elif 'yellow' in alien_color:
    print('\nYou just earned 10 points!')
elif 'red' in alien_color:
    print('\nYou just earned 10 points!')

alien_color = ['red']
if 'green' in alien_color:
    print('\nYou just earned 5 points!')
else:
    print('\nYou just earned 10 points!')
    
age = int(input('How old are you? '))
if age < 2:
    print('\nYou are a baby.')
elif age < 4:
    print('\nYou are a toddler.')
elif age < 13:
    print('\nYou are a kid.')
elif age < 20:
    print('\nYou are a teenager.')
elif age < 65:
    print('\nYou are an adult.')
else:
    print('\nYou are an elder.')
    
users = []
if users:
    for user in users:
        if user == 'admin':
            print('\nHello admin, would you like to see a status report?')
        else:
            print('\nHello ' + user + ', thank you for logging in!')
else:
    print('We need to find more users!')
    
current_users = ['Kenneth', 'Chris', 'Francis', 'Axel', 'Andrew']
new_users = ['Kenneth', 'Sou', 'Francis', 'Leah', 'Chong']
for new_user in new_users:
    if new_user in current_users:
        print('\nYou will need to enter a new username.')
    else:
        print('\nThat username is available.')
numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")
        
