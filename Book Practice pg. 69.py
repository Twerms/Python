food = ['hotdog', 'burger', 'pizza', 'icecream', 'fries']
print('The first three items in the list are:')
print(food[:3])

print('\nThe middle three items in the list are:')
print(food[1:4])

my_pizzas = ['Pepperoni_Pizza', 'Hawaiian_Pizza', 'Cheese_Pizza']
friend_pizzas = my_pizzas[:]
my_pizzas.append('Veggie_Pizza')
friend_pizzas.append('Buffalo_Pizza')
my_pizzas[3] = 'Meat_Pizza'
print('\nMy top 4 favorite pizzas are: ')
print(my_pizzas)
print("My friend's 4 favorite pizzas are: ")
print(friend_pizzas)
