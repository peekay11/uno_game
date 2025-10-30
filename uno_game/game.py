from cards import Deck
from player import Player


deck = Deck()
shuffled_cards = deck.shuffle_cards()
player = Player("Player 1")
cpu = Player("CPU")

# Deal hands
player.draw_hand(shuffled_cards)
cpu.draw_hand(shuffled_cards)


discard_pile = [shuffled_cards.pop()]
print(f"Starting card: {discard_pile[-1]}")

def play_button():
    answer = input("Are you ready to play? (y/n): ").lower()
    if answer == "y":
        print("Starting game...\n")
    else:
        print("Exiting.")
        exit()

play_button()


game_over = False
while not game_over:
    print("\nYour hand:")
    for i, card_value in enumerate(player.cards_in_hand, start=1):
        print(f"{i}. {card_value}")
    print(f"Top card: {discard_pile[-1]}")

    command = input(f"\nChoose action (D=Draw / T=Throw / U=UNO / Q=Quit): ").upper()

    if command == "D":
        player.draw_card(shuffled_cards)
    elif command == "T":
        player.play_card(discard_pile)
    elif command == "U":
        player.declare_uno()
    elif command == "Q":
        print("Game ended.")
        break
    else:
        print("Invalid command.")

    if player.check_winner():
        game_over = True
        break

    # Computer Turn

    print("\nCPU Turn:")
    cpu.cpu_play(discard_pile, shuffled_cards)
    if cpu.check_winner():
        game_over = True
        break
