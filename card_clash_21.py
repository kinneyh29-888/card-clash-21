print("Game Start.")
import random 
# Global Configurations
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,

    "Jack": 10, "Queen": 10, "King": 10, "Ace" : 11
}


def create_deck():
    deck = [(rank, suit) for rank in ranks for suit in suits]
    return deck
def shuffle_deck(deck):
    random.shuffle(deck)
    player_card = [deck.pop(), deck.pop()]
    dealer_card = [deck.pop(), deck.pop()]
    return player_card, dealer_card
deck = create_deck()
player_card, dealer_card = shuffle_deck(deck)
while True:
    player_score = sum(card_values[card[0]] for card in player_card)
    dealer_score = sum(card_values[card[0]] for card in dealer_card)
    print("Player has cards: ", player_card)
    print("Player score: ", player_score)
    print("\n")
    choice = input('Hit (add card) or bust (turn over):').lower()
    if choice == "hit":
        new_card = deck.pop()
        player_card.append(new_card)
        print("Player pulled a: ", new_card)
        print("Player has cards: ", player_card)
        print("Player score: ", player_score)
    elif choice == "bust":
        break 
    else: 
        print("Invalid choice. Please try again.")
        continue
    if player_score > 21:
        print("Player has cards: ", player_card)
        print("Player score: ", player_score)
        print("Dealer has cards: ", dealer_card)
        print("Dealer score: ", dealer_score)
        print("Dealer wins.")
    elif player_score == 21:
        print("Player wins.")
while dealer_score < 18:
    new_card = deck.pop()
    
    dealer_card.append(new_card)
    dealer_score += card_values[new_card[0]]

    print("Dealer has cards: ", dealer_card)
    print("Dealers score: ", dealer_score)
    print("\n")

if dealer_score > 21:
    print("Dealer has cards: ", dealer_card)
    print("Dealer score: ", dealer_score)
    print("Player has cards: ", player_score)
    print("Player wins.")
if player_score > 21:
    print("Player has cards: ", player_card)
    print("Score of Player: ", player_score)
    print("Dealer has cards: ", dealer_card)
    print("Dealer wins.")
if player_score > dealer_score:
    print("Dealer has cards: ", dealer_card)
    print("Dealer score: ", dealer_score)
    print("Player has cards: ", player_card)
    print("PLayer score: ", player_score)
    print("Player wins.")
if dealer_score > player_score:
    print("Dealer has cards: ", dealer_card)
    print("Dealer score: ", dealer_score)
    print("Dealer wins.")
else:
    print("Dealer has cards: ", dealer_card)
    print("Dealer score: ", dealer_score)
    print("Player has cards: ", player_card)
    print("Player score: ", player_score)
    print("Its a tie.")







    