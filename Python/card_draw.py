from random import randint as rand
from random import shuffle

suits = ("Spades","Hearts","Clubs","Diamonds")

class Card:
    def __init__(self, rank, suit):
        if rank not in range(1, 14):
            raise TypeError('Rank must be an integer between 1 and 13.')
        if suit not in suits:
            raise TypeError('Suit must be a string: "Spades", "Hearts", "Clubs", or "Diamonds".')
        # The quick check above makes sure the card being made actually exists in a standard deck of 52.
        # If so, the card is created succesfully.
        self.rank = rank
        self.suit = suit


    def cardName(self):
        """
        Returns a string containing the card's name in common terms.
        """
        if self.rank == 1:
            trueRank = "Ace"
        elif self.rank == 11:
            trueRank = "Jack"
        elif self.rank == 12:
            trueRank = "Queen"
        elif self.rank == 13:
            trueRank = "King"
        else:
            trueRank = str(self.rank)
        return "{rank} of {suit}".format(rank = trueRank, suit = self.suit)

    def flip(self):
        """
        Reveals the requested card.
        """
        print(self.cardName())

def newDeck():
    """
    Resets the deck to ascending order, containing all 52 cards.
    """
    global cardDeck
    cardDeck = [Card(rank, suit) for suit in suits for rank in range(1, 14)]
    cardDeck.reverse() # So that the bottom of the list is the top of the deck, i.e. the Ace of Spades is drawn first by 'cardDeck.pop()'.

newDeck()   # To generate the deck at the start. Note that it is not shuffled at first.

def shuffleDeck():
    """
    Self-explanatory. Shuffles the deck.
    """
    global cardDeck
    for i in range(0, 3):
        shuffle(cardDeck)   # Python's pseudorandom generator is slightly patterned unless shuffled multiple times.

def draw():
    """
    Draws a single card to a variable.
    Useful for replacing and discarding individual cards in a hand, such as replacing cards in poker.
    To do so: <hand>[<card to replace>] = cards.draw()
    Remember that the list for a hand starts from 0, not 1.
    """
    randCard = cardDeck.pop()
    return randCard

def drawFaceUp():
    randCard = cardDeck.pop()
    randCard.flip()
    return randCard

def drawHand(size):
    """
    Draws a <size>-card hand from the deck.
    """
    return [draw() for i in range(0, size)]

def showHand(hand):
    size = len(hand)
    for i in range(0, size):
        hand[i].flip()

def newCard():
    """
    Generates a random card outside of the established deck, and prints its value.
    While occasionally useful, using newCard() for hands is discouraged. Duplicates of preexisting cards will result.
    """
    suit = suits[rand(0, 3)]
    rank = rand(1,13)
    randCard = Card(rank,suit)
    print("The {card} has been generated.".format(card = str(randCard.cardName())))
    return randCard

def cardHelp():
    """
    Gives a set of instructions explaining the use of the 'cards.py' module.
    """
    print('\n' + '=' * 72)
    print('=' * 13 + " [brilliantlyInsane]'s Python Cards: Instructions " + '=' * 14)
    print('=' * 72 + '\n')

    print('—' * 16 + " The Cards " + '—' * 45)
    print('—' * 72)
    print('The "Card" object has two attributes:')
    print('rank - An integer between 1 and 13. (Ace = 1, Jack = 11, Queen = 12, King = 13.)')
    print('suit - A string value of either "Spades", "Hearts", "Clubs", or "Diamonds".')
    print('A specific card object can be made: "Card(<rank>,<suit>)".\n')

    print('—' * 16 + " Drawing Cards " + '—' * 41)
    print('—' * 72)
    print('"Draw" cards to a variable with "<var> = cards.draw()".')
    print('Use "cards.drawFaceUp() to draw a card and print its value.')
    print('"Flip" a card (print its value) with "<var>.flip()".')
    print('Generate an entirely new random card using "cards.newCard()".')
    print('(Note that "newCard()" duplicates a card in the deck.)\n')

    print('—' * 16 + " Hands " + '—' * 49)
    print('—' * 72)
    print('To draw an entire hand with <size> many cards, use "cards.drawHand(<size>)".')
    print('To show a hand, use "cards.showHand(<hand>)."\n')

    print('—' * 16 + " Replacing Cards " + '—' * 39)
    print('—' * 72)
    print('You can replace individual cards in a hand using <hand>[card #] = cards.draw().')
    print('However, lists in Python start FROM 0, not 1!')
    print('"hand[1] = cards.draw()" will replace the SECOND card in your hand, not the first!\n')

    print('—' * 16 + " The Deck " + '—' * 46)
    print('—' * 72)
    print('The deck is stored to a list under the variable "cards.cardDeck".')
    print('Shuffle using "shuffleDeck()". The deck is unshuffled by default.')
    print('Reset the deck completely using cards.newDeck().')
    print('\n' + '=' * 72 + '\n')

print('Type "cards.cardHelp()" to learn how to use this module.')
