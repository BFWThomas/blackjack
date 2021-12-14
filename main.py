from random import randint, choice
from card_helper import deck

class Shoe:
    """
    Class used to define the shoe of playing cards
    Init sets the shoe to a default size of 1 deck, but the class can be initialized with a
    desired number of decks
    """

    def __init__(self, size=1):
        self.shoe = dict(deck)
        self.change_size(size)
        self.numCards = size * 52

    def change_size(self, num_decks):
        """
        Updates the shoe size to num_decks
        Returns the shoe array
        """
        self.shoe = {x:num_decks for x in self.shoe}
        return self.shoe

    def play_card(self, key):
        if self.shoe[key] > 0:
            self.shoe[key] -= 1
        else:
            self.shoe.pop(key, None)
        return


class Player:
    """
    Used to represent a player
    Player has a hand, bankroll, and a bet amount
    """

    def __init__(self, is_dealer=False):
        self.is_dealer = is_dealer
        self.hand = list()
        self.bankroll = 0
        self.bet = 0

    def adjust_bankroll(self, amount):
        self.bankroll += amount
        return

    def set_bet(self, amount):
        if amount <= self.bet:
            self.bet = amount
        else:
            return False
        return True

    def add_to_hand(self, card):
        self.hand.append(card)
        return

    def hand_value(self):
        total = 0

        for i in self.hand:
            # Remove suits and white space
            card = i[:2].strip()
            # Face cards are 10
            if card == 'J' or card == 'Q' or card == 'K':
                total += 10
            # Aces are 1 or 11
            elif card == 'A':
                # TODO: probably needs to have more careful logic for Aces
                if (total + 11) <= 21:
                    total += 11
                else:
                    total += 1
            # Int cards
            else:
                total += int(card)
        return total


class Blackjack:

    def __init__(self, game_shoe):
        dealer = Player(True)
        self.players = [dealer]
        self.shoe = game_shoe
        self.active_player = None

    def add_player(self, player):
        if len(self.players) < 6:
            self.players.append(player)
            return True
        return False

    def deal_hands(self):
        # Deal cards until players have 2 cards
        while len(self.players[0].hand) < 2:
            for i in self.players:
                card_to_play = choice(list(self.shoe.shoe.items()))[0]
                self.shoe.play_card(card_to_play)
                i.add_to_hand(card_to_play)
        return

    def hit(self, player):
        card_to_play = choice(list(self.shoe.shoe.items()))[0]
        self.shoe.play_card(card_to_play)
        player.add_to_hand(card_to_play)

    def show_dealer_hand(self):
        print(self.players[0].hand)

    def get_dealer_value(self):
        return self.players[0].hand_value()
