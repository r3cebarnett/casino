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

    def getSize(self):
        return len(self.deck)
