from ast import excepthandler
from multiprocessing.sharedctypes import Value


#filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''    
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
print('\n')

#filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string2 = ''
for line in lines:
    pi_string2 += line.strip()
print(pi_string2[:5])
print(len(pi_string2[:5]))
print('\n')

#filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
birthday = input('Is your birthday (mmddyy) in the first 150 digits of made-up pi? ')
if birthday in pi_string:
    print('Your birthday is in the first 150 digits of made-up pi!')
else: 
    print('Unfortunately, your birthday is in not the first 150 digits of made-up pi.')
print('\n')

#file_name = 'learning_python.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
lp_string = ''
for line in lines:
    lp_string += line
print(lp_string.replace('Python', 'C'))
print('\n')

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write('I love programming!\n')
    file_object.write('I love creating new games!\n')
with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets!\n')
    file_object.write('I love creating apps that can run in a browser!\n')
print('\n')

#filename = 'guest.txt'
with open(filename, 'w') as gt:
    name = input('What is your name? ')
    gt.write('Guest name: ' + name.title())

#filename = 'guest_book.txt'
with open(filename, 'a') as gbt:
    while True:
        name = input('Please enter all the names checking in.\nEnter quit if finished: ')
        if name == 'quit':
            break
        else:
            gbt.write('Hello ' + name.title() + ", you've been added to the guest book.\n")
print('\n')
        
#filename = 'why_programming.txt'
with open(filename, 'a') as  wp:
    while True:
        who = input('What is your name? ')
        if who == 'quit':
            break
        else:
            wp.write('Name: ' + '\n\t' + who.title() + '\n')
        why = input('Why do you like programming? ')
        if why == 'quit':
            break
        else:
            wp.write('Why ' + who.title() + ' likes programming: ' + '\n\t' + why + '\n') 
            
try:
    print(5/0)
except ZeroDivisionError:
    print('You can not divide by zero!')
print('\n')
    
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You can not divide by zero!')
    else:
        print(answer)
print('\n')
        
#filename = 'learning_python.txt'
try:
    with open(filename) as lpt:
        lines = lpt.readlines()
except FileNotFoundError:
    message = 'Sorry the file ' + lpt + 'does not exist.'
    print(message)

title = "Alice in Wonderland"
print(title.split())
print('\n')

#filename = 'alice.txt'
try:
    with open(filename) as alice:
        lines = alice.read()
except FileNotFoundError:
    msg = 'Sorry the file ' + alice + 'does not exist.'
    print(msg)
else:
    #Count the amount of words in the file.
    words = lines.split()
    num_words = str(len(words))
    print("The file " + filename + " has about " + num_words + " words.")
print('\n')
    
#def count_words(filename):
    '''Count the approximate number of words in a file.'''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = 'Sorry, the file ' + filename + ' does not exist.'
        print(msg)
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = str(len(words))
        print('The file ' + filename + ' has about ' + num_words + ' words.')
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
print('\n')

#def count_words(filename):
    '''Count the approximate number of words in a file.'''
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = str(len(words))
        print('The file ' + filename + ' has about ' + num_words + ' words.')
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
print('\n')

print("Enter 'q' at any time to quit.")
while True:
    try:
        first_number = int(input('First number: '))
        if first_number == 'q':
            break
        second_number = int(input('Second number: '))
        if second_number == 'q':
            break
    except ValueError:
        print('Both numbers have to be integers. Try again.')    
    else:
        sum = first_number + second_number
        print(sum)

