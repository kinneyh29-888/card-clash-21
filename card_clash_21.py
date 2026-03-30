print("Game Start.")
import random 

# Global Configurations
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
}

#Creating deck and returning
def create_deck():
    deck = [(rank, suit) for rank in ranks for suit in suits]
    return deck

#Shuffling deck
def shuffle_deck(deck):
    random.shuffle(deck)

#Pops off cards for dealer and player, stores in variables
def deal_cards(deck):
    player_card = [deck.pop(), deck.pop()]
    dealer_card = [deck.pop(), deck.pop()]
    return player_card, dealer_card

# Player score when recieving ace
# Player chooses if 1 or 11
def calculate_player_score(cards):
    score = 0

    for i in range(len(cards)):
        card = cards[i]

        rank = card[0]
        suit = card[1]

        if rank != "Ace":
            score += card_values[rank]
        else:
            
            if len(card) == 3:
                score += card[2]
            else:
                #Choosing 11 or 1
                while True:
                    choice = input("You got an Ace! Count it as 1 or 11? ")
                    if choice == "1":
                        value = 1
                        break
                    elif choice == "11":
                        value = 11
                        break
                    #Invalid Option
                    else:
                        print("Invalid choice. Please enter 1 or 11.")

                # Store value in card
                cards[i] = (rank, suit, value)
                score += value

    return score

# Dealer score, ace will auto adust
def calculate_dealer_score(cards):
    score = sum(card_values[card[0]] for card in cards)
    ace_count = sum(1 for card in cards if card[0] == "Ace")

    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1

    return score


while True:
    deck = create_deck()
    shuffle_deck(deck)
    player_card, dealer_card = deal_cards(deck)

    while True:
        # Prints cards before score
        print("\nPlayer has cards: ", player_card)

        # Calculates score (Player will see cards before choosing ace 1 or 11)
        player_score = calculate_player_score(player_card)
        print("Player score: ", player_score)

        # Automatic win if player hits 21
        if player_score == 21:
            print("Player hits 21!")
            break
        
        # Automatic loss if player is over 21
        if player_score > 21:
            print("Player busts! Dealer wins.")
            break

        choice = input('Hit or stand: ').lower()
        
        # Player chooses hit and gains a new card
        # New card is printed
        if choice == "hit":
            new_card = deck.pop()
            player_card.append(new_card)
            print("Player pulled a: ", new_card)
        
        # Ends player turn if chooses stand
        elif choice == "stand":
            break
        
        #Invalid Choice
        else:
            print("Invalid choice. Please try again.")
            continue

    player_score = calculate_player_score(player_card)

    # Final print (all scores) when player busts
    if player_score > 21:
        print("\nDealer has cards: ", dealer_card)
        dealer_score = calculate_dealer_score(dealer_card)
        print("Dealer score: ", dealer_score)
        
        #Option to play again
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != "yes":
            break
        else:
            continue

    # When player breaks or turn is over
    # Calculating deal score 
    print("\nDealer's turn...")
    dealer_score = calculate_dealer_score(dealer_card)
    
    # Shows dealer cards and score
    print("Dealer has cards: ", dealer_card)
    print("Dealer score: ", dealer_score)

    # Dealer pulls new card when scores under 17, new card is added to score
    while dealer_score < 17:
        new_card = deck.pop()
        dealer_card.append(new_card)
        dealer_score = calculate_dealer_score(dealer_card)
        
        # Showing new card, new hand, and score
        print("\nDealer pulled: ", new_card)
        print("Dealer has cards: ", dealer_card)
        print("Dealer score: ", dealer_score)

        # Player wins when dealer busts
        if dealer_score > 21:
            print("\nDealer busts! Player wins.")
            break

    # Calculating who wins and printing
    if dealer_score <= 21:
        if player_score > dealer_score:
            print("\nPlayer wins.")
        elif dealer_score > player_score:
            print("\nDealer wins.")
        else:
            print("\nIts a tie.")
    
    #Final hands, final scores
    print("\nFinal Hands:")
    print("Player:", player_card, "Score:", player_score)
    print("Dealer:", dealer_card, "Score:", dealer_score)
    
    # Playing again
    # If yes, repeats
    # if no, prints goodbye
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
