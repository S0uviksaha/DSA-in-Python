__package__ = "2. List"

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxSum = 0

        for i in nums:
            if sum < 0:
                sum = 0
            elif i + sum < 0:
                sum = 0
            else:
                sum += i

            maxSum = max(sum, maxSum)
        
        if maxSum == 0 and nums.count(0) == 0:
            return max(nums)
        
        return maxSum


if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

    solution = Solution()
    result = solution.maxSubArray(nums)

    print("\nMaximum Subarray Sum:", result)
