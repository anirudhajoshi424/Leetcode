
arr = [1,2,2,4,4,5,6,7,7,8]
c = {i: 0 for i in arr}
j = 0
output = []
for i in range(len(arr)):
    if c[arr[i]] == 0:
        arr[j] = arr[i]
        arr.append(j)
    else:
        c[arr[i]] = 1
print(arr)
