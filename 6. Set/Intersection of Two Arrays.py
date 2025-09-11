__package__ = "6. Set"

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)
        return list(n1.intersection(n2))


if __name__ == "__main__":
    nums1 = list(map(int, input("Enter first array (space-separated): ").split()))
    nums2 = list(map(int, input("Enter second array (space-separated): ").split()))

    solution = Solution()
    result = solution.intersection(nums1, nums2)

    print("\nIntersection of the two arrays:")
    print(result)