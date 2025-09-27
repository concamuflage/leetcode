class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_pointer = 0 # elements before this index is unique
        current_pointer = 0 # current index
        reference = None 
        unique_values_count = 0

        while current_pointer <= len(nums) - 1:
            current_value = nums[current_pointer]
            if current_value != reference: # encounters a different value
                unique_values_count += 1
                reference = current_value
                if reference is not None:
                    nums[unique_pointer],nums[current_pointer] = nums[current_pointer],nums[unique_pointer]
                current_pointer += 1
                unique_pointer += 1
            else:
                current_pointer += 1

        return unique_values_count