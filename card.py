import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.notFlip = True

    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

    def isHidden(self):
        return self.notFlip

class Deck:
    SUITS = ['CLUB', 'SPADE', 'HEART', 'DIAMOND']
    VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.deck = []
        for i in Deck.SUITS:
            for j in Deck.VALUES:
                self.deck.append(Card(i, j))

        self.position = 0

    def getSize(self):
        return len(self.deck)-self.position

    def pickCard(self, count):
        for i in range(count):
            if self.position < 52:
                suit = self.deck[self.position].getSuit()
                value = self.deck[self.position].getValue()
                print(value, "of", suit + 's')
                self.deck[self.position].notFlip = False
                self.position += 1

            else:
                self.shuffle()
                suit = self.deck[self.position].getSuit()
                value = self.deck[self.position].getValue()
                print(value, "of", suit + 's')
                self.deck[self.position].notFlip = False
                self.position += 1

    def shuffle(self):
        random.shuffle(self.deck)

        for i in self.deck:
            i.notFlip = True

        self.position = 0
