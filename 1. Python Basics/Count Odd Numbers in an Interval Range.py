__package__ = "Python Basics"

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 1 or high % 2 == 1:
            return (high - low) // 2 + 1
        return (high - low) // 2

if __name__ == "__main__":
    low = int(input("Enter the low value: "))
    high = int(input("Enter the high value: "))

    solution = Solution()
    result = solution.countOdds(low, high)

    print(f"Number of odd numbers between {low} and {high}: {result}")
