class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        lookup = {}
        biggest = float("-inf")
        smallest = float("inf")
        for num in nums:
            if num not in lookup:
                lookup[num] = 0
            biggest = max(biggest,num)
            smallest = min(smallest,num)

        global_max = biggest
        longest = 0
        number = smallest
        biggest = smallest

        while number <= global_max:
            number +=1
            if number not in lookup:
                count = biggest - smallest + 1
                longest = max(count,longest)
                # keep incrementing until we find a the next smallest number in the sequence.
                while number < global_max:
                    number += 1
                    if number in lookup:
                        smallest = number
                        biggest = number
                        break
            else:
                biggest = number
        return longest
s = Solution()
a = [1,100]
print(s.longestConsecutive(a))






