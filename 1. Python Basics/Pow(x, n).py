__package__ = "Python Basics"

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x, n)

if __name__ == "__main__":
    x = float(input("Enter the base (x): "))
    n = int(input("Enter the exponent (n): "))

    solution = Solution()
    result = solution.myPow(x, n)

    print(f"{x} raised to the power {n} = {result}")
