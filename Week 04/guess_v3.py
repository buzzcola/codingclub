# import the "random" module, which has functions for making random numbers.
import random

# make a random number that the user can guess.
maximum = 20
number = random.randint(1, maximum)

# set up the guess variable here. The user hasn't guessed anything yet, so set it to "None".
guess = None

# Tell the user the range of numbers. Use the "str" function to convert the number to a string.
print("I'm thinking of a number between 1 and " + str(maximum) + ". Maybe you can guess it!")

# keep looping as long as the guess is wrong.
while guess != number:

    # get the guess and convert it from a string to a number using the int() function.
    guess = int(input('What is your guess?'))

    # if the guess is wrong, print a message about that.
    if guess != number:
        print('Nope. Try again!')

# if we made it to this line, they must have guessed correctly.
print('Congratulations! You win.')