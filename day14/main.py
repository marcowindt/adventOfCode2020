import os


TEST_MEM = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

TEST_EXAMPLE = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""


def apply_bit_mask(mask: str, number: int) -> int:
    to_mask = list(format(number, '#038b')[2:])
    for i, bit in enumerate(mask):
        if bit == 'X':
            continue
        elif bit == '1':
            to_mask[i] = '1'
        elif bit == '0':
            to_mask[i] = '0'
    return int("".join(to_mask), 2)


def mem_mask(mask: str, address: int) -> list:
    xs_idx = []
    to_mask = list(format(address, '#038b')[2:])
    # first apply mask
    for i, bit in enumerate(mask):
        if bit == 'X':
            to_mask[i] = 'X'
            xs_idx.append(i)
        elif bit == '1':
            to_mask[i] = '1'
    # find all possible masks
    bit_strings = [list(format(i, '#0{}b'.format(len(xs_idx)+2))[2:]) for i in range(2**len(xs_idx))]
    addresses = []
    for bit_string in bit_strings:
        new_address = to_mask.copy()
        for i, bit in enumerate(bit_string):
            x_idx = xs_idx[i]
            new_address[x_idx] = bit
        addresses.append(int("".join(new_address), 2))
    return addresses


def solution():
    # instructions = TEST_MEM
    # instructions = TEST_EXAMPLE
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        instructions = fd.read()
    instructions = [(ins.split(" = ")[0], ins.split(" = ")[1]) if ins.split(" = ")[0] == 'mask' else ('mem', int(((ins.split(" = ")[0]).split("[")[1]).split("]")[0]), int(ins.split(" = ")[1])) for ins in instructions.splitlines()]

    # PART ONE
    memory = dict()
    mask = 'X' * 36
    for ins in instructions:
        if ins[0] == 'mask':
            mask = ins[1]
        else:
            memory[ins[1]] = apply_bit_mask(mask, int(ins[2]))
            # print(mem_address, ins[1], apply_bit_mask(mask, ins[1]))
    print("1:", sum(memory.values()))

    # PART TWO
    memory = dict()
    mask = '0' * 36
    for ins in instructions:
        if ins[0] == 'mask':
            mask = ins[1]
        else:
            addresses = mem_mask(mask, int(ins[1]))
            for address in addresses:
                # print(mem_address, format(address, '#038b'), address, ins[1])
                memory[address] = ins[2]
    print("2:", sum(memory.values()))


if __name__ == '__main__':
    solution()
