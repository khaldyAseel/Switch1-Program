# Acoording to the design principles Separation of Concerns
# we will devide the code 

import random
from card import Card

class Board:
    def __init__(self, size):
        self.size = size
        self.cards = self.init_cards()
        random.shuffle(self.cards)

    def init_cards(self):
        return [Card(i) for i in range(self.size//2) for _ in range(2)]
      

    def display_board(self):
        for i, card in enumerate(self.cards):
            if card.face_up:
                print(f"{card.value:2}", end=" ")
            else:
                print(" *", end=" ")
            if (i + 1) % (self.size // 2) == 0:
                print()
        print()

    def is_match(self, index1, index2):
        return self.cards[index1].value == self.cards[index2].value

    def all_cards_matched(self):
        return all(card.face_up for card in self.cards)