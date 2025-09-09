__package__ = "Python Basics"

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        F = [0] * (n + 1)
        F[1] = 1

        for i in range(2, n + 1):
            F[i] = F[i - 1] + F[i - 2]

        return F[n]

if __name__ == "__main__":
    n = int(input("Enter a number (n): "))

    solution = Solution()
    result = solution.fib(n)

    print(f"Fibonacci number at position {n} = {result}")
