# class Solution:
#     # my solution
#     # manipulate the mask to check if the ith position is set or not.
#     def hammingWeight(self, n: int) -> int:
#         total = 0 
#         length = n.bit_length()
#         for index in range(length):
#             mask = 1 
#             mask <<= index
#             result = (n & mask)
#             if result:
#                 total +=1
#         return total


# class Solution:
#     # GPT solution
#     # right shift n to check if the ith position is set or not.
#     # it is more efficient than my solution because after right shifting n 
#     # for a few times, n might become 0 and the loop can be stopped.

#     def hammingWeight(self, n: int) -> int:
#         total = 0 
#         while n:
#             if n&1:
#                 total +=1
#             n >>= 1
#         return total


class Solution:
    # Brian Kernighan's 
    # This is the most efficient for this problem
    # Let's trace 7
    # n:        1101 1100 1000
    # n-1:      1100 1011 0111
    # n&n-1:    1100 1000 0000
    # if there is no borrow, the 1 disappears after the loop
    # if there is a borrow, the 1 also disappers after the loop
    # O(k), k is the number of set bits in the number.

 
    def hammingWeight(self,n: int) -> int:
        count = 0
        while n:
            n &= n - 1   # Clear the lowest set bit
            count += 1
        return count

sol = Solution()
# print(sol.hammingWeight(0)) # 0 
# print(sol.hammingWeight(1)) # 1 
# print(sol.hammingWeight(3)) # 2 
# print(sol.hammingWeight(4)) # 1
print(sol.hammingWeight(7)) # 3
        
