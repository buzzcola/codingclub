# our first program where we write our own functions!

import random
import time

# function to print the introduction.
def displayIntro():

    # Here's a new way to make strings: multi-line strings!
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')

    print()

# this function makes the user choose a cave.
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()

    return cave

# Send the user into the chosen cave... and see if they get eaten!
def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')


# everything has been functions so far. Now let's actually do something!
# make a "while" loop where the user can play until they're done.

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    # here's where we actually call our functions.
    
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()