import os
from itertools import combinations


SMALL_TEST = """16
10
15
5
1
11
7
19
6
12
4"""

TEST_NUMBERS = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


def tribonacci(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


def solution():
    # numbers = TEST_NUMBERS
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        numbers = fd.read()
    numbers = [int(num) for num in numbers.splitlines()]

    numbers.sort()
    numbers = [0] + numbers + [numbers[-1] + 3]

    # PART ONE
    jolts_3 = 0
    jolts_1 = 0
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] == 3:
            jolts_3 += 1
        elif numbers[i + 1] - numbers[i] == 1:
            jolts_1 += 1
    print("1: {} (jolts1), {} (jolts3), {} (product)".format(jolts_1, jolts_3, jolts_1 * jolts_3))

    # PART TWO, put to much time in the wrong, thanks to Reddit for hinting the correct way of solving this
    ones = dict()
    current_tuple = ()
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] == 1:
            current_tuple += (1,)
        else:
            if len(current_tuple) in ones:
                ones[len(current_tuple)] += 1
            else:
                ones[len(current_tuple)] = 1
            current_tuple = ()
    s = 1
    for k in ones.keys():
        x = tribonacci(k)
        s *= x**ones[k]
    print("2:", s)


if __name__ == '__main__':
    solution()
