import random

colours = ['r', 'y', 'g', 'b']
values = [0,1,2,3,4,5,6,7,8,9,'reverse', 'skip', 'draw 2', 'wild +4', 'wild']

def create_deck():
    deck = []
    for v in values[:-2]:
        for c in colours:
            card = (v, c)
            deck.append(card)
            if v == 0:
                continue
            deck.append(card)
    for v in values[-2:]:
        card = (v, 'X')
        deck.append(card)
        deck.append(card)
        deck.append(card)
        deck.append(card)
    return deck

class Game:
    def __init__(self, num_players, deck, used_deck=[], players = [], direction = 'c'):
        self.num_players = num_players
        self.deck = deck
        self.used_deck = used_deck
        self.players = players
        self.direction = direction
        self.deck_size = len(deck)
        self.top_card = deck[0]

    def create_players(self):
        i=0
        while i < self.num_players:
            name = input('Players Name: ')
            player = Player(name)
            self.players.append(player)
            i+=1
        return self.players
    
    def deal(self): #input is a list of players
        players_cards = {}
        for player in self.players:
            print(player)
            cards = []
            for i in range(7):
                card = self.deck.pop(0)
                cards.append(card)
            player.cards = cards
            players_cards[player.name] = cards
        return players_cards
    
    def first_card(self):
        card = self.deck.pop(0)
        self.used_deck.append(card)
        return card
    
    def shuffle(self):
        random.shuffle(self.deck)
        return self.deck

    def change_direction(self):
        if self.direction == 'c':
            self.direction = 'ac'
        else:
            self.direction = 'c'
        self.deck = self.deck[::-1]
        return self.direction


            
    #output is a dictionary with keys as the player and 

class Player:
    def __init__(self, name, cards=[]):
        self.name = name
        self.num_cards = len(cards)
        self.cards = cards

    def __str__(self):
        return self.name


class Card:
    def __init__(self, value, colour):
        self.value = value
        self.colour = colour
    
    def str(self):
        return 'UnoCard(' + self.cardcolor + ', ' + self.cardtype + ')'
    
    def valid(self, used_deck):
        top_card = used_deck[-1]
        if self.colour == top_card[1]:
            return True
        else:
            return False
