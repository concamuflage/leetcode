from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -10**9  # max profit when holding a stock
        cash = 0       # max profit when not holding
        for p in prices:
            hold = max(hold, cash - p)  # buy
            cash = max(cash, hold + p)  # sell
        return cash
    
sol = Solution()

print(sol.maxProfit([7,1,5,3,6,4])) # 7
print(sol.maxProfit([1,2,3,4,5])) # 4
print(sol.maxProfit([5,4,3,2,1])) # 0
