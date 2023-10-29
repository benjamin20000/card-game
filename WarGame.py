import math
import random

from Cards import Deck


class Player:
    def __init__(self, name: str, hand: list):
        self.name = name
        self.hand = hand

    def __repr__(self):
        return self.name

    def __len__(self):
        return len(self.hand)


class Game:
    def __init__(self, player_1_name, player_2_name):
        self.game_over = False
        deck = Deck()
        deck.shuffle()
        self.player_1 = Player(player_1_name, deck.deal_hand(len(deck)//2))
        self.player_2 = Player(player_2_name, deck.list())
        #self.rounds = 20000

    def play_round(self, cards_cash=None):
        if cards_cash is None:
            cards_cash = []
        while self.game_over is False: #and self.rounds > 0 :
            #self.rounds -= 1
            player_1_card = self.player_1.hand.pop(0)
            player_2_card = self.player_2.hand.pop(0)
            cards_cash.append(player_1_card)
            cards_cash.append(player_2_card)
            if player_1_card > player_2_card:
                self.player_1.hand += cards_cash
                cards_cash = []
            elif player_2_card > player_1_card:
                self.player_2.hand += cards_cash
                cards_cash = []
            elif player_2_card == player_1_card:
                self.check_it_over()
                self.war(cards_cash)
            self.shuffle()
            #print(len(self.player_1.hand))
            self.check_it_over()
        winner = self.how_winne()

        return winner#,#20000-self.rounds
    def shuffle(self):
        random.shuffle(self.player_1.hand)
        random.shuffle(self.player_2.hand)
    def war(self, cards_cash: list):
        i = 0
        while i < 3 and self.game_over == False:
            cards_cash.append(self.player_1.hand.pop(0))
            cards_cash.append(self.player_2.hand.pop(0))
            i += 1
            self.check_it_over()
        self.play_round(cards_cash)


    def check_it_over(self):
        if len(self.player_1.hand) == 0 or len(self.player_2.hand) == 0:
            self.game_over = True


    def how_winne(self):
        if len(self.player_1.hand) > len(self.player_2.hand):
            return self.player_1
        else:
            return self.player_2


G = Game("A", "B")
print(G.play_round())
print(G.player_1.hand)
print(G.player_2.hand)