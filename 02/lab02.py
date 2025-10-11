# 1. Name:
#      Parker Morgan
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      This is a simple authentication program. The program reads data from a
#      JSON file containing two constructs: usernames and passwords.
#      The program converts these constructs into two lists, then combines the
#      lists into a dictionary. The user enters a username and password.
#      If the username and password match, a message is displayed approving
#      the user's authentication. If not, a message is displayed 
#      stating that the user is not authorized. 
# 4. What was the hardest part? Be as specific as possible.
#      I would say the hardest part of the assignemnt was figuring out how
#      to relate the two constructs by index and match them up. It took me
#      multiple tries with different ideas, but ultimately settled on
#      zipping the lists together and turning them into a dictionary. 
#       
#      I also had a difficult time making my comments concise yet clear.
#      I've always struggled with having clear documentation in my code, but I
#      believe that I was able to accomplish that with this assignment.
# 5. How long did it take for you to complete the assignment?
#      This assignment took me approximately 90 minutes.

import json

# Load the JSON file and parse its contents.
with open('Lab02.json', 'r') as file:
    json_text = file.read()
    data = json.loads(json_text)

# Extract usernames and passwords from the data.
usernames = data['username']
passwords = data['password']

# Link usernames to their corresponding passwords.
credentials = dict(zip(usernames, passwords))

# Prompt the user for login credentials.
username = input('Username: ')
password = input('Password: ')

# Check if the entered credentials match.
if credentials.get(username) == password:
    print('You are authenticated!')
else:
    print('You are not authorized to use this system.')

    