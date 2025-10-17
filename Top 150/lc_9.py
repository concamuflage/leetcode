# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         # solution using string
#         if x < 0:
#             return False
#         x_str = str(x)
#         left = 0
#         right = len(x_str) - 1
#         while left <= right:
#             if x_str[left] != x_str[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         # trace 121 and 1221 , you will understand. 

#         # solution without using string
#         if x < 0:
#             return False
#         if x % 10 == 0 and x != 0:
#             return False
#         # reverse the second half

#         reversed_half = 0
#         while x > reversed_half:
#             reversed_half = reversed_half*10 + x % 10
#             x //= 10 
#         # for 121, x will be 1 and reversed_half will be 12
#         # we remove the 2 and compare.
#         return reversed_half == x or reversed_half // 10 == x 
    
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # this solution complete reverses the number
        # pro: code is simpler to understand. 
        # con: slower than just reversing the first half.
        original = x
        # solution without using string
        if x < 0:
            return False
        reversed_half = 0
        while x > 0:
            reversed_half = reversed_half*10 + x % 10
            x //= 10 

        # for 121, x will be 1 and reversed_half will be 12
        # we remove the 2 and compare.
        return reversed_half == original
        


sol = Solution()

print(sol.isPalindrome(10)) # false
print(sol.isPalindrome(1)) # true
print(sol.isPalindrome(22)) # true
print(sol.isPalindrome(78)) # false
print(sol.isPalindrome(121)) # true
print(sol.isPalindrome(123)) # false
print(sol.isPalindrome(12345)) # false
print(sol.isPalindrome(66666)) # true
print(sol.isPalindrome(-22)) # false