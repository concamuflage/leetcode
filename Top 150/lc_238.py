class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        prefix_array = [1]* length
        suffix_array = [1]* length
        answer = [1]* length
        # construct the prefix array

        for index in range(1,length):
            prefix_array[index] = nums[index-1]*prefix_array[index-1]

        # construct the suffix array
        for index in range(length-2,-1,-1):
            suffix_array[index] = nums[index+1]*suffix_array[index+1]

        # construct the answer array
        for index in range(0,length):
            answer[index] = prefix_array[index]*suffix_array[index]

        return answer

s = Solution()
print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([1,2]))