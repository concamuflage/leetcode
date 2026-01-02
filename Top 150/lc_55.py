from typing import List
class Solution:
    def canJump(self, nums):
        # if farthest can be reached, then all the positions before it can be reached too.

        farthest = 0
        for i, jump in enumerate(nums):
            # the following loop is important for case like [0,3,1,1,4]
            # in the loop, we can reach 3, but we shouldn't reach it.
            if i > farthest:
                return False     # can't even reach this index
            farthest = max(farthest, i + jump)
        return True


class Solution:
    def canJump(self, nums):
        dp = [0]*len(nums)
        dp[0] = 1
        for index,jump in enumerate(nums):
            if dp[index]:
                for index_two in range(jump+1):
                    result = index_two + index
                    if result < len(nums): # if it is a valid index in nums
                        dp[index_two + index] = 1
        return bool(dp[-1])


sol = Solution()

print(sol.canJump([2,0])) # true
print(sol.canJump([0,3,1,1,4])) # false
print(sol.canJump([2,3,1,1,4])) # True
print(sol.canJump([3,2,1,0,4])) # False
