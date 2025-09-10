__package__ = "2. List"

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(0, len(prices) - 1):
            if prices[i+1] > prices[i]:
                profit += (prices[i+1] - prices[i])
        return profit


if __name__ == "__main__":
    prices = list(map(int, input("Enter stock prices separated by spaces: ").split()))

    solution = Solution()
    result = solution.maxProfit(prices)

    print("\nMaximum Profit:", result)