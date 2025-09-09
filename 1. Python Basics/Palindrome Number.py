__package__ = "1. Python Basics"

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp1 = x
        temp2 = 0

        if x < 0:
            return False

        while temp1 > 0:
            r = temp1 % 10
            temp2 = temp2 * 10 + r
            temp1 //= 10

        return temp2 == x

if __name__ == "__main__":
    x = int(input("Enter a number: "))

    solution = Solution()
    result = solution.isPalindrome(x)

    if result:
        print(f"{x} is a Palindrome ")
    else:
        print(f"{x} is NOT a Palindrome ")
