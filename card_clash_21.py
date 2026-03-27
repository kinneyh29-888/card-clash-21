print("Game Start.")
import random 

# Global Configurations
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
}
# Function creates deck and return value
def create_deck():
    deck = [(rank, suit) for rank in ranks for suit in suits]
    return deck

# Function shuffles deck and deals player and dealer card 
def shuffle_deck(deck):
    random.shuffle(deck)
    player_card = [deck.pop(), deck.pop()]
    dealer_card = [deck.pop(), deck.pop()]
    return player_card, dealer_card

# Loops for rounds
while True:
    deck = create_deck()
    player_card, dealer_card = shuffle_deck(deck)

    while True:
        
        #Total score of the player cards
        player_score = sum(card_values[card[0]] for card in player_card)
        
        #Prints when hit
        print("\nPlayer has cards: ", player_card)
        print("Player score: ", player_score)
        
        #Game ends when score over 21
        if player_score > 21:
            print("Player busts! Dealer wins.")
            break

        choice = input('Hit (add card) or bust (turn over): ').lower()
        
        #New card, add to score, and print card
        if choice == "hit":
            new_card = deck.pop()
            player_card.append(new_card)
            print("Player pulled a: ", new_card)
        
        # End player turn if player bust
        elif choice == "bust":
            break
        
        
        # Invalid inputs
        else:
            print("Invalid choice. Please try again.")
            continue
    
    # Add up score after either hit or bust 
    player_score = sum(card_values[card[0]] for card in player_card)
    
    
    
    if player_score > 21:
        print("\nDealer has cards: ", dealer_card)
        dealer_score = sum(card_values[card[0]] for card in dealer_card)
        print("Dealer score: ", dealer_score)
        
        #
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != "yes":
            break
        else:
            continue

    print("\nDealer's turn...")
    dealer_score = sum(card_values[card[0]] for card in dealer_card)

    print("Dealer has cards: ", dealer_card)
    print("Dealer score: ", dealer_score)

    while dealer_score < 18:
        new_card = deck.pop()
        dealer_card.append(new_card)
        dealer_score = sum(card_values[card[0]] for card in dealer_card)

        print("\nDealer pulled: ", new_card)
        print("Dealer has cards: ", dealer_card)
        print("Dealer score: ", dealer_score)

        if dealer_score > 21:
            print("\nDealer busts! Player wins.")
            break

    if dealer_score <= 21:
        if player_score > dealer_score:
            print("\nPlayer wins.")
        elif dealer_score > player_score:
            print("\nDealer wins.")
        else:
            print("\nIts a tie.")

    print("\nFinal Scores:")
    print("Player:", player_card, "Score:", player_score)
    print("Dealer:", dealer_card, "Score:", dealer_score)

    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        print("End Game.")
        break







    