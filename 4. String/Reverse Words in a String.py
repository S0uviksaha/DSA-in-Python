__package__ = "4. String"

class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split()
        li.reverse()
        ans = " ".join(li)
        return ans


if __name__ == "__main__":
    s = input("Enter a sentence: ")

    solution = Solution()
    result = solution.reverseWords(s)

    print("\nReversed words:")
    print(result)
