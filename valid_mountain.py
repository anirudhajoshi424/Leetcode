from typing import List

class Solution:
    def validmountain(self, arr: List[int]) -> bool:

        i = 1

        while (i<len(arr) and arr[i] > arr[i-1]):
            i += 1
        if(i == 1 or i == len(arr)):
            return False

        while (i<len(arr) and arr[i] < arr[i-1]):
            i += 1

        return i == len(arr)

s = Solution()

answer = s.validmountain([1,2,3,4,2,1])

print(answer)
