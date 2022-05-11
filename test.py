def binarysearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low<=high:

        mid = (low+high)//2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1
            
    return -1

arr = [1,2,3,4,9,6]
target = 2

result = binarysearch(arr, target)

if result != -1:
    print("Element searching for is at %d" % result)
else:
    print("Element not present")
