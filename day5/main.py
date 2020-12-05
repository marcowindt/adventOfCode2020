import math
import os


def front_back_solve(boarding_pass: str, lower: int = 0, upper: int = 127, i: int = 0, until: int = 6, f: str = "F", b: str = "B"):
    while i < until:
        if boarding_pass[i] == f:
            upper -= math.ceil((upper - lower) / 2)
        elif boarding_pass[i] == b:
            lower += math.ceil((upper - lower) / 2)
        i += 1
    if boarding_pass[until] == f:
        return lower
    return upper


def left_right_solve(boarding_pass: str, lower: int = 0, upper: int = 7, i: int = 7, until: int = 9):
    return front_back_solve(boarding_pass=boarding_pass, lower=lower, upper=upper, i=i, until=until, f="L", b="R")


def solution():
    # test_passes = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    passes = []
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        for line in fd:
            passes.append(line.split("\n")[0])

    # PART ONE
    seat_ids = [front_back_solve(boarding) * 8 + left_right_solve(boarding) for boarding in passes]
    print("1:", max(seat_ids))

    # PART TWO
    for i in range(seat_ids[0], seat_ids[-1] + 1):
        if i not in seat_ids:
            print("2:", i)
            break


if __name__ == '__main__':
    solution()
