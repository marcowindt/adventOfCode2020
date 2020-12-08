import os


TEST_OP_CODES = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


def run(op_codes: list, current: int = 0, accumulator: int = 0) -> (int, bool):
    seen = []
    while current not in seen and current < len(op_codes):
        seen.append(current)
        if op_codes[current][0] == "acc":
            accumulator += op_codes[current][1]
            current += 1
        elif op_codes[current][0] == "jmp":
            current += op_codes[current][1]
        else:
            # nop
            current += 1

    return accumulator, current == len(op_codes)


def solution():
    # op_codes = TEST_OP_CODES
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        op_codes = fd.read()
    op_codes = [(op_code.split(" ")[0], int(op_code.split(" ")[1])) for op_code in op_codes.split("\n")]

    accumulator, terminated = run(op_codes)
    print("1: {} {}".format(accumulator, terminated))

    jmp_and_nop = [idx for idx, op_code in enumerate(op_codes) if op_code[0] != "acc"]
    for idx in jmp_and_nop:
        if op_codes[idx][0] == "jmp":
            op_codes[idx] = "nop", op_codes[idx][1]
            accumulator, terminated = run(op_codes)
            if terminated:
                print("2: {} (idx): {} (acc) {} (terminated)".format(idx, accumulator, terminated))
            op_codes[idx] = "jmp", op_codes[idx][1]
        elif op_codes[idx][0] == "nop":
            op_codes[idx] = "jmp", op_codes[idx][1]
            accumulator, terminated = run(op_codes)
            if terminated:
                print("2: {} (idx): {} (acc) {} (terminated)".format(idx, accumulator, terminated))
            op_codes[idx] = "nop", op_codes[idx][1]


if __name__ == '__main__':
    solution()
