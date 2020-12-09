import os

TEST_NUMBERS = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def solution():
    # numbers, preamble = TEST_NUMBERS, 5
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        numbers = fd.read()
    numbers = [int(num) for num in numbers.splitlines()]
    preamble = 25

    # PART ONE
    invalid_number = -1
    for i in range(preamble, len(numbers)):
        # print("new range: {} - {}".format(i - preamble, i))
        valid = False
        for j in range(i - preamble, i):
            if numbers[i] - numbers[j] in numbers[i - preamble:i]:
                valid = True
                break
        if not valid:
            invalid_number = numbers[i]
            print("1: {} (idx) {} (num)".format(i, numbers[i]))
            break

    # PART TWO
    assert invalid_number > -1
    start, end = 0, 1

    while sum(numbers[start:end]) != invalid_number:
        if sum(numbers[start:end]) > invalid_number:
            start += 1
        elif sum(numbers[start:end]) < invalid_number:
            end += 1
    num_range = numbers[start:end]
    num_min = min(num_range)
    num_max = max(num_range)
    num_sum = num_min + num_max
    print("2: [{}, {}]: {} (min), {} (max), {} (sum)".format(start, end, num_min, num_max, num_sum))


if __name__ == '__main__':
    solution()
