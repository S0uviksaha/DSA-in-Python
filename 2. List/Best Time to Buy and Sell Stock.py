__package__ = "3. Matrix"

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        profit = 0
        maxProfit = 0
        for i in prices[1:]:
            if i < buy:
                buy = i
            elif i > buy:
                sell = i
                profit = sell - buy
            maxProfit = max(profit, maxProfit)
        
        return maxProfit


if __name__ == "__main__":
    prices = list(map(int, input("Enter stock prices separated by spaces: ").split()))

    solution = Solution()
    result = solution.maxProfit(prices)

    print("\nMaximum Profit:", result)
