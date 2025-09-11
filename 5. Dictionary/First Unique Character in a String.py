__package__ = "5. Dictionary"

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = {}
        for i in s:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1
        
        for i in range(len(s)):
            if dict1[s[i]] == 1:
                return i
        
        return -1


if __name__ == "__main__":
    s = input("Enter a string: ")

    solution = Solution()
    result = solution.firstUniqChar(s)

    if result != -1:
        print(f"\nIndex of first unique character: {result} (character: '{s[result]}')")
    else:
        print("\nNo unique character found.")
