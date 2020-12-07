import os

TEST_BAGS = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

TEST_BAGS_TWO = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


def at_least_contain(bags: dict, color: str = 'shiny gold'):
    colors = set()
    popping_colors = {color}

    while len(popping_colors) > 0:
        current_color = popping_colors.pop()
        for left in bags.keys():
            rights = bags[left]
            for num, right in rights:
                if right == current_color:
                    colors.add(left)
                    popping_colors.add(left)
    return colors


def count_inner_bags(bags: dict, color: str = 'shiny gold'):
    bag_count = 0
    for right in bags[color]:
        bag_count += right[0] + right[0] * count_inner_bags(bags, right[1])
    return bag_count


def solution():
    # bag_rules = TEST_BAGS
    # bag_rules = TEST_BAGS_TWO
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        bag_rules = fd.read()
    bag_rules = bag_rules.split("\n")

    bags = {}
    for bag_rule in bag_rules:
        left, right = bag_rule.split("contain")[0], bag_rule.split("contain")[1]
        left = left.split(" bags ")[0]
        right = right[1:-1]
        rights = [right.split(" bag")[0].split(" bags")[0].split(" ") for right in right.split(", ")]
        bags[left] = [(int(right[0]), " ".join(right[1:])) for right in rights if right[0] != "no"]

    # PART ONE
    print("1:", len(at_least_contain(bags)))

    # PART TWO
    print("2:", count_inner_bags(bags))


if __name__ == '__main__':
    solution()
