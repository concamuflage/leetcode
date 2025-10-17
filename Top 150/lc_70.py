# class Solution:
#     def climbStairs(self, n: int) -> int:
#         # bottom up with iteration,using a list
#         if n <= 2:
#             return n 
#         dp = [0] * (n+1)
#         dp[1],dp[2] = 1,2
#         for index in range(3,n+1):
#             dp[index] = dp[index-1] + dp[index-2]
#         return dp[-1]

class Solution:
    def climbStairs(self, n: int) -> int:
        # top down with memoization
        dict = {1:1,2:2}
        self.climb(n,dict)
        return dict[n]
    
    def climb(self,n,dict):
        if n  not in dict:
            dict[n] = self.climb(n-2,dict) + self.climb(n-1,dict)
        return dict[n]

sol = Solution()
print(sol.climbStairs(1)) # 1
print(sol.climbStairs(2)) # 2
print(sol.climbStairs(3)) # 3
print(sol.climbStairs(4)) # 5
print(sol.climbStairs(5)) # 8

