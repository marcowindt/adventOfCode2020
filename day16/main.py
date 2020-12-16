import os


TEST_TICKETS = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""


def possible_classes_for_num(rules: dict, num: int) -> set:
    valid_set = set()
    for rule in rules.keys():
        rs = rules[rule]
        r0 = rs[0]
        r1 = rs[1]
        if r0[0] <= num <= r0[1] or r1[0] <= num <= r1[1]:
            valid_set.add(rule)
    return valid_set


def solution():
    # tickets = TEST_TICKETS
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        tickets = fd.read()

    rules = {rule.split(": ")[0]: [(int(rule.split(": ")[1].split(" or ")[0].split("-")[0]), int(rule.split(": ")[1].split(" or ")[0].split("-")[1])), (int(rule.split(": ")[1].split(" or ")[1].split("-")[0]), int(rule.split(": ")[1].split(" or ")[1].split("-")[1]))]for rule in tickets.split("\n\n")[0].splitlines()}
    your_ticket = [int(value) for value in tickets.split("\n\n")[1].splitlines()[1].split(",")]
    nearby_tickets = [[int(value) for value in ticket.split(",")] for ticket in tickets.split("\n\n")[2].splitlines()[1:]]

    # PART ONE
    invalid_nums = []
    invalid_tickets = set()
    for i, nearby_ticket in enumerate(nearby_tickets):
        for number in nearby_ticket:
            valid = False
            for field in rules.keys():
                ranges = rules[field]
                for r in ranges:
                    if r[0] <= number <= r[1]:
                        # valid
                        valid = True
                        break
            if not valid:
                invalid_nums.append(number)
                invalid_tickets.add(i)
    print("1:", sum(invalid_nums))

    invalid_tickets = list(invalid_tickets)
    invalid_tickets.sort(reverse=True)

    # PART TWO
    for invalid_ticket in invalid_tickets:
        del nearby_tickets[invalid_ticket]

    all_classes = set(rules.keys())
    option_classes = {i: all_classes.copy() for i in range(len(nearby_tickets[0]))}

    nearby_tickets.append(your_ticket)
    for nearby_ticket in nearby_tickets:
        for i, num in enumerate(nearby_ticket):
            option_classes[i] = option_classes[i].intersection(possible_classes_for_num(rules, num))

    i = 0
    # big enough number
    while i < 100:
        for option in option_classes.keys():
            classes = option_classes[option]
            if len(classes) == 1:
                for other_option in option_classes.keys():
                    if other_option != option:
                        option_classes[other_option] = option_classes[other_option].difference(option_classes[option])
        i += 1

    result = 1
    for option in option_classes:
        cur_class = option_classes[option].pop()
        if len(cur_class) > 9 and cur_class[:9] == "departure":
            result *= your_ticket[option]
    print("2:", result)


if __name__ == '__main__':
    solution()
