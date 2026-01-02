from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            # total += diff
            tank += diff

            if tank < 0:
                start = i + 1
                tank = 0

        return start if total >= 0 else -1




s = Solution()
# result = s.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2])
# result = s.canCompleteCircuit([2,3,4], [3,4,3])
result = s.canCompleteCircuit([5,8,2,8],[6,5,6,6])


print(result)
