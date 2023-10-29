import  random
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        if self.rank == 1:
            self.rank = 15

    def __repr__(self):
        if self.rank == 16 or self.rank == 'joker':
            return f' {self.suit} joker'
        if self.rank == 15 or self.rank == 'ace':
            return f' {self.suit} ace'
        if self.rank == 11 or self.rank == 'Jack':
            return f' {self.suit} Jack'
        elif self.rank == 12 or self.rank == 'Queen':
            return f' {self.suit} Queen'
        elif self.rank == 13 or self.rank == 'King':
            return f' {self.suit} King'
        elif  self.rank < 11 :
            return f' {self.suit} {self.rank}'
        else:
            return f'such a rank doesnt exist'


    def __lt__(self, a):
        return self.rank < a.rank

    def __gt__(self, a):
        if self.rank > a.rank:
            return True
        else: return False

    def __eq__(self, other):
        return self.rank == other.rank


class joker(Card):
    def __init__(self):
        super().__init__("joker", 16)







class Deck:

    def __init__(self):
        card_suits=["diamond(♦)", "clubs(♣)", "hearts(♥)", "spades(♠)"]
        ranks=[i for i in range(1,14)]
        self.deck = []
        for suit in card_suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))


    def shuffle(self):
        x_deck = []
        while len(self.deck) > 0:
            ran = random.randint(0, len(self.deck) - 1)
            x_deck.append(self.deck[ran])
            self.deck.pop(ran)
        self.deck = x_deck
        return self.deck

    def draw(self):
        return self.deck.pop(-1)

    def list(self):
        return list(self.deck)


    def __len__(self):
        return len(self.deck)


    def __str__(self):  #  return a str or list
        return str(self.deck)

    def __getitem__(self, i):
        return self.deck[i]

    def add_joker(self):
        #jokers = [joker(), joker()]
        self.deck.append(joker())
        self.deck.append(joker())


    def sort_by_suit (self): #: A method to sort the deck by suit
        self.deck.sort(key=lambda x: x.suit)

    def sort_by_rank(self):  # A method to sort the deck by rank.
        self.deck.sort(key=lambda x: x.rank)

    def deal_hand(self, num_cards):
        hand = []
        i = 0
        while i < num_cards:
            hand.append(self.draw())
            i += 1
        return hand




def count_cards(deck ):  # method to count how many cards of each rank are in the deck.
    counter = [0 for i in range(14)]
    for card in deck:
        counter[card.rank-1] += 1

    return counter