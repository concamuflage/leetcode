

class Solution:
    # this method is different from mine
    # to extract i-th bit from n
    # it rightshit the ith bit to the LSB position and & it with 1
    # the code is shorter, but not very straight forward. 
    
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1            # extract i-th bit from n
            res = res | (bit << (31 - i)) # place it at reversed position
        return res

# the following is an implementation of this video solution
# https://www.youtube.com/watch?v=UcoN6UjAI64
class Solution:
    def reverseBits(self, n: int) -> int:
        # Part 1
        # mask1 test if a digit in n is 1 or 0. 
        # it starts from LSB of n and move leftward.
        # if that bit is 1, then put that 1 into correct position in an res variable.
        # if that bit is 0, we don't change the correct position in res as that position is already 0.
        # Part 2 to put 1 at the correct position in the res variable.
        # we change mask2 so that the correct position in mask2 is 1 and the rest is 0.
        # we or mask2 and res variable, this puts 1 at desired position in res and the rest of the positions remain unchanged.

        # print("integer")
        res = 0
        for index in range(32):
            # reset masks in every loop
            mask1 = 1 # for detecting if certain position of n contains 1 or 0
            mask2 = 1 # for moving the 1 at certain position to its correct place in res.
            # print("index",index)
            mask1 = mask1 << index 
            result1 = n & mask1
            # print("mask1",bin(mask1))
            # print("result1",bin(result1))
            if result1: # if the tested position is a 1.
                # move it to correct position
                mask2 = mask2 << (31- index)
                # print("mask2",bin(mask2))
                # print("res",bin(res))
                res = res | mask2
                # print("new res",bin(res))
        return res 



sol = Solution()
print(sol.reverseBits(43261596))      #964176192
print(sol.reverseBits(2147483644))    #1073741822