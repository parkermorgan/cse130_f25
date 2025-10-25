# 1. Name:
#      Parker Morgan
# 2. Assignment Name:
#      Lab 06: Image Compression
# 3. Assignment Description:
#      This program takes a JSON file containing compressed image data
#      and displays it to the user using '#' to represent filled pixels.
#      It reads the file as text, converts it into a usable object, and
#      extracts the necessary data. The program then creates a blank base
#      image, iterates through each column to determine whether each spot
#      is filled or blank, and prints the final image to the screen.
# 4. Algorithmic Efficiency
#      O(n), or linear effeciency. The processing time grows directly with the
#      amount of filled or blank value in the image. Each value is visited 
#      a set number of times while decoding and printing, making performance
#      proportional to input size. Doubling the image size roughly doubles the
#      time required to process it.
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part for me was figuring out how to create the base blank 
#      image and fill the values depending on the data in each column. I wasn't
#      very confident in the pseudocode I had created so I based my code off
#      of the example solution. 
# 6. How long did it take for you to complete the assignment?
#      This assignment overall took me around 3.5 hours, including review and 
#      revisions of my code. 

# Allow for json functionality.
import json

# Get and read file.
filename = input('What is the file name? ')

with open(filename, "r") as file:
    image_text = file.read()

# Convert text into usable object and pull data.
image_json = json.loads(image_text)

image_data = image_json['data']
num_rows = image_json['num_rows']
num_columns = image_json['num_columns']

# Create blank base image.
image = [[False for _ in range(num_rows)] for _ in range(num_columns)]

# Go through each column and determine whether spot is filled or blank.
for column in range(num_columns):
    filled = True
    row = 0
    for i_run in range(len(image_data[column])):
        for value in range(image_data[column][i_run]):
            if row < num_rows:
                image[column][row] = filled
                row += 1
        filled = not filled

# Print statement to display to user.
print('\nHere is your uncompressed image!\n')

# Print the image, don't start a new line when characters are in the same row.
for row in range(num_rows):
    for column in range(num_columns):
        if image[column][row]:
            print('#', end='')
        else:
            print(' ', end='')
    print() 