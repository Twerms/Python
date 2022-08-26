repeater = 'Tell me something and I will repeat it back to you: '
repeater += '\nEnter "quit" to end the program. '
message = ""
while message != 'quit':
    message = input(repeater)
    print(message)
    
repeater = 'Tell me something and I will repeat it back to you: '
repeater += '\nEnter "quit" to end the program. '
active = True
while active:
    message = input(repeater)
    if message == 'quit':
        active = False
    elif message == 'no more':
        active = False
    else:     
        print(message)

prompt = '\nPlease enter the name of a city you have visited:'
prompt += "\n(Enter 'quit' when you are finished.) "  
while True:
    answer = input(prompt)
    if answer == 'quit':
        break
    else:
        print('I would love to go to ' + answer.title() + '!')
        
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
    
x = 1
while x <= 10:
    print(x)
    x += 1
    
topping = 'Enter the toppings you want on your pizza.'
topping += '\nType "quit" if you are finished. '
while True:
    answer = input(topping)
    if answer == 'quit':
        break
    else:
        print(answer.title() + ' has been added to you pizza.')
    
age = 'Enter your age: '
age += '\nType "quit" if finished. '
while True: 
    answer = input(age)
    if answer == 'quit':
        break
    answer = int(answer)
    if answer < 3:
        print('Your ticket is free!')
    elif answer <= 12:
        print('Your ticket is $10.')
    elif answer > 12:
        print('Your ticket is $15.')

age = 'Enter your age: '
age += '\nType "quit" if finished. '
active = True 
while active: 
    answer = input(age)
    if answer == 'quit':
        active = False
    else:
        answer = int(answer)
        if answer < 3:
            print('Your ticket is free!')
        elif answer <= 12:
            print('Your ticket is $10.')
        elif answer > 12:
            print('Your ticket is $15.\n')
            
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print('Verifying user: ' + current_users.title())
    confirmed_users.append(current_users)
print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
responses = {}
polling_active = True
while polling_active:
    name = input('\nWhat is your name? ')
    response = input('Which mountain would you like to climb someday? ')
    responses[name] = response
    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        polling_active = False
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(name + ' would like to climb ' + response + '.\n')

sandwich_orders = ['ham', 'pastrami', 'deli', 'pastrami', 'tuna', 'pastrami']
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print('I made your ' + made_sandwich + '.')
    finished_sandwiches.append(made_sandwich)
print('\nHere are the sandwhiches made:')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title() + ' Sandwich')
    
weight = input('\nHow much do you weigh? ')
conversion = input('Lbs or Kgs? ')
if conversion.lower() == 'lbs':
    print('You are ' + str(float(int(weight)) * 0.454) + ' in kgs.')
if conversion.lower() == 'kgs':
    print('You are ' + str(float(int(weight)) / 0.454) + ' in lbs.')
    
youtuber_poll = {}
poll_active = True
while poll_active:
    name = input('\nWhat is your name? ')
    youtuber = input('Who is your favorite youtuber? ')
    youtuber_poll[name] = youtuber
    question = input('Is there another person wanting to answer the poll? (yes/no) ')
    if question == 'no':
        poll_active = False
print('\n---Youtuber Poll Results---')
for name, youtuber in youtuber_poll.items():
    print(name.title() + "'s favorite youtuber is " + youtuber + '.')
