__package__ = "4. String"

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li = s.split()
        return len(li[-1])


if __name__ == "__main__":
    s = input("Enter a sentence: ")

    solution = Solution()
    result = solution.lengthOfLastWord(s)

    print("\nLength of last word:", result)
