__package__ = "2. List"

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        k = 2
        for i in range(2, n):
            if nums[i] != nums[i - 2]:
                nums[k] = nums[i]
                k += 1

        return k

if __name__ == "__main__":
    nums = list(map(int, input("Enter a sorted list of numbers (space-separated): ").split()))

    solution = Solution()
    k = solution.removeDuplicates(nums)

    print(f"\nNumber of elements after allowing at most 2 duplicates: {k}")
    print(f"Array after processing: {nums[:k]}")
