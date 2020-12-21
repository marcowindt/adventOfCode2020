import os
import re
from hashlib import md5
from math import sqrt
from copy import deepcopy

DIGEST_LEN = 8
TEST_IMAGES = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""

LEFT = 0
TOP = 1
RIGHT = 2
BOTTOM = 3

SEA_MONSTER = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """


def strip_image(images, image):
    fresh_image = []
    p_image = ""
    for square_row in image:
        for i in range(10):
            row = ""
            p_row = ""
            for square in square_row:
                row += "".join(images[square][i])
                p_row += "".join(images[square][i]) + " "
            p_image += p_row + "\n"
            if 1 <= i <= 8:
                fresh_row = ""
                for j in range(len(square_row)):
                    fresh_row += row[(j * 10) + 1:(j * 10) + 9]
                fresh_image.append(fresh_row)
        p_image += "\n"
    return fresh_image, p_image


def left_side_image(image: list):
    left = []
    for image_row in image:
        left.append(image_row[0])
    return left


def right_side_image(image: list):
    right = []
    for image_row in image:
        right.append(image_row[-1])
    return right


def top_side_image(image: list):
    return image[0]


def bottom_side_image(image: list):
    return image[-1]


def get_image_side(image: list, side: int):
    funcs_sides = [left_side_image, top_side_image, right_side_image, bottom_side_image]
    return funcs_sides[side](image)


def rotate2d(ls):
    return list(zip(*ls[::-1]))


def _rotate(ls: list, n: int):
    return ls[n:] + ls[:n]


def rotate(ls: list):
    return _rotate(ls, -1)


def flip_vertical(ls: list):
    return [ls[LEFT], ls[BOTTOM], ls[RIGHT], ls[TOP]]


def flip_vertical2d(ls):
    return ls[::-1]


def flip_horizontal(ls: list):
    return [ls[RIGHT], ls[TOP], ls[LEFT], ls[BOTTOM]]


def flip_horizontal2d(ls):
    new_ls = []
    for ls_row in ls:
        new_ls.append(ls_row[::-1])
    return new_ls


def get_bottom_neighbour(images: dict, tiles_d: dict, sides_d: dict, tile: int):
    side_top = tiles_d[tile][TOP]
    side_bottom = tiles_d[tile][BOTTOM]

    neighbors_top = sides_d[side_top].copy()
    neighbors_bottom = sides_d[side_bottom].copy()
    if len(neighbors_bottom) != 2:
        neighbors = neighbors_top
        tiles_d[tile] = flip_vertical(tiles_d[tile])
        images[tile] = flip_vertical2d(images[tile])
    else:
        neighbors = neighbors_bottom

    # print(tile, side_d, neighbors, tiles_d[tile])
    neighbors.remove(tile)
    neighbor = neighbors.pop()

    while tiles_d[neighbor][TOP] != tiles_d[tile][BOTTOM]:
        tiles_d[neighbor] = rotate(tiles_d[neighbor])
        images[neighbor] = rotate2d(images[neighbor])

    if get_image_side(images[neighbor], TOP) != get_image_side(images[tile], BOTTOM):
        tiles_d[neighbor] = flip_horizontal(tiles_d[neighbor])
        images[neighbor] = flip_horizontal2d(images[neighbor])

    return neighbor


def get_top_row(images: dict, tiles_d: dict, sides_d: dict, corners: list, tile: int):
    current_tile = tile

    # TOP LEFT
    while not (len(sides_d[tiles_d[current_tile][LEFT]]) == 1 and len(sides_d[tiles_d[current_tile][TOP]]) == 1):
        tiles_d[current_tile] = rotate(tiles_d[current_tile])
        images[current_tile] = rotate2d(images[current_tile])

    top_row = [current_tile]
    while current_tile not in corners or current_tile == tile:
        side_c = tiles_d[current_tile][RIGHT]
        neighbors = sides_d[side_c].copy()
        neighbors.remove(current_tile)
        neighbor = neighbors.pop()

        while tiles_d[neighbor][LEFT] != side_c:
            tiles_d[neighbor] = rotate(tiles_d[neighbor])
            images[neighbor] = rotate2d(images[neighbor])

        if get_image_side(images[current_tile], RIGHT) != get_image_side(images[neighbor], LEFT):
            tiles_d[neighbor] = flip_vertical(tiles_d[neighbor])
            images[neighbor] = flip_vertical2d(images[neighbor])

        current_tile = neighbor
        top_row.append(current_tile)
    return top_row


def match_sea_monster(image_part, sea_monster):
    for i, image_row, sea_monster_row in zip(range(len(image_part)), image_part, sea_monster):
        for j, image_cell, sea_monster_cell in zip(range(len(image_row)), image_row, sea_monster_row):
            if sea_monster_cell == '#' and image_cell != '#':
                return False, image_part
    for i, image_row, sea_monster_row in zip(range(len(image_part)), image_part, sea_monster):
        for j, image_cell, sea_monster_cell in zip(range(len(image_row)), image_row, sea_monster_row):
            if sea_monster_cell == '#' and image_cell == '#':
                image_part[i][j] = 'O'
    return True, image_part


def get_image_part(image, sea_monster, i: int = 0, j: int = 0):
    image_rows = image[i:(i+len(sea_monster))]
    image_part = []
    for image_row in image_rows:
        image_part.append(image_row[j:j+len(sea_monster[0])])
    return image_part


def set_image_part(image, image_part, i: int = 0, j: int = 0):
    for k, l in zip(range(i, i + len(image_part)), range(len(image_part))):
        for m, n in zip(range(j, j + len(image_part[0])), range(len(image_part[0]))):
            image[k][m] = image_part[l][n]
    return image


def count_sea_monsters(image):
    sea_monster = [list(monster_part) for monster_part in SEA_MONSTER.splitlines()]

    cnt = 0
    for i in range(len(image) - len(sea_monster)):
        for j in range(len(image[0]) - len(sea_monster[0])):
            image_part = get_image_part(image, sea_monster, i, j)
            matched, new_image_part = match_sea_monster(image_part, sea_monster)
            if matched:
                cnt += 1
                image = set_image_part(image, new_image_part, i, j)
    return cnt, image


def count_hashtags(image) -> int:
    cnt = 0
    for image_row in image:
        cnt += image_row.count('#')
    return cnt


def print_image(image):
    for image_row in image:
        print("".join(image_row))


def solution():
    # images = TEST_IMAGES
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        images = fd.read()

    images = {int(image.split("\n")[0].split(" ")[1].split(":")[0]): [tuple(r) for r in image.split("\n")[1:]] for image in images.split("\n\n")}

    tiles_d = dict()
    sides_d = dict()
    for tile in images.keys():
        side_a = ""
        side_c = ""
        for t in images[tile]:
            side_a += t[0]
            side_c += t[-1]

        side_a = min(side_a, side_a[::-1])                                          # LEFT
        side_b = min("".join(images[tile][0]), "".join(images[tile][0][::-1]))      # TOP
        side_c = min(side_c, side_c[::-1])                                          # RIGHT
        side_d = min("".join(images[tile][-1]), "".join(images[tile][-1][::-1]))    # BOTTOM

        tiles_d[tile] = [
            md5(side_a.encode()).hexdigest()[:DIGEST_LEN],
            md5(side_b.encode()).hexdigest()[:DIGEST_LEN],
            md5(side_c.encode()).hexdigest()[:DIGEST_LEN],
            md5(side_d.encode()).hexdigest()[:DIGEST_LEN],
        ]
        for side in tiles_d[tile]:
            if side in sides_d:
                sides_d[side].add(tile)
            else:
                sides_d[side] = {tile}

    non_overlapping_d = dict()
    for tile in tiles_d.keys():
        non_overlapping_count = 0
        for side in tiles_d[tile]:
            if sides_d[side] == {tile}:
                non_overlapping_count += 1
        non_overlapping_d[tile] = non_overlapping_count

    res = 1
    corners = []
    for non_overlap in non_overlapping_d.keys():
        if non_overlapping_d[non_overlap] == 2:
            res *= non_overlap
            corners.append(non_overlap)
    print("1:", res)

    # PART TWO
    image_top_row = get_top_row(images, tiles_d, sides_d, corners, corners[0])
    image = [image_top_row]

    for i in range(0, int(sqrt(len(images))) - 1):
        current_row = image[i]
        new_row = []
        for square in current_row:
            neighbor = get_bottom_neighbour(images, tiles_d, sides_d, square)
            new_row.append(neighbor)
        image.append(new_row)

    # for image_row in image:
    #     print(image_row)

    fresh_image, p_image = strip_image(images, image)
    # print(p_image)
    # for image_row in fresh_image:
    #     print(image_row)

    fresh_image = [list(part) for part in fresh_image]

    start_image = deepcopy(fresh_image)

    # variants = [
    #     deepcopy(start_image),
    #     rotate2d(deepcopy(start_image)),
    #     rotate2d(rotate2d(deepcopy(start_image))),
    #     rotate2d(rotate2d(rotate2d(deepcopy(start_image)))),
    #     flip_horizontal2d(deepcopy(start_image)),
    #     rotate2d(flip_horizontal2d(deepcopy(start_image))),
    #     rotate2d(rotate2d(flip_horizontal2d(deepcopy(start_image)))),
    #     rotate2d(rotate2d(rotate2d(flip_horizontal2d(deepcopy(start_image))))),
    # ]

    start_image = deepcopy(start_image)
    sea_hashtags_count = count_hashtags(SEA_MONSTER.splitlines())
    image_hashtag_count = count_hashtags(start_image)

    sea_monster_count, new_image = count_sea_monsters(deepcopy(start_image))
    print("2: {} (👺), {} (#)".format(sea_monster_count, image_hashtag_count - sea_hashtags_count * sea_monster_count))


if __name__ == '__main__':
    solution()
