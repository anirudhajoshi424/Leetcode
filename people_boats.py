from typing import List
class Solution:
    def peopleboats(self, people: List[int] ,limit: int) -> int:
        people.sort()
        heavyP = len(people) - 1
        lightP = 0
        boat = 0
        while heavyP >= lightP:
            if people[heavyP] + people[lightP] <= limit:
                boat += 1
                lightP += 1
                heavyP -= 1
            else:
                boat += 1
                heavyP -= 1
        return boat



s = Solution()

result = s.peopleboats([1,2,3,4,4,5], 6)

print(result)
