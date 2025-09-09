__package__ = "2. List"

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        sum_ = 0  # use sum_ to avoid overwriting Python's built-in sum()
        for i in nums:
            sum_ += i
            output.append(sum_)
        return output

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

    solution = Solution()
    result = solution.runningSum(nums)

    print("Running sum of the array:")
    print(result)

