import uno
import random

deck = uno.create_deck()

player_num = int(input('Welcome to UNO! How many players? '))

uno = uno.Game(player_num, deck)
uno.shuffle()
uno.create_players()
state = uno.deals()


