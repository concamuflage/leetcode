class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)

        h_index = 0
        for count,number in enumerate(citations,start = 1):
            if count > number:
                return h_index
            else:
                h_index = count
        return h_index

s = Solution()
# print(s.hIndex([0])) # should be 0
print(s.hIndex([3,0,6,1,5])) # should be 3



