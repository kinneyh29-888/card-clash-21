print("Game Start.")
import random 
# Global Configurations
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,

    "Jack": 10, "Queen": 10, "King": 10, "Ace" : 11
}

def create_deck():
    deck = [(rank, suit) for rank in ranks for suit in suits]
    
def shuffle_deck(deck):
    random.shuffle(deck)
    player_card = [deck.pop(), deck.pop()]
    dealer_card = [deck.pop(), deck.pop()]
def deal_card(deck):
    print(player_card)
    
create_deck()
shuffle_deck(deck)
deal_card(deck)







    