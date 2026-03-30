Card Clash 21!

How to play:
Player and dealer (computer) start with two cards
Your goal is to get as close to 21 as possible without going over

Once seeing your two cards you can 'hit' which means drawing a new card
Or 'stand' to end your turn

Special rule:
If you draw an Ace you can choose the value as a 1 or 11

Dealer (computer) rules:
  The dealer must hit untiol score is at least 16
  Dealers aces automatically adjust from 11 - 1 if needed

Game logic:
  Combines suits and ranks into a full deck of 52 cards
  Number cards = face value
  Face cards (Jack, Queen, King) = 10
  Ace:
    Player decides value
    Dealer adjusts to avoid bust

Conditions:
  Player wins if:
    Dealer busts
    Player score > dealer score
  Dealer wins if:
    Player busts
    Dealer > player score
  Tie if equal scores

EXAMPLE GAMEPLAY:
Player has cards:  [('Ace', 'Spades'), ('7', 'Hearts')]
You got an Ace! Count it as 1 or 11? 11
Player score: 18

Hit or stand: hit
Player pulled a: ('5', 'Clubs')
Player score: 23

Player busts! Dealer wins.



