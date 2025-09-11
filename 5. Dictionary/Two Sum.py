__package__ = "5. Dictionary"

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict1 = {}

        for i in range(n):
            rem = target - nums[i]
            if rem in dict1:
                return [dict1[rem], i]
            else:
                dict1[nums[i]] = i
        
        return []


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    target = int(input("Enter target: "))

    solution = Solution()
    result = solution.twoSum(nums, target)

    if result:
        print("\nIndices of the two numbers that sum to target:", result)
    else:
        print("\nNo two numbers found that sum to target.")
