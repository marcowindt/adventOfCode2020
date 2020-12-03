import os


def solution(target: int = 2020):
    nums = []
    with open(os.path.join(os.path.dirname(__file__), './input.txt'), 'r') as fd:
        for line in fd:
            nums.append(int(line.split("\n")[0]))

    # PART ONE
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                print("1:", nums[i], nums[j], nums[i] * nums[j])

    # PART TWO
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    print("2:", nums[i], nums[j], nums[k], nums[i] * nums[j] * nums[k])


if __name__ == "__main__":
    solution()
