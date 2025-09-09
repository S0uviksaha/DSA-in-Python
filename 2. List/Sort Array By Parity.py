__package__ = "2. List"

from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        k = 0
        for i in range(n):
            if nums[i] % 2 == 0:
                # Swap even element to position k
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
        return nums

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

    solution = Solution()
    result = solution.sortArrayByParity(nums)

    print("\nArray after sorting by parity (evens first):")
    print(result)
