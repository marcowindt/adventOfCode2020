
if __name__ == "__main__":
    TARGET = 2020
    nums = []
    with open('input.txt', 'r') as fd:
        for line in fd:
            nums.append(int(line.split("\n")[0]))

    # PART ONE
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == TARGET:
                print("1:", nums[i], nums[j], nums[i] * nums[j])

    # PART TWO
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if nums[i] + nums[j] + nums[k] == TARGET:
                    print("2:", nums[i], nums[j], nums[k], nums[i] * nums[j] * nums[k])
