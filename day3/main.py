import os

TREE = "#"
EMPTY = "."


def count_trees(forest: list, plus_right: int = 3, plus_down: int = 1) -> int:
    cur_pos = [0, 0]
    tree_count = 0
    while cur_pos[0] < len(forest):
        if forest[cur_pos[0]][cur_pos[1]] == TREE:
            tree_count += 1

        cur_pos[0] += plus_down
        cur_pos[1] = (cur_pos[1] + plus_right) % len(forest[0])
    return tree_count


def solution():
    forest = []
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        for line in fd:
            forest.append(line.split("\n")[0])

    # PART ONE
    print("1:", count_trees(forest, plus_right=3, plus_down=1))

    # PART TWO
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    multiplied = 1
    for slope in slopes:
        multiplied *= count_trees(forest, plus_right=slope[0], plus_down=slope[1])
    print("2:", multiplied)


if __name__ == "__main__":
    solution()
