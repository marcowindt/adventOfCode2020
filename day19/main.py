import os
import re


TEST_RULES = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

TEST_RULES_LOOP = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""


class Node:

    def __init__(self, val, children: list):
        self.val = val
        self.children = children

    def __str__(self):
        return "[{}: {}]".format(self.val, self.children)


def solve(rules: dict, num, recursive: dict, depth: int = 0):
    if rules[num] == [['a']]:
        return Node('a', [])
    elif rules[num] == [['b']]:
        return Node('b', [])
    else:
        pattern = ""
        children = []
        for sub_rule in rules[num]:
            sub_pattern = "("
            sub_children = []
            for p in sub_rule:
                if p == num:
                    if p in recursive:
                        if recursive[p] > depth:
                            break
                        else:
                            recursive[p] += 1
                    else:
                        recursive[p] = 1
                child = solve(rules, p, recursive, depth)
                sub_children.append(child)
                sub_pattern += child.val
            sub_pattern += ")"
            pattern += sub_pattern + "|"
            children.append(sub_children)

        return Node("(" + pattern[:-1] + ")", children)


def get_pattern(rules: dict, depth: int = 0):
    pattern = ''
    for x in rules[0][0]:
        pattern += solve(rules, x, {}, depth=depth).val
    return pattern


def solution():
    # rules = TEST_RULES
    # rules = TEST_RULES_LOOP
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        rules = fd.read()

    # PREPROCESS
    rules, messages = rules.split("\n\n")
    rules = rules.splitlines()
    messages = messages.splitlines()

    rules_d = dict()
    for rule in rules:
        k = int(rule.split(": ")[0])
        r = rule.split(": ")[1]
        rights = []
        for right in r.split(" | "):
            vs = []
            for v in right.split(" "):
                try:
                    vs.append(int(v))
                except ValueError:
                    vs.append(v[1])
            rights.append(vs)
        rules_d[k] = rights
    rules = rules_d

    # PART ONE
    pattern = get_pattern(rules)
    print("1:", len([message for message in messages if re.fullmatch(pattern, message) is not None]))

    # PART TWO - LOOP RULES
    # UPDATE THE FOLLOWING RULES
    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 3
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    # depth = 3 == 3 recursions, was enough
    pattern = get_pattern(rules, depth=3)
    print("2:", len([message for message in messages if re.fullmatch(pattern, message) is not None]))


if __name__ == '__main__':
    solution()
