__package__ = "7. Searching"

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            sum1 = numbers[l] + numbers[r]
            if sum1 == target:
                return [l + 1, r + 1]  # 1-based index as per problem statement
            elif sum1 < target:
                l += 1
            else:
                r -= 1
        
        return []


if __name__ == "__main__":
    numbers = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
    target = int(input("Enter target: "))

    solution = Solution()
    result = solution.twoSum(numbers, target)

    if result:
        print(f"\nIndices (1-based) of the two numbers that sum to {target}: {result}")
    else:
        print("\nNo two numbers found that sum to target.")
