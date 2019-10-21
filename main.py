from random import randint

# General Variable, needs to improve

# Types and number of cards
types = {
    0: 'Clubs',
    1: 'Hearts',
    2: 'Diamonds',
    3: 'Spades'
}
numbers = {
    0: "AS",
    1: "2",
    2: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "Jack",
    11: "Queen",
    12: "King"
}
# Cards of every player
hands = {}


# Main method, controls the entire game and calls other methods
def game():
    # Basic variables
    #   If we are playing with 52 cards the software ask how many players are going to play and save
    # the number into players variable. Then, its going to draw two cards for every player
    print("Enter # players: ")
    players = int(input())
    turn_player = 1
    cards = 52
    cards_dealt = []

    for player in range(players):
        [draw(cards, cards_dealt, turn_player, players) for _ in range(2)]
    print("********")

    # TODO:
    # ask every player if he wants to draw a new card, if he answer yes use the next line method
    # draw(cards, cards_dealt, turn_player, players)
    # Then the result is calculated with the blackjack rules explained in the docs
    # at the end, shows every player hands and resolution with methods show_hands(turn_player) and
    # post_winner()


# Draw cards every time its called
def draw(cards, cards_dealt, turn_player, players):
    # Params:
    # cards = number of cards to play with
    # cards_dealt = list with cards give it to every player
    # turn_player = who players its being processing
    # players = how many players are playing this turn
    print("Player {} drawing".format(turn_player))
    if cards > 0:
        while True:
            type = randint(0, 3)
            number = randint(0, 12)
            card = "{0}/{1}".format(types[type], numbers[number])
            if card not in cards_dealt:
                cards_dealt.append(card)
                hands[turn_player] = number
                print(str(card))
                if turn_player == players:
                    turn_player = 1
                else:
                    turn_player += 1
                return card


def show_hands(turn_player):
    # Params:
    # turn_player = who players its being processing
    for card in hands:
        print("Player {0}".format(turn_player))
        print hands.get(turn_player))


# Run program, should be changed to an interface
game()
