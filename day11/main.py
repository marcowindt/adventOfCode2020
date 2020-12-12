import os
from copy import deepcopy

FLOOR = '.'
EMPTY = "L"
OCCUPIED = "#"
TEST_SEATS = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

DIRECTIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),            (0, 1),
    (1, -1),   (1, 0),  (1, 1)
]


def all_adjacent_not_occupied(seats: list, i: int, j: int) -> bool:
    for (dx, dy) in DIRECTIONS:
        cur_i, cur_j = i + dx, j + dy
        if 0 <= cur_i < len(seats) and 0 <= cur_j < len(seats[0]) and seats[cur_i][cur_j] == OCCUPIED:
            return False
    return True


def count_adjacent_occupied(seats: list, i: int, j: int) -> int:
    cnt = 0
    for (dx, dy) in DIRECTIONS:
        cur_i, cur_j = i + dx, j + dy
        if 0 <= cur_i < len(seats) and 0 <= cur_j < len(seats[0]) and seats[cur_i][cur_j] == OCCUPIED:
            cnt += 1
    return cnt


def all_visible_not_occupied(seats: list, i: int, j: int) -> bool:
    for (dx, dy) in DIRECTIONS:
        cur_i, cur_j = i + dx, j + dy
        while 0 <= cur_i < len(seats) and 0 <= cur_j < len(seats[0]):
            if seats[cur_i][cur_j] == OCCUPIED:
                return False
            if seats[cur_i][cur_j] == EMPTY:
                break
            cur_i, cur_j = cur_i + dx, cur_j + dy
    return True


def count_visible_occupied(seats, i: int, j: int) -> int:
    cnt = 0
    for (dx, dy) in DIRECTIONS:
        cur_i, cur_j = i + dx, j + dy
        while 0 <= cur_i < len(seats) and 0 <= cur_j < len(seats[0]):
            if seats[cur_i][cur_j] == OCCUPIED:
                cnt += 1
                break
            if seats[cur_i][cur_j] == EMPTY:
                break
            cur_i, cur_j = cur_i + dx, cur_j + dy
    return cnt


def count_seat(seats: list, seat: str = OCCUPIED) -> int:
    res = 0
    for seat_row in seats:
        res += list(seat_row).count(seat)
    return res


def perform_changes(seats: list, changes: dict) -> list:
    for cell in changes.keys():
        seats[cell[0]][cell[1]] = changes[cell]
    return seats


def print_seats(seats: list):
    for seat_row in seats:
        print("".join(seat_row))


def solution():
    # seats = TEST_SEATS
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        seats = fd.read()
    raw_seats = [list(seat_row) for seat_row in seats.splitlines()]

    # PART ONE
    seats = deepcopy(raw_seats)
    changes = dict()
    keeps_changing = True
    while keeps_changing:
        keeps_changing = False
        seats = perform_changes(seats, changes)
        changes = dict()
        for i, seat_row in enumerate(seats):
            for j, seat in enumerate(seat_row):
                if seat == FLOOR:
                    continue
                elif seat == EMPTY and all_adjacent_not_occupied(seats, i, j):
                    keeps_changing = True
                    changes[(i, j)] = OCCUPIED
                elif seat == OCCUPIED and count_adjacent_occupied(seats, i, j) >= 4:
                    keeps_changing = True
                    changes[(i, j)] = EMPTY
    # print_seats(seats)
    print("1:", count_seat(seats))

    # PART TWO, too slow but works
    seats = deepcopy(raw_seats)
    changes = dict()
    keeps_changing = True
    while keeps_changing:
        keeps_changing = False
        seats = perform_changes(seats, changes)
        changes = dict()
        for i, seat_row in enumerate(seats):
            for j, seat in enumerate(seat_row):
                if seat == FLOOR:
                    continue
                if seat == EMPTY and all_visible_not_occupied(seats, i, j):
                    keeps_changing = True
                    changes[(i, j)] = OCCUPIED
                elif seat == OCCUPIED and count_visible_occupied(seats, i, j) >= 5:
                    keeps_changing = True
                    changes[(i, j)] = EMPTY
    print("2:", count_seat(seats), "<- slow i know")


if __name__ == '__main__':
    solution()
