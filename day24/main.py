import os

TEST_TILES = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew"""


def next_tile(current_tile: tuple, direction: str):
    if direction == "e":
        return current_tile[0] + 1, current_tile[1]
    elif direction == "se":
        if current_tile[1] % 2 == 0:
            return current_tile[0], current_tile[1] + 1
        else:
            return current_tile[0] + 1, current_tile[1] + 1
    elif direction == "sw":
        if current_tile[1] % 2 == 0:
            return current_tile[0] - 1, current_tile[1] + 1
        else:
            return current_tile[0], current_tile[1] + 1
    elif direction == "w":
        return current_tile[0] - 1, current_tile[1]
    elif direction == "nw":
        if current_tile[1] % 2 == 0:
            return current_tile[0] - 1, current_tile[1] - 1
        else:
            return current_tile[0], current_tile[1] - 1
    elif direction == "ne":
        if current_tile[1] % 2 == 0:
            return current_tile[0], current_tile[1] - 1
        else:
            return current_tile[0] + 1, current_tile[1] - 1


def neighbors(d_tile: tuple):
    ns = []
    for direction in ['e', 'w', 'se', 'sw', 'ne', 'nw']:
        ns.append(next_tile(d_tile, direction))
    return ns


def count_black_tiles(tiles_dict: dict, tiles: list):
    cnt = 0
    for d_tile in tiles:
        if d_tile in tiles_dict and tiles_dict[d_tile]:
            cnt += 1
            if cnt == 3:
                return cnt
    return cnt


def tile_to_flip(instruction: str, ref: tuple = (0, 0)):
    i = 0
    current_tile = ref
    while i < len(instruction):
        if instruction[i] == 'e' or instruction[i] == 'w':
            current_tile = next_tile(current_tile, instruction[i])
            i += 1
        elif instruction[i] == 's' or instruction[i] == 'n':
            current_tile = next_tile(current_tile, instruction[i:(i + 2)])
            i += 2
    return current_tile


def flip_tile(tiles_dict: dict, d_tile: tuple):
    if d_tile in tiles_dict:
        tiles_dict[d_tile] = not tiles_dict[d_tile]
    else:
        tiles_dict[d_tile] = True  # black
    return tiles_dict


def flip_tiles(tiles_dict: dict, d_tiles: list):
    for d_tile in d_tiles:
        tiles_dict = flip_tile(tiles_dict, d_tile)
    return tiles_dict


def increase_tiles_by_neighbors(tiles_dict: dict):
    ns = set()
    for d_tile in tiles_dict:
        ns = ns.union(set(neighbors(d_tile)))

    for d_tile in ns:
        if d_tile not in tiles_dict:
            tiles_dict[d_tile] = False

    return tiles_dict


def process_day(tiles_dict: dict):
    tiles_to_flip = []
    tiles_dict = increase_tiles_by_neighbors(tiles_dict)

    for d_tile in tiles_dict:
        tile_neighbors = neighbors(d_tile)
        count_black = count_black_tiles(tiles_dict, tile_neighbors)
        # print(tiles_dict[d_tile], count_black)
        if tiles_dict[d_tile] and (count_black == 0 or count_black > 2):
            tiles_to_flip.append(d_tile)
        elif not tiles_dict[d_tile] and count_black == 2:
            tiles_to_flip.append(d_tile)

    return flip_tiles(tiles_dict, tiles_to_flip)


def process_days(tiles_dict: dict, days: int = 1):
    for day in range(days):
        process_day(tiles_dict)


# https://i.stack.imgur.com/4QKD2.jpg
def solution():
    # tiles = TEST_TILES
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        tiles = fd.read()
    tiles = tiles.splitlines()

    tiles_dict = dict()

    for tile in tiles:
        flip_tile(tiles_dict, tile_to_flip(tile))

    print("1:", sum([1 if tiles_dict[d_tile] else 0 for d_tile in tiles_dict]))

    process_days(tiles_dict, 100)
    print("2:", sum([1 if tiles_dict[d_tile] else 0 for d_tile in tiles_dict]))


if __name__ == '__main__':
    solution()
