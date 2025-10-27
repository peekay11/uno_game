
import random
class Card:
    def __init__(self):
        self.cards = [0,1,2,3,4,5,6,7,8,9,"skip","reverse","draw 2","draw 4"]
        self.colors = ["red", "green", "blue", "black"]

    def check_cards(self):
        all_cards = []
        for card in self.cards:
            for color in self.colors:
                mixed = "{} {}".format(card, color)
                all_cards.append(mixed)
        return all_cards
    

    def shuffle_cards(self):
        shuffled_cards = []
        for card in self.cards:
           for color in self.colors:
                mixed = "{} {}".format(card, color)
                shuffled_cards.append(mixed)
                random.shuffle(shuffled_cards)
        return shuffled_cards


    #   🔀 This shuffles the list in place


deck = Card()
print(deck.check_cards())
space = " "
print(space *100)
print(deck.shuffle_cards())

