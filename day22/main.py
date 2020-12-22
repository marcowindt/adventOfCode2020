import os
from collections import defaultdict, deque
from copy import deepcopy
from typing import Deque

TEST_DECKS = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

known_games = dict()


def game(deck_1: Deque, deck_2: Deque):
    prev_rounds = set()
    while len(deck_1) != 0 and len(deck_2) != 0:
        round_id = "".join((":".join(str(x) for x in deck_1), ":".join(str(x) for x in deck_2)))

        if round_id in prev_rounds:
            # player 1 wins
            p1_card = deck_1.popleft()
            p2_card = deck_2.popleft()
            deck_1.append(p1_card)
            deck_1.append(p2_card)
            continue
        prev_rounds.add(round_id)

        p1_card = deck_1.popleft()
        p2_card = deck_2.popleft()

        if p1_card <= len(deck_1) and p2_card <= len(deck_2):
            # recursive combat
            recursive_deck_1 = deque([deck_1[n] for n in range(p1_card)])
            recursive_deck_2 = deque([deck_2[n] for n in range(p2_card)])

            recursive_round_id = "".join((":".join(str(x) for x in recursive_deck_1), ":".join(str(x) for x in recursive_deck_2)))

            if recursive_round_id not in known_games:
                res_deck_1, res_deck_2 = game(recursive_deck_1, recursive_deck_2)
                known_games[recursive_round_id] = len(res_deck_2) == 0

            if known_games[recursive_round_id]:
                # player 1 wins
                deck_1.append(p1_card)
                deck_1.append(p2_card)
            else:
                # player 2 wins
                deck_2.append(p2_card)
                deck_2.append(p1_card)
        else:
            if p1_card > p2_card:
                # player 1 wins normal game
                deck_1.append(p1_card)
                deck_1.append(p2_card)
            else:
                # player 2 wins normal game
                deck_2.append(p2_card)
                deck_2.append(p1_card)
    return deck_1, deck_2


def score(deck: tuple) -> int:
    s = 0
    for i, c in zip(range(len(deck), 0, -1), range(len(deck))):
        s += deck[c] * i
    return s


def solution():
    # decks = TEST_DECKS
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        decks = fd.read()

    decks = decks.split("\n\n")
    init_deck_1 = tuple([int(card) for card in decks[0].split("Player 1:\n")[1].split("\n")])
    init_deck_2 = tuple([int(card) for card in decks[1].split("Player 2:\n")[1].split("\n")])

    deck_1 = deepcopy(init_deck_1)
    deck_2 = deepcopy(init_deck_2)

    while len(deck_1) != 0 and len(deck_2) != 0:
        p1_card = deck_1[0]
        p2_card = deck_2[0]
        deck_1 = deck_1[1:]
        deck_2 = deck_2[1:]
        if p1_card > p2_card:
            # player 1 wins
            deck_1 += (p1_card,)
            deck_1 += (p2_card,)
        else:
            # player 2 wins
            deck_2 += (p2_card,)
            deck_2 += (p1_card,)
    deck_1_score, deck_2_score = score(deck_1), score(deck_2)
    print("1:", max(deck_1_score, deck_2_score))

    deck_1 = deepcopy(init_deck_1)
    deck_2 = deepcopy(init_deck_2)

    deck_1 = deque(deck_1)
    deck_2 = deque(deck_2)

    deck_1, deck_2 = game(deck_1, deck_2)
    deck_1_score, deck_2_score = score(deck_1), score(deck_2)
    print("2:", max(deck_1_score, deck_2_score))


if __name__ == '__main__':
    solution()
