import os
from math import ceil, gcd, lcm

TEST_IDS = """939
7,13,x,x,59,x,31,19"""

TEST_EXTRA = """0
17,x,13,19"""

TEST_EXTRA_2 = """0
67,7,59,61"""

TEST_EXTRA_3 = """0
67,x,7,59,61"""

TEST_EXTRA_4 = """0
67,7,x,59,61"""

TEST_EXTRA_5 = """0
1789,37,47,1889"""


def correct_timestamp(buses: list, timestamp: int) -> bool:
    for (i, bus) in buses:
        if not ((timestamp + i) / bus).is_integer():
            return False
    return True


def solution():
    # ids = TEST_IDS
    # ids = TEST_EXTRA
    # ids = TEST_EXTRA_2
    # ids = TEST_EXTRA_3
    # ids = TEST_EXTRA_4
    # ids = TEST_EXTRA_5
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        ids = fd.read()
    ids = ids.splitlines()
    estimate = int(ids[0])
    buses = [(i, int(bus)) for i, bus in enumerate(ids[1].split(",")) if bus != 'x']

    # PART ONE
    times = {}
    for bus in buses:
        times[ceil(estimate / bus[1]) * bus[1]] = bus[1]

    print("1:", min(times), times[min(times)], (min(times) - estimate) * times[min(times)])

    # PART TWO - CHINESE REMAINDER THEOREM:
    #
    # x_i = b_i (mod n_i)
    # big_n = product(n_i for i, n_i in buses)
    # big_n_i = big_n // n_i
    # x = sum(b_i * big_n_i * x_i) % big_n

    # Product of all moduli == product(all_bus_ids)
    big_n = lcm(*[bus for i, bus in buses])

    # Calculate all big_n_i
    big_n_i_s = [big_n // n_i for i, n_i in buses]

    # All bs <=> index in bus id list
    bs = [i for i, bus in buses]

    # All xs (modulo inverses) <=> ids of buses
    xs = [pow(big_n_i, -1, bus) for big_n_i, (i, bus) in zip(big_n_i_s, buses)]

    # Find x <=> timestamp t
    sum_bi_ni_xi = sum([b_i * big_n_i * x_i for b_i, big_n_i, x_i in zip(bs, big_n_i_s, xs)])
    timestamp = -sum_bi_ni_xi % big_n
    print("2: {}".format(timestamp))


if __name__ == '__main__':
    solution()
