filename = input('What is the filename? ')

with open(filename) as file:
    for name in file:
        print(name)
