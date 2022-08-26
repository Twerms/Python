filenames = ['cats.txt', 'dogs.txt']
try:
    for file in filenames:
        with open(file) as cd:
            meownbark = cd.read()
except FileNotFoundError:
    print("The file you finding is missing")
else:
    print(meownbark)