
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self._recurSearchInsert(nums,target,0,len(nums)-1)
    def _recurSearchInsert(self,nums,target,left, right):
        # base
        if left > right:
            return left
        #
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            # search the right side
            left = mid + 1
        else: 
            # sear the right side
            right = mid - 1
        return self._recurSearchInsert(nums,target,left,right)



sol = Solution()

print(sol.searchInsert([], 2))          # 0
print(sol.searchInsert([1], 1))         # 0
print(sol.searchInsert([11, 13], 13))   # 1
print(sol.searchInsert([2, 3, 7], 7))   # 2
print(sol.searchInsert([13, 19, 21, 28], 20))  # 2
