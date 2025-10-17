from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for index in range(len(digits)-1,-1,-1):
            target = digits[index]
            result = target + carry 
            if result == 10:
                if index == 0:
                    digits[index] = 0
                    digits.insert(0,1)
                else:
                    carry == 1
                    digits[index] = 0

            else:
                digits[index] = result 
                break
        return digits

            

sol = Solution()


print(sol.plusOne([0])) # [1]
print(sol.plusOne([8])) # [9]
print(sol.plusOne([9])) # [1,0]
print(sol.plusOne([1,0])) # [1,1]
print(sol.plusOne([9,9])) # [1,0,0]
print(sol.plusOne([8,9,9])) # [9,0,0]
print(sol.plusOne([9,9,9])) # [1,0,0,0]
