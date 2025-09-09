__package__ = "1. Python Basics"

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        if n % 2 != 0 or n <= 0:
            return False
        
        return self.isPowerOfTwo(n // 2) 

if __name__ == "__main__":
    n = int(input("Enter a number: "))

    solution = Solution()
    result = solution.isPowerOfTwo(n)

    if result:
        print(f"{n} is a power of 2")
    else:
        print(f"{n} is NOT a power of 2")
