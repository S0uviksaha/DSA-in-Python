__package__ = "3. Matrix"

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxSum = 0

        for i in range(0, len(accounts)):
            sum = 0
            for j in range(0, len(accounts[0])):
                sum += accounts[i][j]
            
            if sum > maxSum:
                maxSum = sum
        
        return maxSum


if __name__ == "__main__":
    m = int(input("Enter number of customers: "))
    n = int(input("Enter number of banks per customer: "))
    
    accounts = []
    print(f"Enter wealth for each customer (space-separated {n} values per customer):")
    for _ in range(m):
        row = list(map(int, input().split()))
        accounts.append(row)

    solution = Solution()
    result = solution.maximumWealth(accounts)

    print("\nMaximum Wealth:", result)