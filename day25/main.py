import os


TEST_PUBLIC_KEYS = """5764801
17807724"""


def transform_subject(value: int = 1, subject: int = 7):
    value *= subject
    value %= 20201227
    return value


def solution():
    # pks = TEST_PUBLIC_KEYS
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        pks = fd.read()

    pks = [int(x) for x in pks.splitlines()]
    card_pk, door_pk = pks[0], pks[1]

    card_loop_size = -1
    door_loop_size = -1

    cur_val = 1
    i = 0
    while card_loop_size == -1 or door_loop_size == -1:
        cur_val = transform_subject(cur_val)

        if cur_val == card_pk:
            card_loop_size = i
        if cur_val == door_pk:
            door_loop_size = i
        i += 1

    # print(card_loop_size, door_loop_size)

    i = 0
    enc_key = 1
    while i <= card_loop_size:
        enc_key = transform_subject(enc_key, door_pk)
        i += 1

    print("1:", enc_key)


if __name__ == '__main__':
    solution()
