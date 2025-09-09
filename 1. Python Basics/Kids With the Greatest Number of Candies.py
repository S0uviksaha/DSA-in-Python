__package__ = "1. Python Basics"

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = 0
        output = []

        for i in candies:
            if i > maxCandies:
                maxCandies = i

        for i in candies:
            if (i + extraCandies) >= maxCandies:
                output.append(True)
            else:
                output.append(False)

        return output

if __name__ == "__main__":
    candies = list(map(int, input("Enter candies for each kid (space-separated): ").split()))
    extraCandies = int(input("Enter extra candies: "))

    solution = Solution()
    result = solution.kidsWithCandies(candies, extraCandies)

    print("\nResult (True = kid can have greatest number of candies):")
    print(result)
