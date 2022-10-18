import random

suits = ('spades', 'clubs', 'hearts', 'diamonds')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return f"{self.value} of {self.suit}".title()

class Deck():
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.deck.append(card)
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal_one(self):
        return self.deck.pop(0)
    
    def __str__(self):
        return f"Pack of cards"
    
    def __len__(self):
        return len(self.deck)

class Player():
    def __init__(self, total=100):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self, total = 100):
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def hit_or_stand(deck, player):
    while True:
        hit_or_stand = input("Hit or Stand? Enter h to hit or s to stay: ")
        if hit_or_stand.lower() == 'h':
            hit(deck, player)
            print(f"\nAdded new card: {player.cards[-1]}\n")
            print(f"Value of your cards: {player.value} \n")
            break
        elif hit_or_stand.lower() == 's':
            print("Player stands. Dealer is playing.")
            break
        else:
            print('Sorry, please try again')
            continue

def hit(deck, player):
    player.add_card(deck.deal_one())
    player.adjust_for_ace()

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How much amount would you like to bet? '))
        except ValueError:
            print("Please enter valid amount")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed 100")
            else:
                break

def play():
    print("Welcome to Blackjack!!! \n")

    while True:
        deck = Deck()
        deck.shuffle()
        
        dealer = Player()
        dealer.add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())

        player_chips = Chips()  
        take_bet(player_chips)

        player = Player()
        player.add_card(deck.deal_one())
        player.add_card(deck.deal_one())
        player.adjust_for_ace()

        print(f"\nDealer's card 1: {dealer.cards[0]} \n")
        print(f"Your card 1: {player.cards[0]} \n")
        
        input("Press enter to see the value of your 2nd card \n")
        
        print(f"Your card 2: {player.cards[1]} \n")
        print(f"Your total card value: {player.value} \n")

        hit_or_stand(deck, player)

        if player.value > 21:
            print("Player busts!")
            player_chips.lose_bet()
            print("\nPlayer's winnings stand at ",player_chips.total)
            
        if player.value <= 21:
            while dealer.value < 17:
                hit(deck, dealer)

            print("Dealers card: ", *dealer.cards, sep="\n")
            print(f"\nDealers value: {dealer.value}\n")

            if dealer.value > 21:
                print("Dealer busts!")
                player_chips.win_bet()
            elif dealer.value > player.value:
                print("Dealer wins!")
                player_chips.lose_bet()
            elif player.value > dealer.value:
                print("Player Wins!")
                player_chips.win_bet()
            else:
                print("Dealer and Player tie! It's a push.")
            
            print("\nPlayer's winnings stand at ",player_chips.total)

            new_game = input("Would you like to play another game? Enter 'y' or 'n' ")
        
            if new_game[0].lower()=='y':
                continue
            else:
                print("Thanks for playing!")
                break


if __name__ == "__main__":
    play()