import re
import os


def check_valid_ecl(color: str, colors=None) -> bool:
    if colors is None:
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return color in colors


def check_valid_pid(pid: str) -> bool:
    if len(pid) != 9:
        return False
    try:
        pid = int(pid)
        return True
    except ValueError:
        return False


def check_valid_hgt(hgt: str) -> bool:
    return (hgt[-2:] == 'in' and 59 <= int(hgt[:-2]) <= 76) or (hgt[-2:] == 'cm' and 150 <= int(hgt[:-2]) <= 193)


def check_valid_hcl(hcl: str) -> bool:
    hcl = hcl.split("#")
    if len(hcl) == 2:
        try:
            hcl = int(hcl[1], 16)
            return True
        except ValueError:
            return False
    return False


def check_valid_eyr(eyr: str, start: int = 2020, end: int = 2030):
    assert start <= end
    return start <= int(eyr) <= end


def check_valid_byr(byr: str, start: int = 1920, end: int = 2002):
    return check_valid_eyr(byr, start=start, end=end)


def check_valid_iyr(iyr: str, start: int = 2010, end: int = 2020):
    return check_valid_eyr(iyr, start=start, end=end)


def solution():
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        passports = fd.read()
    passports = passports.split("\n\n")
    passports = [passport.replace("\n", " ").split(" ") for passport in passports]
    passports = [{field.split(":")[0]: field.split(":")[1] for field in passport} for passport in passports]

    # PART ONE
    required = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}
    invalid_count = 0
    invalid_ids = []
    for i, passport in enumerate(passports):
        if not required.issubset(set(passport.keys())):
            invalid_count += 1
            invalid_ids.append(i)
    print("1:", len(passports) - invalid_count)

    # PART TWO
    invalid_count = len(invalid_ids)
    valid_funcs = {
        'byr': check_valid_byr,
        'iyr': check_valid_iyr,
        'eyr': check_valid_eyr,
        'hgt': check_valid_hgt,
        'hcl': check_valid_hcl,
        'ecl': check_valid_ecl,
        'pid': check_valid_pid,
    }
    for i, passport in enumerate(passports):
        if i in invalid_ids:
            continue
        for k in valid_funcs.keys():
            if not valid_funcs[k](passport[k]):
                invalid_count += 1
                break
    print("2:", len(passports) - invalid_count)


if __name__ == '__main__':
    solution()
