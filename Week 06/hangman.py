import urllib.request
import random
import time

# Make a big list of words.
# Parameters:
#   minimum_length (integer): only include words that are at least this long.
def get_words(minimum_length):
    result = []
    url = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-no-swears.txt"
    for line in urllib.request.urlopen(url):
        word = line.decode("utf-8")[:-1]
        if len(word) >= minimum_length:
            result.append(word)

    return result

# Make a secret word for playing hangman.
# Parameters:
#   minimum_length (integer): only include words that are at least this long.
def get_secret_word(minimum_length):
    words = get_words(minimum_length)
    return random.choice(words)

# Take a guess.
# Parameters:
#   guessed (list): a list of the letters already guessed.
def guess_letter(guessed):
    print("What's your guess?")
    letter = input()
    if letter in guessed:
        print('You already guessed that letter.')
        return

    print('Give me a ' + letter + '!')
    guessed.append(letter)

# Check if the game has been won.
# Paramters:
#   secret_word (string): the word the player is trying to guess.
#   guessed (list): a list with all the guesses so far.
def word_guessed(secret_word, guessed):
    for letter in secret_word:
        if letter not in guessed:
            return False

    return True

# Check if the game has been lost.
# Parameters:
#   secret_word (string): the word the player is trying to guess.
#   guessed (list): a list with all the guesses so far.
#   maximum_wrong_guesses (integer): the most incorrect guesses allowed.
def out_of_guesses(secret_word, guessed, maximum_wrong_guesses):
    return wrong_guesses(secret_word, guessed) >= maximum_wrong_guesses

# Count the number of wrong guesses.
# Parameters:
#   secret_word (string): the word the player is trying to guess.
#   guessed (list): a list with all the guesses so far.
def wrong_guesses(secret_word, guessed):
    result = 0
    for letter in guessed:
        if letter not in secret_word:
            result = result + 1

    return result

# Print out the word, with the correctly guessed letters revealed,
# and the rest as a dash. Also print how many guesses are left.
# Parameters
#   secret_word (string): the word the player is trying to guess.
#   guessed (list): a list with all the guesses so far.
#   maximum_wrong_guesses (integer): the most incorrect guesses allowed.
def show_status(secret_word, guessed, maximum_wrong_guesses):
    for letter in secret_word:
        if letter in guessed:
            print(letter, end='')
        else:
            print('-', end='')

        time.sleep(0.4)

    print()
    print('Wrong guesses remaining: ' + str(maximum_wrong_guesses - wrong_guesses(secret_word, guessed)))
    print()


maximum_wrong_guesses = 7
guessed = []
number_of_guesses = 0
secret_word = get_secret_word(6)

while not word_guessed(secret_word, guessed) and not out_of_guesses(secret_word, guessed, maximum_wrong_guesses):
    show_status(secret_word, guessed, maximum_wrong_guesses)
    guess_letter(guessed)

show_status(secret_word, guessed, maximum_wrong_guesses)

if word_guessed(secret_word, guessed):    
    print('YOU DID IT!!!')
else:
    print('you dead')
    print('btw the word was ' + secret_word)
