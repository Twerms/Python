for numbers in range(1,21):
    print(numbers)
print('\n')
    
hundreds = []
for hundred in range(1,101):
    hundreds.append(hundred)
print(str(hundreds) +'\n')
    
numbers = []
for number in range(1,21,2):
    numbers.append(number)
print(str(numbers)+'\n')
    
tens = list(range(1,11))
biggest = max(tens)
addedup = sum(tens)
print(biggest)
print(str(addedup)+'\n')

cubes = []
for cube in range(1,11):
    cubes.append(cube**3)
print(cubes)

cubes = [cube**3 for cube in range(1,11)]
print(str(cubes)+'\n')

list = []
for number in range(1,11):
    list.append(number+1)
    print('This is line #' + str(number) + '.')


