# from typing import List

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         // my initial solution
#         prev_num = float("inf") 
#         count = 0
#         index = 0 
#         while index < len(nums):
#             num = nums[index]
#             if num == prev_num:
#                 if count == 2:
#                     del nums[index]
#                     continue 
#                 count += 1
#             else: # first time see this num.
#                 prev_num = num
#                 count = 1 
#             index += 1
        
#         return len(nums)



# class Solution:
#     # gpt solution, concise but hard to understand.
#     def removeDuplicates(self, nums: list[int]) -> int:
#         i = 0  # slow pointer
#         for num in nums:
#             if i < 2 or num != nums[i - 2]:
#                 nums[i] = num
#                 i += 1
#         return i
    
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # I rewrote the gpt solution.
        # essentially, the counter is incremented only when a number
        # looks backward and finds out they are different. 
        
        if len(nums) < 3:
            return len(nums)
        
        count = 2 
        for index in range(2,len(nums)):
            if nums[index] != nums[index -2]:
                count += 1
        return count 

        
        
    

sol = Solution()

print(sol.removeDuplicates([1])) # 1
print(sol.removeDuplicates([1,1])) # 2
print(sol.removeDuplicates([1,1,3])) # 3
print(sol.removeDuplicates([1,1,3,3])) # 4
print(sol.removeDuplicates([1,1,2,2,2])) # 4
print(sol.removeDuplicates([0,0,1,1,1,1,2,3,3])) # 7

