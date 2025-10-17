from typing import List

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # this is a naive method O(n^k)
#         for time in range(k):
#             last_element = nums.pop()
#             nums.insert(0,last_element)
#         return nums   
     
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # using swap 
#         # [1,2,3]
#         # [3,1,2] k = 1
#         # [2,3,1] k = 2
#         # O(k*n) if k is n, then O(n^2)
#         for time in range(k):
#             for index in range(len(nums)-1,0,-1):
#                 nums[index],nums[index-1] = nums[index-1],nums[index]
#         return nums
    
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums) 
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)
        return nums
    def reverse(self,nums,left,right):
        # O(n)
        while left <= right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1
            
sol = Solution()

print(sol.rotate([-1],2)) # [-1]
print(sol.rotate([1],0)) # [1]
print(sol.rotate([1],1)) # [1]
print(sol.rotate([1,2],1)) # [2,1]
print(sol.rotate([1,2],2)) # [1,2]
print(sol.rotate([1,2,3],1)) # [3,1,2]
print(sol.rotate([1,2,3],2)) # [2,3,1]
print(sol.rotate([1,2,3],3)) # [1,2,3]



