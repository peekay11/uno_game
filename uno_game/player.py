from cards import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.cards_in_hand = []

    def draw_hand(self, deck):
        self.cards_in_hand = [deck.pop() for _ in range(7)]

    def draw_card(self, deck):
        if deck:
            drawn_card = deck.pop()
            self.cards_in_hand.append(drawn_card)
            print(f"{self.name} drew: {drawn_card}")
        else:
            print(" The Deck is empty..")

    def play_card(self, discard_pile):
       
        top_card = discard_pile[-1]
        playable = [card for card in self.cards_in_hand if card.matches(top_card)]


        if not playable:
            print(f"{self.name} has no playable cards.")
            return False

        #  ask which card to play
        print(f"Top card: {top_card}")
        for i, card in enumerate(playable):
            print(f"{i+1}. {card}")

        try:
            choice = int(input(f"{self.name}, choose a card number to play: ")) - 1
            chosen_card = playable[choice]
        except (ValueError, IndexError):
            print("Invalid choice.")
            return False

        self.cards_in_hand.remove(chosen_card)
        discard_pile.append(chosen_card)
        print(f"{self.name} played: {chosen_card}")
        return True



# cpu logic 
    def cpu_play(self, discard_pile, deck):

        top_card = discard_pile[-1]
        playable = [card for card in self.cards_in_hand if card.matches(top_card)]

        if playable:
            chosen_card = playable[0]
            self.cards_in_hand.remove(chosen_card)
            discard_pile.append(chosen_card)
            print(f"{self.name} played: {chosen_card}")
        else:
            print(f"{self.name} cannot play — drawing a card.")
            self.draw_card(deck)

    def declare_uno(self):
        if len(self.cards_in_hand) == 1:
            print(f"{self.name} declares UNO!")
        elif len(self.cards_in_hand) == 0:
            print(f"{self.name} has no cards  already won!")

    def check_winner(self):
        if len(self.cards_in_hand) == 0:
            print(f"{self.name} won the game!")
            return True
        return False







