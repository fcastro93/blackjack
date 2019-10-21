from random import randint

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

hands = {}


# Main method, controls the entire game and calls other methods
def game():
    # Basic variables
    print("Enter # players: ")
    players = int(input())
    turn_player = 1
    cards = 52
    cards_dealt = []

    for player in range(players):
        [draw(cards, cards_dealt, turn_player, players) for _ in range(2)]
    print("********")

    show_hands(turn_player)
    # draw(cards, cards_dealt, turn_player, players)


# Draw cards
def draw(cards, cards_dealt, turn_player, players):
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
    for card in hands:
        print("Player {0}".format(turn_player))
        print (hands.get(turn_player))

# Run program
game()