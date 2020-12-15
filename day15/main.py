import os


TEST = """0,3,6"""
TEST_1 = """1,3,2"""
TEST_2 = """2,1,3"""
TEST_3 = """1,2,3"""
TEST_4 = """2,3,1"""
TEST_5 = """3,2,1"""
TEST_6 = """3,1,2"""


def solution():
    # tests = [TEST, TEST_1, TEST_2, TEST_3, TEST_4, TEST_5, TEST_6]
    # numbers = tests[6]
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        numbers = fd.read()
    numbers = [int(num) for num in numbers.split(",")]

    last_seen = dict()
    prev_last_seen = dict()
    for i, num in enumerate(numbers):
        if i != len(numbers) - 1:
            if num in last_seen:
                prev_last_seen[num] = last_seen[num]
            last_seen[num] = i

    turn = len(numbers)
    while turn < 30000000:
        last_spoken = numbers[turn - 1]

        if last_spoken not in prev_last_seen:
            # first time
            numbers.append(0)

            if last_spoken in last_seen:
                prev_last_seen[last_spoken] = last_seen[last_spoken]
            last_seen[last_spoken] = turn - 1

            if 0 in last_seen:
                prev_last_seen[0] = last_seen[0]
            last_seen[0] = turn
        else:
            # spoken before
            difference = last_seen[last_spoken] - prev_last_seen[last_spoken]
            numbers.append(difference)
            if difference in last_seen:
                prev_last_seen[difference] = last_seen[difference]
            last_seen[difference] = turn

        turn += 1

    print("1:", numbers[2019])
    print("2:", numbers[29999999])


if __name__ == '__main__':
    solution()
