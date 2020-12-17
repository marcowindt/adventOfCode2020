import os
from collections import defaultdict
from itertools import product

INACTIVE = 0
ACTIVE = 1
TEST_CUBES = """.#.
..#
###"""


def find_neighbors(position: tuple) -> set:
    offsets = product((-1, 0, 1), repeat=len(position))
    return {tuple(a + b for a, b in zip(position, offset)) for offset in offsets if offset != (0,) * len(position)}


def cycle_cubes(cubes_active: dict, num_cycles: int = 6) -> dict:
    """ Returns dict of active cubes after `num_cycles` cycles"""
    cycle = 0
    while cycle < num_cycles:
        becomes_inactive = set()
        becomes_active = set()

        to_add = set(cubes_active.keys())
        for cube_pos in cubes_active.keys():
            neighbors = find_neighbors(cube_pos)
            for neighbor in neighbors:
                to_add.add(neighbor)

        for cube_pos in to_add:
            neighbors = find_neighbors(cube_pos)
            n_active_count = 0

            for neighbor in neighbors:
                if neighbor in cubes_active:
                    n_active_count += 1
                    if n_active_count > 3:
                        break

            if cube_pos in cubes_active and n_active_count != 2 and n_active_count != 3:
                becomes_inactive.add(cube_pos)
            if cube_pos not in cubes_active and n_active_count == 3:
                becomes_active.add(cube_pos)

        for cube_pos in becomes_inactive:
            del cubes_active[cube_pos]
        for cube_pos in becomes_active:
            cubes_active[cube_pos] = ACTIVE
        cycle += 1
    return cubes_active


def solution():
    # cubes = TEST_CUBES
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        cubes = fd.read()
    cubes = [[c for c in cube] for cube in cubes.splitlines()]

    # PART ONE
    cubes_active = defaultdict(int)  # apparently faster
    for i, cube_row in enumerate(cubes):
        for j, cube in enumerate(cube_row):
            if cube == '#':
                cubes_active[(i, j, 0)] = ACTIVE

    cubes_active = cycle_cubes(cubes_active)
    print("1:", len(cubes_active))

    # PART TWO
    cubes_active = defaultdict(int)  # apparently faster
    for i, cube_row in enumerate(cubes):
        for j, cube in enumerate(cube_row):
            if cube == '#':
                cubes_active[(i, j, 0, 0)] = ACTIVE

    cubes_active = cycle_cubes(cubes_active)
    print("2:", len(cubes_active))


if __name__ == '__main__':
    solution()
