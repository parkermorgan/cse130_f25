# 1. Name: 
#    Parker Morgan
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#   This program is a guessing game where the user guesses a random number between 1 and a positive integer of the user's choice. The numbers they have guessed are stored within an list and are displayed to the user, along with the total number of guesses they did once they guess the correct number.
# 4. What was the hardest part? Be as specific as possible.
#    Because I am taking this class late into my schooling, it came to me pretty easily. However, I had made the mistake of using the max_value variable in my loop when the user was guessing instead of the value_random variable. Because of this the correct answer was always the max value the user input, and it took me a few minutes to realize my mistake. I also had to review the formatting for if statements and while loops since I have been working with other programming languages.
# 5. How long did it take for you to complete the assignment?
#    Including reading the instructions and reviewing python, the assignment took just under an hour.
import random

# Game introduction.
print('This is the "guess a number" game. \nYou try to guess a random number in the smallest number of attempts.')
# Prompt the user for how difficult the game will be. Ask for an integer.
max_value = int(input('Pick a positive integer: '))
if max_value <0:
    print('Invalid number. Please try again')
# Generate a random number between 1 and the chosen value.
attempts = 0
value_random = random.randint(1, max_value)

# Give the user instructions as to what he or she will be doing.

print(f'Guess a number between 1 and {max_value}.')

# Initialize the sentinal and the array of guesses.

guesses = []

looping = True

# Play the guessing game.

while looping:

# Prompt the user for a number.
    guess = int(input('> '))
    # Store the number in an array so it can be displayed later.
    guesses.append(guess)
    attempts += 1
    # Make a decision: was the guess too high, too low, or just right.
    if guess < value_random:
        print('     Too low!')
        
    elif guess > value_random:
        print('     Too high!')
        
    elif guess == value_random:
       
        # Give the user a report: How many guesses and what the guesses where.
        print(f'You were able to find the number in {attempts} guesses.')
        print(f'The numbers you guessed were: {guesses}')
        looping = False
    




