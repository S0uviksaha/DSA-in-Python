__package__ = "4. String"

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        st = s.lower()

        while i < j:
            if not st[i].isalnum():
                i += 1
            elif not st[j].isalnum():
                j -= 1
            else:
                if st[i] != st[j]:
                    return False
                i += 1
                j -= 1

        return True


if __name__ == "__main__":
    s = input("Enter a string: ")

    solution = Solution()
    result = solution.isPalindrome(s)

    if result:
        print("\nThe string iS a palindrome (ignoring non-alphanumeric characters).")
    else:
        print("\nThe string is NOT a palindrome.")
