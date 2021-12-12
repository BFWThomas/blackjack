from random import randint

class Shoe:
    """
    Class used to define the shoe of playing cards
    Init sets the shoe to a default size of 1 deck, but the class can be initialized with a
    desired number of decks
    """

    def __init__(self, size=1):
        self.shoe = [size] * 52
        self.numCards = size * 52

    def change_size(self, num_decks):
        """
        Updates the shoe size to num_decks
        Returns the shoe array
        """

        self.shoe = [num_decks] * 52
        return self.shoe

    def play_card(self, index):
        if self.shoe[index] > 0:
            self.shoe[index] -= 1
            return True
        else:
            return False

    def card_translation(self, index):
        """
        Given an index as int, return the name of the card that corresponds to the index
        Should only be used for debugging
        """

        # Index is in Spade range (0-12)
        if 0 <= index <= 12:
            if 1 <= index <= 9:
                print("Spade" + (str(index+1)))
            elif index == 0:
                print("SpadeA")
            elif index == 10:
                print("SpadeJ")
            elif index == 11:
                print("SpadeQ")
            elif index == 12:
                print("SpadeK")

        # Index is in Clubs range (13-25)
        elif 13 <= index <= 25:
            if 14 <= index <= 22:
                print("Club" + (str(index-12)))
            elif index == 13:
                print("ClubA")
            elif index == 23:
                print("ClubJ")
            elif index == 24:
                print("ClubQ")
            elif index == 25:
                print("ClubK")

        # Index is in Hearts range (26-38)
        elif 26 <= index <= 38:
            if 27 <= index <= 35:
                print("Heart" + (str(index-25)))
            elif index == 26:
                print("HeartA")
            elif index == 36:
                print("HeartJ")
            elif index == 37:
                print("HeartQ")
            elif index == 38:
                print("HeartK")

        # Index is in Diamonds range (39-51)
        elif 39 <= index <= 51:
            if 40 <= index <= 48:
                print("Diamond" + (str(index-38)))
            elif index == 39:
                print("DiamondA")
            elif index == 49:
                print("DiamondJ")
            elif index == 50:
                print("DiamondQ")
            elif index == 51:
                print("DiamondK")
        else:
            print("Invalid index")
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


class Blackjack:

    def __init__(self, game_shoe):
        dealer = Player(True)
        self.players = [dealer]
        self.shoe = game_shoe

    def add_player(self, player):
        if len(self.players) < 6:
            self.players.append(player)
            return True
        return False

    def deal_hands(self):
        while len(self.players[0].hand) < 2:
            for i in self.players:
                while True:
                    attempt_card = randint(0, 51)
                    if self.shoe.play_card(attempt_card):
                        i.add_to_hand(attempt_card)
                        break
                    else:
                        print("Card already played")
        return

    def show_dealer_hand(self):
        print(self.players[0].hand)


if __name__ == '__main__':
    shoe = Shoe(5)
    game = Blackjack(shoe)
    player1 = Player()
    player2 = Player()
    player3 = Player()
    player4 = Player()

    game.add_player(player1)
    game.add_player(player2)
    game.add_player(player3)
    game.add_player(player4)

    game.deal_hands()
    for i in game.players:
        print(str(i))
        for j in i.hand:
            shoe.card_translation(j)

    print(shoe.shoe)
