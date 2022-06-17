import random
# Game Title
print("*******      *         *         *****     *     *           *       *          *****      *      *  ")
print("*      *     *       *    *     *          *   *             *     *    *      *           *     *   ")
print("*      *     *       *    *     *          *  *              *     *    *      *           *    *    ")
print("*******      *       *    *     *          * *               *     *    *      *           *  *      ")
print("*      *     *       ******     *          *   *             *     ******      *           *    *    ")
print("*      *     *       *    *     *          *     *           *     *    *      *           *      *  ")
print("*******      ******  *    *      *****     *       *     *         *    *       *****      *        *")

# Coming Soon
# add money
# add additional players 
#num_players = input("1 player or 2 players? \n Type 1 or 2: ")
name1 = input("\nEnter your name: ")
# if num_players == 2:
    # name2 = input("Enter name for player 2: ")
deck = deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
play = True

class Dealer:
    def __init__(self):
        self.hand = []

    def clear_hand(self):
        self.hand = []
        total = sum(self.hand)
        return total
    
    def deal_hand(self):
        while len(self.hand) <= 1:
            cards = random.choice(deck)
            self.hand.append(cards)
        total = sum(self.hand)
        print(f"Dealer Hand: {self.hand[0]}")
        return total
    def draw_card(self):
        total = sum(self.hand)
        if sum(self.hand) < 17:
            cards = random.choice(deck)
            self.hand.append(cards)
            total = sum(self.hand)
            print(f"Dealer Hand: {total}")
            return total
            
        else:
            print(f"Dealer Hand: {total}")
            return total

class Player:
    def __init__(self):
        self.hand = []

    def clear_hand(self):
        self.hand = []
        total = sum(self.hand)
        return total
    
    def deal_hand(self):
        while len(self.hand) <= 1:
            cards = random.choice(deck)
            self.hand.append(cards)
        total = sum(self.hand)
        print(f"{name1}'s Hand: {total}")

    def draw_card(self):
        cards = random.choice(deck)
        self.hand.append(cards)
        total = sum(self.hand)
        print(f"{name1}: {total}")
        return total

    def stand(self):
        total = sum(self.hand)
        print(f"{name1}: {total}")
        return total
# Objects
dealer = Dealer()
player1 = Player()
player2 = Player()

# Dealing initial hand
dealer.deal_hand()
player1.deal_hand()

# Main Game
def blackjack():
    play = True
    while play == True:
        
        player_choice = input("\nChoose Hit or Stand: ")
        player_choice = player_choice.casefold()
        if player_choice == "hit":
            plyr_hand = player1.draw_card()
            dealer_hand = dealer.draw_card() 
            if plyr_hand > 21:
                print("Bust! Dealer wins!")
                play = False
            elif dealer_hand > 21:
                print(f"Bust! {name1} wins!")
                play = False 
            elif dealer_hand == plyr_hand:
                print("Draw")
                play = False
        elif player_choice == "stand":
            plyr_hand = player1.stand()
            dealer_hand = dealer.draw_card()
            
            if dealer_hand > 21:
                print(f"Bust! {name1} wins!")
                break
            # If neither the dealer nor the player has over 21 this part of the code determines which hand is closer to 21   
            plyr_hand_dis_21 = 21 - plyr_hand
            dealer_hand_dis_21 = 21 - dealer_hand
            if plyr_hand_dis_21 < dealer_hand_dis_21:
                print(f"\nYour current hand is: {plyr_hand}")
                print(f"Dealer hand is {dealer_hand}")
                print(f"{name1} wins!")
                play = False
            else:
                print(f"\nYour current hand is: {plyr_hand}")
                print(f"Dealer hand is: {dealer_hand}")
                print("Dealer wins!")
                play = False
        
    
blackjack()
while True:
    play_again = input("\nPlay Again? Y or N: ")
    play_again = play_again.casefold()
    if play_again == "y":
        print("\n ---New Game---")
        player1.clear_hand()
        dealer.clear_hand() 
        player1.deal_hand()
        dealer.deal_hand()
        play = True
        blackjack()
    elif play_again == "n":
        exit()
    else:
        print("Invalid input")    

    
        
        
