# reference:https://www.youtube.com/watch?v=M9foA9gcL98

# use bit manipulation to solve this problem.
# manually calculate the sample in the video 
# and you may understand why does it work.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        while b:
            summary_without_carry = a ^ b 
            carry = (a & b) << 1
            a = summary_without_carry
            b = carry
        # bin generates a string from the binary integer.
        result = bin(a)[2:]
        return result


sol = Solution()
print(sol.addBinary("11","1")) # 100
print(sol.addBinary("1010","1011")) # 10101

