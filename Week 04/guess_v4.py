# import the "random" module, which has functions for making random numbers.
import random

# make a random number that the user can guess.
maximum = 10
number = random.randint(1, maximum)

# Tell the user the range of numbers. Use the "str" function to convert the number to a string (text).
print("I'm thinking of a number between 1 and " + str(maximum) + ". Maybe you can guess it!")

win = False
guesses = 0

while not win:

    # get the guess and convert it from a string to an integer (whole number) using the int() function.
    guess = int(input('What is your guess?'))
    guesses = guesses + 1

    # let the user know if they won or not.
    if guess == number:
        win = True
    else:
        print("Nope. Try again.")


print("You win! It only took you " + str(guesses) + " guesses.")
