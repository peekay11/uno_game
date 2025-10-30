import random

class Card:
    def __init__(self, value, color):
        self.value = value  # number or action
        self.color = color  # red, green, blue, yellow

    def __str__(self):
        return f"{self.value} {self.color}"

    def matches(self, other_card):
        if self.color == other_card.color:
            return True
        if self.value == other_card.value:
            return True
        if self.value == "draw 4":  # Wild card can always be played
            return True
        return False


class Deck:
    def __init__(self):
        self.values = [0,1,2,3,4,5,6,7,8,9,"skip","reverse","draw 2","draw 4"]
        self.colors = ["red", "green", "blue", "yellow"]

    def shuffle_cards(self):
        deck = [Card(value, color) for value in self.values for color in self.colors]
        random.shuffle(deck)
        return deck
