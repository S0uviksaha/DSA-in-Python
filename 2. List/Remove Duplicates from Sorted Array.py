__package__ = "2. List"

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        j = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1

        return j

if __name__ == "__main__":
    nums = list(map(int, input("Enter a sorted list of numbers (space-separated): ").split()))

    solution = Solution()
    k = solution.removeDuplicates(nums)

    print(f"\nNumber of unique elements: {k}")
    print(f"Array after removing duplicates: {nums[:k]}")