import os


TEST_GROUP_ANSWERS = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def solution():
    # group_answers = TEST_GROUP_ANSWERS
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        group_answers = fd.read()
    group_answers = group_answers.split("\n\n")
    group_answers = [group_answer.split("\n") for group_answer in group_answers]

    # PART ONE
    yes_counts = []
    for group_answer in group_answers:
        group_set = set(group_answer[0])
        for answer in group_answer[1:]:
            group_set = group_set.union(set(answer))
        yes_counts.append(len(group_set))
    print("1:", sum(yes_counts))

    # PART TWO
    yes_counts = []
    for group_answer in group_answers:
        group_set = set(group_answer[0])
        for answer in group_answer[1:]:
            group_set = group_set.intersection(set(answer))
        yes_counts.append(len(group_set))
    print("2:", sum(yes_counts))


if __name__ == '__main__':
    solution()
