# DegeneracyLite

## Description

Hey everybody, I went ahead and made this program so that anyone playing online BlackJack can get their edge over the house and win a little something (hopefully). This program relies on users input to accurately count cards thus it is imperative that you feed it the correct information (to the best of your abilities). The program will also feed the player statisically proven basic strategy based on the dealers upcard and the players hand. Feel free to use and manipulate this code in anyway that you see fit. Happy gambling!

This project is ongoing and ultimately ends with it being fully automated using computer vision and selenium modules but I am always open to new ideas from those that are more skilled at python than myself, so please reach out to me if you have ideas.


## Arguments for the program 

1. The number of decks being used for the shoe (usually 6 or 8) or number of decks left in play 

2. The number of players at the table besides yourself

3. Position you have taken at the table (based on normal indexing and not zero based)

***Example of use:***

    python counting.py 8 3 1

## Operation

This program follows the logical progression of the game BlackJack thus inputs for cards start with the first and second round of cards dealt to the players followed by the dealers up card. Every player will either hit, stay, or split (followed by some combination of the previous actions). When a player hits on their turn simply input the corresponding card into the given players prompt. They will either bust or stay in which case the program will either transition to the next players turn or accept an 's' from the input to indicate the player is stay. In the case of the split, a pair will be recognized and the player will be asked if they decided to split (input y for yes or anything else for no). That's pretty much it!
