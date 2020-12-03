import os


def solution():
    passwords = []
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        for line in fd:
            record = line.split("\n")[0]
            cols = record.split(" ")
            password_details = {
                "min": int(cols[0].split("-")[0]),
                "max": int(cols[0].split("-")[1]),
                "char": cols[1].split(":")[0],
                "chars": cols[2]
            }
            passwords.append(password_details)

    # PART ONE
    cnt = 0
    for password_details in passwords:
        if password_details["min"] > password_details["chars"].count(password_details["char"]) or password_details["max"] < password_details["chars"].count(password_details["char"]):
            cnt += 1
    print("1: cnt:", len(passwords) - cnt)

    # PART TWO
    cnt = 0
    for password_details in passwords:
        if password_details["chars"][password_details["min"] - 1] == password_details["char"] and \
                password_details["chars"][password_details["max"] - 1] != password_details["char"]:
            cnt += 1
        elif password_details["chars"][password_details["min"] - 1] != password_details["char"] and \
                password_details["chars"][password_details["max"] - 1] == password_details["char"]:
            cnt += 1
    print("2: cnt:", cnt)


if __name__ == "__main__":
    solution()
