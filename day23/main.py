import os
from copy import deepcopy


TEST_CUPS = """389125467"""


class Cup:

    def __init__(self, label: int, prev=None, next=None):
        self.label = label
        self.prev = prev
        self.next = next

    def __repr__(self):
        return "->{}".format(self.label)


class Cups:

    def __init__(self, start):
        self.start = start
        self.head = start
        self.cup_dict = dict()
        self.cup_dict[start.label] = self.start

    def append(self, label: int):
        new_node = Cup(label)
        if self.start is None:
            self.start = new_node
            self.head = self.start
        else:
            self.head.next = new_node
            new_node.prev = self.head
            self.head = new_node
        self.cup_dict[label] = new_node

    def remove_right_3(self, label: int):
        current_cup = self.cup_dict[label]
        first_cup = current_cup.next
        second_cup = current_cup.next.next
        third_cup = current_cup.next.next.next
        new_end = third_cup.next
        current_cup.next = new_end
        new_end.prev = current_cup
        first_cup.prev = None
        third_cup.next = None
        return [first_cup, second_cup, third_cup]

    def append_after_3(self, label: int, first_cup: Cup):
        start_cup = self.cup_dict[label]
        end_cup = start_cup.next
        end_cup.prev = first_cup.next.next
        start_cup.next = first_cup
        first_cup.prev = start_cup
        end_cup.prev.next = end_cup

    def connect_both_ends(self):
        self.head.next = self.start
        self.start.prev = self.head

    def __repr__(self):
        if self.start is None:
            return "->"
        else:
            n = self.start
            t = ""
            first = True
            while n is not None and (n is not self.start or first):
                first = False
                t += "->{}".format(n.label)
                n = n.next
            return t


def game(new_cups: list, moves: int = 100):
    cups = Cups(Cup(new_cups[0]))

    for i in range(1, len(new_cups)):
        cups.append(new_cups[i])
    cups.connect_both_ends()

    move = 1
    lowest_cup = 1
    highest_cup = len(new_cups)
    current_cup = cups.start
    while move <= moves:
        pick_up = cups.remove_right_3(current_cup.label)

        destination_cup_label = current_cup.label - 1
        while destination_cup_label in [c.label for c in pick_up] or destination_cup_label < lowest_cup:
            destination_cup_label = destination_cup_label - 1
            if destination_cup_label < lowest_cup:
                destination_cup_label = highest_cup

        cups.append_after_3(destination_cup_label, pick_up[0])
        current_cup = current_cup.next
        move += 1

    return cups


def solution():
    # cups = TEST_CUPS
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        cups = fd.read()
    init_cups = [int(c) for c in cups]  # + [i for i in range(10, 1000001)]

    # PART ONE
    new_cups = deepcopy(init_cups)
    cups = game(new_cups)
    print("1:", cups)

    # PART TWO
    new_cups = deepcopy(init_cups) + [i for i in range(10, 1000001)]
    cups = game(new_cups, moves=10000000)

    first = cups.cup_dict[1].next.label
    second = cups.cup_dict[1].next.next.label
    print("2:", first, second, first * second)


if __name__ == '__main__':
    solution()
