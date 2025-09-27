class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        if len(prices) == 1 or len(prices) == 0:
            return 0
        left_pointer = 0 # buying point
        right_pointer = 1 # selling point
        max_profit = max(0,prices[right_pointer]-prices[left_pointer])
        while right_pointer <= len(prices) - 2:
            if prices[right_pointer] < prices[left_pointer]:
                left_pointer = right_pointer
            right_pointer += 1
            profit = prices[right_pointer]-prices[left_pointer]
            max_profit = max(max_profit,profit)
        return max_profit