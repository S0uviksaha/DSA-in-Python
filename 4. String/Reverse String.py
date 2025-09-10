__package__ = "4. String"

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1

        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1


if __name__ == "__main__":
    s = list(input("Enter a string: "))  # Convert string to list of characters

    solution = Solution()
    solution.reverseString(s)  # This reverses s in-place

    print("\nReversed string:")
    print("".join(s))  # Join back to a string for display
