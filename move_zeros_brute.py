nums = [2,3,4,0,0,9,8]
output = []

for i in range(len(nums)):
    if nums[i] != 0:
        output.append(nums[i])
for i in range(len(output),len(nums)):
    output.append(0)

print(output)
