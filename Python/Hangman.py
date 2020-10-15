"""
Hangman, by lol 

"""
import random
import sys

# Set up the constants:
# (!) Try adding or changing the strings in HANGMAN_PICS to make a
# guillotine instead of a gallows.
HANGMAN_PICS = [r"""
 +--+
 |  |
    |
    |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
    |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====""",
                r"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
====="""]

# (!) Try replacing CATEGORY and WORDS with new strings.
CATEGORY = 'AVENGERS SUPER HEROES'
WORDS = 'IRONMAN THOR CAPTAINAMERICA BLACKWIDOW WASP ANTMAN HULK HAWKEYE QUICKSILVER VISION FALCON SPIDERMAN WARMACHINE DOCTORSTRANGE '.split()


def main():
    print('====< Hangman <==== __lol__')

    # Setup variables for a new game:
    missedLetters = []  # List of incorrect letter guesses.
    correctLetters = []  # List of correct letter guesses.
    secretWord = random.choice(WORDS)  # The word the player must guess.

    while True:  # Main game loop.
        drawHangman(missedLetters, correctLetters, secretWord)

        # Let the player enter their letter guess:
        guess = getPlayerGuess(missedLetters + correctLetters)

        if guess in secretWord:
            # Add the correct guess to correctLetters:
            correctLetters.append(guess)

            # Check if the player has won:
            foundAllLetters = True  # Start off assuming they've won.
            for secretWordLetter in secretWord:
                if secretWordLetter not in correctLetters:
                    # There's a letter in the secret word that isn't
                    # yet in correctLetters, so the player hasn't won:
                    foundAllLetters = False
                    break
            if foundAllLetters:
                print('Yes! The secret word is:', secretWord)
                print('You have won!')
                break  # Break out of the main game loop.
        else:
            # The player has guessed incorrectly:
            missedLetters.append(guess)

            # Check if player has guessed too many times and lost. (The
            # "- 1" is because we don't count the empty gallows in
            # HANGMAN_PICS.)
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                drawHangman(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!')
                print('The word was "{}"'.format(secretWord))
                break


def drawHangman(missedLetters, correctLetters, secretWord):
    """Draw the current state of the hangman, along with the missed and
    correctly-guessed letters of the secret word."""
    print(HANGMAN_PICS[len(missedLetters)])
    print('The category is:', CATEGORY)
    print()

    # Show the incorrectly guessed letters:
    print('Missed letters: ', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    if len(missedLetters) == 0:
        print('No missed letters yet.')
    print()

    # Display the blanks for the secret word (one blank per letter):
    blanks = ['_'] * len(secretWord)

    # Replace blanks with correctly guessed letters:
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks[i] = secretWord[i]

    # Show the secret word with spaces in between each letter:
    print(' '.join(blanks))


def getPlayerGuess(alreadyGuessed):
    """Returns the letter the player entered. This function makes sure
    the player entered a single letter they haven't guessed before."""
    while True:  # Keep asking until the player enters a valid letter.
        print('Guess a letter.')
        guess = input('> ').upper()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif not guess.isalpha():
            print('Please enter a LETTER.')
        else:
            return guess


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
