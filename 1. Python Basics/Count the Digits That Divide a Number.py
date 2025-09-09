__package__ = "1. Python Basics"

class Solution:
    def countDigits(self, num: int) -> int:
        number = num
        count = 0

        while num > 0:
            x = num % 10
            if number % x == 0:
                count += 1
            num //= 10

        return count

if __name__ == "__main__":
    num = int(input("Enter a number: "))

    solution = Solution()
    result = solution.countDigits(num)

    print(f"Count of digits that evenly divide {num}: {result}")
