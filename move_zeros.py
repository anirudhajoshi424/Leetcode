
def movezeros(nums):
    j = 0
    n = len(nums)

    for i in range(n):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    for x in range(j, n):
        nums[x] = 0

    return nums

nums = [1, 0, 0, 3, 12, 7, 8, 87]

answer = movezeros(nums)

print(answer)
