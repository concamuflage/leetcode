# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         count_of_val = 0
#         for index in range(len(nums)):
#             if nums[index] == val:
#                 nums[index] = 60 
#                 count_of_val +=1
#         nums.sort()
#         return len(nums)- count_of_val
    
# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
            
#         end_index = len(nums) - 1
#         front_index = 0 
#         count_of_val = 0
#         while front_index < end_index:
#             if nums[front_index] == val:
#                 try:
#                     if nums[front_index] != nums[end_index]:
#                         nums[front_index],nums[end_index] = nums[end_index],nums[front_index]
#                         end_index -= 1
#                     else:
#                         end_index -= 1
#                     count_of_val += 1
#                 except IndexError:
#                     print(IndexError)
#                     end_index -= 1
#             else:
#                  front_index += 1
#         remaining = len(nums)- count_of_val
#         for range in count_of_val:
#             nums.pop()
#         return remaining 


from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums) - 1
        i = 0
        while i <= end:
            if nums[i] == val:
                nums[i] = nums[end]
                end -= 1
            else:
                i += 1
        return end + 1  # number of elements not equal to val