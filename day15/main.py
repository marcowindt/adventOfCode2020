import os


TEST = """0,3,6"""
TEST_1 = """1,3,2"""
TEST_2 = """2,1,3"""
TEST_3 = """1,2,3"""
TEST_4 = """2,3,1"""
TEST_5 = """3,2,1"""
TEST_6 = """3,1,2"""

TARGET = 30000000


def solution():
    # tests = [TEST, TEST_1, TEST_2, TEST_3, TEST_4, TEST_5, TEST_6]
    # numbers = tests[0]
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        numbers = fd.read()
    numbers = [int(num) for num in numbers.split(",")]

    last_seen = {numbers[i]: i for i in range(len(numbers) - 1)}

    turn = len(numbers) - 1
    while turn < TARGET:
        last_spoken = numbers[turn]

        if last_spoken not in last_seen:
            # first time
            numbers.append(0)
        else:
            # spoken before
            difference = turn - last_seen[last_spoken]
            numbers.append(difference)

        last_seen[last_spoken] = turn
        turn += 1

    print("1:", numbers[2019])
    print("2:", numbers[29999999])


if __name__ == '__main__':
    solution()
