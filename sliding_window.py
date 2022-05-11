
def slidingwindow(arr, windowsize):

    arraylength = len(arr)
    if arraylength <= windowsize:
        return -1

    windowsum = sum(arr[i] for i in range(windowsize))
    max_sum = windowsum



    for i in range(arraylength-windowsize):
        windowsum = windowsum - arr[i] + arr[i+windowsize]
        max_sum = max(windowsum,max_sum)

    return max_sum


arr = [80, 160, 90, 100]
k = 2

answer = slidingwindow(arr, k)

print(answer)
