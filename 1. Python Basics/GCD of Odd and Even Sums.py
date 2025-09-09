__package__ = "Python Basics"

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # oddSum = n * n
        # evenSum = n * (n - 1)
        # gcd(oddSum, evenSum) = gcd(n*n, n*(n-1)) = n
        return n

if __name__ == "__main__":
    n = int(input("Enter a number (n): "))

    solution = Solution()
    result = solution.gcdOfOddEvenSums(n)

    print(f"GCD of odd and even sums for n = {n} is {result}")
