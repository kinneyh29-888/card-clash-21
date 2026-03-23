import random 
# Global Configurations
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,

    "Jack": 10, "Queen": 10, "King": 10, "Ace" : 11
}

Print("Game Start.")

"""Returns a list of 52 tuples representing a standard deck:
(rank, suit)"""
def create_deck():
    ranks for suits in range(52):

print(create_deck)

"""Shuffles the deck list in-place."""
def shuffle_deck(deck):
    deck.random()
    
"""Calculates the total value of cards in a hand.
Requirement: If the score is over 21 and the hand comntains an Ace,
reduce the score by 10 until the score is <=21 or no Aces remain."""
def calculate_score(hand):
    if 
    







    