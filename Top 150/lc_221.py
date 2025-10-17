from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num 
        return result 

sol = Solution()

print(sol.singleNumber([2,2,1])) # 1
print(sol.singleNumber([2000,2000,3,3,5])) # 5
print(sol.singleNumber([2,2,10000])) # 10000
print(sol.singleNumber([2,1,2,400001,400001])) # 1
print(sol.singleNumber([-1])) # -1
print(sol.singleNumber([-2,-1,-2,4,4])) -1