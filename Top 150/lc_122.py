from typing import List

# greedy approach
# class Solution:
#     def maxProfit(self, prices):
#         profit = 0
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i - 1]:
#                 profit += prices[i] - prices[i - 1]
#         return profit

# dynamic programming
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         hold = -10*9  # max profit when holding a stock, just initialized to a small number
#         cash = 0       # max profit when not holding
#         for p in prices:
#             print("hold","cash","p","cash-p","hold+p")
#             print(hold," ", cash, " ",p," ", cash-p," " ,hold + p )
#             hold = max(hold, cash - p)  # buy
#             cash = max(cash, hold + p)  # sell
#         return cash

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_profit = 0
        buy_profit = 0
        current_profit = 0
        for price in prices:
            # buy
            buy_profit = current_profit - price
            # sell
            sell_profit = current_profit + price
            current_profit = max(buy_profit,sell_profit)

        return current_profit

sol = Solution()

print(sol.maxProfit([7,1,5])) # 4
# print(sol.maxProfit([7,1,5,3,6,4])) # 7
# print(sol.maxProfit([1,2,3,4,5])) # 4
# print(sol.maxProfit([5,4,3,2,1])) # 0
