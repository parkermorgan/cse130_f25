# 1. Name:
#      Parker Morgan
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      The program takes an array of data values from a JSON file. It sorts the
#      array in ascending order using a selection sort and prints each item 
#      from the list one line at a time, and is sorted alphabetically or 
#      numerically depending on the provided data. The program also has
#      multiple 'assert' statements to check for possible bugs in the selecting
#      and sorting of the JSON file. 
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was figuring out where to put the 'assert' 
#      statements that would make the most sense. Translating my pseudocode to 
#      Python was relatively easy, but I had to go back and review asserts
#      to remember exactly how to put them in. 
# 5. How long did it take for you to complete the assignment?
#      This assignment took be a little less than 2 hours. 


import json

def array_sort(array):
    assert (
    all(isinstance(x, type(array[0])) for x in array)
    ), 'All elements must be the same type.'

    i_check = len(array) - 1

    while i_check > 0:
        max_index = 0
        max_value = array[0]

        for i in range(1, i_check + 1):
            if array[i] > max_value:
                max_value = array[i]
                max_index = i

        array[i_check], array[max_index] = array[max_index], array[i_check]
        i_check -= 1

    for value in array:
        print(f'\t{value}')


user_file = input("What is the name of the file? ")

assert user_file.endswith('.json'), 'Invalid file, must use JSON.'
with open(user_file, "r") as file:
    data = json.load(file)

assert 'array' in data, 'File does not have a key named "array."'
assert isinstance(data['array'], list), '"array" must be a list.'

array = data['array']
assert len(array) > 0, 'Array cannot be empty.'

print(f'The values in {user_file} are:')

array_sort(array)