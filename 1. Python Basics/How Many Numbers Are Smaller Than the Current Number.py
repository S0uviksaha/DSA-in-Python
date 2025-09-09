__package__ = "1. Python Basics"

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            output.append(count)
        return output

if __name__ == "__main__":
    # Take user input as a list of integers
    nums = list(map(int, input("Enter numbers separated by spaces (e.g -> 2 6 3 7 9): ").split()))
    
    solution = Solution()
    result = solution.smallerNumbersThanCurrent(nums)
    
    print("Result (count of smaller numbers for each element):")
    print(result)
