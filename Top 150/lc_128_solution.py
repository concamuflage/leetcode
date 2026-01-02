class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        s = set(nums)
        best = 0

        for x in s:
            # Only start counting if x is the start of a sequence
            if x - 1 not in s:
                y = x
                while y in s:
                    y += 1
                best = max(best, y - x)

        return best