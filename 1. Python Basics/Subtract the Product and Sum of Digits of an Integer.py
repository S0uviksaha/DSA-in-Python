__package__ = "Python Basics"

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        add = 0  
        num = n

        while n > 0:
            r = n % 10
            product *= r
            add += r
            n //= 10

        return product - add

if __name__ == "__main__":
    n = int(input("Enter a number: "))

    solution = Solution()
    result = solution.subtractProductAndSum(n)

    print(f"Product of digits - Sum of digits for {n} = {result}")
