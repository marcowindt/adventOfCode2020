import os

TEST_ROUTE = """F10
N3
F7
R90
F11"""


class Action:
    
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value


def solution():
    # route = TEST_ROUTE
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        route = fd.read()
    route = [Action(action[0], int(action[1:])) for action in route.splitlines()]

    # PART ONE
    cur_pos = [0, 0]  # x (left-right), y (up-down)
    cur_facing = 1  # 0: NORTH, 1: EAST, 2: SOUTH, 3: WEST
    for action in route:
        if action.name == 'N':
            cur_pos[1] += action.value
        elif action.name == 'S':
            cur_pos[1] -= action.value
        elif action.name == 'E':
            cur_pos[0] += action.value
        elif action.name == 'W':
            cur_pos[0] -= action.value
        elif action.name == 'L':
            cur_facing = (cur_facing - ((action.value % 360) // 90)) % 4
        elif action.name == 'R':
            cur_facing = (cur_facing + ((action.value % 360) // 90)) % 4
        elif action.name == 'F':
            if cur_facing == 0:
                cur_pos[1] += action.value
            elif cur_facing == 2:
                cur_pos[1] -= action.value
            elif cur_facing == 1:
                cur_pos[0] += action.value
            elif cur_facing == 3:
                cur_pos[0] -= action.value
    print("1:", abs(cur_pos[0]) + abs(cur_pos[1]))

    # PART TWO
    way_point = [10, 1]
    cur_pos = [0, 0]  # x (left-right), y (up-down)
    for action in route:
        if action.name == 'N':
            way_point[1] += action.value
        elif action.name == 'S':
            way_point[1] -= action.value
        elif action.name == 'E':
            way_point[0] += action.value
        elif action.name == 'W':
            way_point[0] -= action.value
        elif action.name == 'L':
            # L 90 = R 270 (10 E, 4 N) => (-4 E, 10 N)
            if action.value == 90:
                way_point = [-way_point[1], way_point[0]]
            # L 180 = R 180 (10 E, 4 N) => (-10 E, -4 N)
            if action.value == 180:
                way_point = [-way_point[0], -way_point[1]]
            # L 270 = R 90 (10 E, 4 N) => (4 E, -10 N)
            if action.value == 270:
                way_point = [way_point[1], -way_point[0]]
        elif action.name == 'R':
            # R 90 (10 E, 4 N) => (4 E, -10 N)
            if action.value == 90:
                way_point = [way_point[1], -way_point[0]]
            # R 180 (10 E, 4 N) => (-10 E, -4 N)
            if action.value == 180:
                way_point = [-way_point[0], -way_point[1]]
            # R 270 (10 E, 4 N) => (-4 E, 10 N)
            if action.value == 270:
                way_point = [-way_point[1], way_point[0]]
        elif action.name == 'F':
            cur_pos[0] += way_point[0] * action.value
            cur_pos[1] += way_point[1] * action.value
    print("2:", abs(cur_pos[0]) + abs(cur_pos[1]))


if __name__ == '__main__':
    solution()
