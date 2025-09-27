class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = None 
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            else:
                if num == candidate:
                    count += 1
                else: 
                    count -= 1
        return candidate
            